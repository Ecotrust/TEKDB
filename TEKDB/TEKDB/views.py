import contextlib
from dal import autocomplete
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.contenttypes.models import ContentType
from django.core import management
from django.db import connection
from django.db.models import Q
from django.http import HttpResponse, FileResponse, JsonResponse
import io
import os
import shutil
from TEKDB.utils import bytes_to_readable, check_disk_space
from TEKDB.models import (
    Citations,
    Media,
    Places,
    PlacesResourceEvents,
    Resources,
    ResourcesActivityEvents,
)
import tempfile
import zipfile
from configuration.models import Configuration


def get_related(request, model_name, id):
    from django.apps import apps
    import json

    if not (
        request.user.is_authenticated
        and request.user.has_perm("TEKDB.change_%s" % model_name.lower())
    ):
        return HttpResponse("Unauthorized", status=401)
    data = json.dumps([])
    try:
        model = apps.get_model("TEKDB", model_name)
        instance = model.objects.get(pk=id)
        if hasattr(instance, "get_related_objects"):
            data = json.dumps(instance.get_related_objects(id))
    except Exception:
        pass
    return HttpResponse(data, content_type="application/json")


# from https://www.geeksforgeeks.org/working-zip-files-python/
def get_all_file_paths(directory, cwd=False):
    if cwd:
        os.chdir(cwd)
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths


def get_directory_size(directory):
    total = 0
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                total += os.path.getsize(filepath)
            except OSError:
                continue
    return total


# Only Admins!
@user_passes_test(lambda u: u.is_superuser)
def ExportDatabase(request, test=False):
    datestamp = datetime.now().strftime("%Y%m%d")

    os.chdir(os.path.join(settings.MEDIA_ROOT, ".."))
    relative_media_directory = settings.MEDIA_ROOT.split(os.path.sep)[-1]
    media_paths = get_all_file_paths(relative_media_directory, cwd=os.getcwd())
    media_size = get_directory_size(relative_media_directory)

    tmp_path = tempfile.gettempdir()
    has_space, free_bytes = check_disk_space(media_size, tmp_path)
    if not has_space:
        status_code = 507
        status_message = f"Not enough disk space to export the database. The media directory is {bytes_to_readable(media_size)} but only {bytes_to_readable(free_bytes)} is available. Please free up disk space or contact your IT team."
        response = JsonResponse(
            {
                "status_code": status_code,
                "status_message": status_message,
            },
            status=507,
        )
        response.set_cookie("export_status", "error", path="/")
        return response

    tmp_zip = tempfile.NamedTemporaryFile(
        delete=False, prefix=f"{datestamp}_backup_", suffix=".zip"
    )

    response = HttpResponse()
    try:
        dumpfile = f"{datestamp}_backup.json"
        json_buffer = io.StringIO()
        excludes = getattr(settings, "EXPORT_DUMP_EXCLUDE", [])
        management.call_command(
            "dumpdata",
            exclude=excludes,
            indent=2,
            stdout=json_buffer,
        )

        # Write the zip with compression — no temp directory needed
        with zipfile.ZipFile(tmp_zip.name, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            zf.writestr(dumpfile, json_buffer.getvalue())
            json_buffer.close()  # Free memory as soon as possible
            for media_file in media_paths:
                zf.write(media_file)

        response = FileResponse(open(tmp_zip.name, "rb"))

    finally:
        try:
            if not test:
                os.remove(tmp_zip.name)
            response.set_cookie("export_status", "done", path="/")
        except (PermissionError, NotADirectoryError):
            response.set_cookie("export_status", "error", path="/")
            pass
    return response


def getDBTruncateCommand():
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        management.call_command("sqlflush")
    full_output = f.getvalue()
    cmd_list = full_output.split("\n")
    return [x for x in cmd_list if not x == ""]


# Only Admins!
@user_passes_test(lambda u: u.is_superuser)
def ImportDatabase(request):
    status_code = 500
    status_message = "An unknown error occurred."
    if not request.method == "POST":
        status_code = 405
        status_message = "Request method not allowed. Must be a post."
        return JsonResponse(
            {"status_code": status_code, "status_message": status_message},
            status=status_code,
        )
    else:
        if "MEDIA_DIR" in request.POST.keys() and os.path.exists(
            request.POST["MEDIA_DIR"]
        ):
            # used for testing so current media is not overwritten
            media_dir = request.POST["MEDIA_DIR"]
        else:
            media_dir = settings.MEDIA_ROOT
        # Unzip file
        if "import_file" in request.FILES.keys():
            with tempfile.TemporaryDirectory() as tempdir:
                try:
                    tmp_zip_file = tempfile.NamedTemporaryFile(
                        mode="wb+", delete=True, suffix=".zip"
                    )
                    for chunk in request.FILES["import_file"].chunks():
                        tmp_zip_file.write(chunk)
                    tmp_zip_file.seek(0)

                except Exception as e:
                    status_code = 500
                    status_message = f'Unable to read the provided file. Be sure it is a zipped file containing a .json representing the database and a "media" directory containing any static files. {e}'
                    return JsonResponse(
                        {"status_code": status_code, "status_message": status_message},
                        status=status_code,
                    )
                if zipfile.is_zipfile(tmp_zip_file):
                    zip = zipfile.ZipFile(tmp_zip_file, "r")
                    non_media = [
                        x for x in zip.namelist() if "media" not in x and ".json" in x
                    ]
                    # Validate Zip Contents
                    if not len(non_media) == 1 or len(zip.namelist()) < 2:
                        status_code = 500
                        status_message = "Received malformed import file. Must be a zipfile contailing one JSON file and a directory named 'media'"
                        return JsonResponse(
                            {
                                "status_code": status_code,
                                "status_message": status_message,
                            },
                            status=status_code,
                        )
                    # --- Pre-flight disk space check ---
                    # We need space for the JSON fixture in tempdir plus
                    # the media files written to MEDIA_ROOT. Calculate the
                    # uncompressed size of the fixture and media separately.
                    fixture_name = non_media[0]
                    media_members = [
                        m
                        for m in zip.namelist()
                        if m.startswith("media/") and not m.endswith("/")
                    ]

                    fixture_size = sum(
                        info.file_size
                        for info in zip.infolist()
                        if info.filename == fixture_name
                    )
                    media_size = sum(
                        info.file_size
                        for info in zip.infolist()
                        if info.filename in media_members
                    )

                    # Check temp directory space (for the extracted fixture)
                    tmp_path = tempfile.gettempdir()
                    has_tmp_space, tmp_free = check_disk_space(fixture_size, tmp_path)

                    if not has_tmp_space:
                        status_code = 507
                        status_message = f"Not enough disk space to extract the database fixture. The fixture requires {bytes_to_readable(fixture_size)} but only {bytes_to_readable(tmp_free)} is available in the temp directory. Please free up disk space or contact your IT team."

                        return JsonResponse(
                            {
                                "status_code": status_code,
                                "status_message": status_message,
                            },
                            status=status_code,
                        )

                    # Check media directory space (for the restored media)
                    has_media_space, media_free = check_disk_space(
                        media_size, media_dir
                    )

                    if not has_media_space:
                        status_code = 507
                        status_message = f"Not enough disk space to restore media files. The media requires {bytes_to_readable(media_size)} but only {bytes_to_readable(media_free)} is available. Please free up disk space or contact your IT team."
                        return JsonResponse(
                            {
                                "status_code": status_code,
                                "status_message": status_message,
                            },
                            status=status_code,
                        )

                    try:
                        zip.extract(fixture_name, tempdir)

                    except Exception as e:
                        status_code = 500
                        status_message = (
                            f"Unable to extract the fixture from the provided file. {e}"
                        )
                        return JsonResponse(
                            {
                                "status_code": status_code,
                                "status_message": status_message,
                            },
                            status=status_code,
                        )
                    try:
                        # Emptying DB tables
                        truncate_tables_cmds = getDBTruncateCommand()
                        with connection.cursor() as cursor:
                            for sql_command in truncate_tables_cmds:
                                cursor.execute(sql_command)
                    except Exception as e:
                        status_code = 500
                        status_message = f"Error while attempting to remove old database data. New data has NOT been imported. Significant data loss possible. Please check your import file and try again. {e}"
                        return JsonResponse(
                            {
                                "status_code": status_code,
                                "status_message": status_message,
                            },
                            status=status_code,
                        )

                    try:
                        # Loading in DB Fixture
                        fixture_file_path = os.path.join(tempdir, fixture_name)
                        with open(fixture_file_path) as source_fixture:
                            source_encoding = source_fixture.encoding
                        if not source_encoding.lower() == "utf-8":
                            with open(fixture_file_path, "rb") as source_fixture:
                                with open(
                                    os.path.join(tempdir, "UTF8_fixture.json"), "w+b"
                                ) as target_fixture:
                                    contents = source_fixture.read()
                                    target_fixture.write(
                                        contents.decode(source_encoding).encode("utf-8")
                                    )
                                    fixture_file_path = target_fixture.name

                        management.call_command("loaddata", fixture_file_path)
                        # Clear Django's in-memory ContentType cache so subsequent
                        # requests use the PKs from the newly imported data, not
                        # the stale pre-import values.  Without this, the
                        # ResumableAdminWidget renders the wrong content_type_id
                        # (e.g. the old Media PK now maps to LookupTechniques),
                        # causing FieldDoesNotExist on upload.
                        ContentType.objects.clear_cache()
                    except Exception as e:
                        status_code = 500
                        status_message = f"Error while loading in data from provided zipfile. Your old data has been removed. Please coordinate with IT to restore your database, and share this error message with them:\n {e}"
                        return JsonResponse(
                            {
                                "status_code": status_code,
                                "status_message": status_message,
                            },
                            status=status_code,
                        )

                    try:
                        # Copy media files directly from the zip into
                        # MEDIA_ROOT one at a time, instead of extracting
                        # everything to a temp dir first
                        for member in media_members:
                            # Strip the leading "media/" prefix to get
                            # the relative path inside MEDIA_ROOT
                            relative_path = member[len("media/") :]
                            if not relative_path:
                                continue
                            target_path = os.path.join(media_dir, relative_path)
                            os.makedirs(os.path.dirname(target_path), exist_ok=True)
                            with (
                                zip.open(member) as src,
                                open(target_path, "wb") as dst,
                            ):
                                shutil.copyfileobj(src, dst)

                    except Exception as e:
                        status_code = 500
                        status_message = f"Error while restoring your media files. Please work with IT to restore these, providing them your zipfile and this error message:\n {e}"
                        return JsonResponse(
                            {
                                "status_code": status_code,
                                "status_message": status_message,
                            },
                            status=status_code,
                        )
                    status_code = 200
                    status_message = "Database import completed successfully."
                else:
                    status_code = 400
                    status_message = "Uploaded file is not recognized as a zipfile. Be sure you have a valid backup file and try again."
        else:
            status_code = 400
            status_message = (
                "Request must have an attached zipfile to restore the database from."
            )

    return JsonResponse(
        {"status_code": status_code, "status_message": status_message},
        status=status_code,
    )


# Only Authenticated Users!
@permission_required("TEKDB.change_list")
def get_places_geojson(request):
    from .models import Places
    import json

    # Get all places
    places = Places.objects.exclude(geometry__isnull=True)
    # GeoJSON to store all places
    geojson = {"type": "FeatureCollection", "features": []}

    # Check for max results configuration
    try:
        config = Configuration.objects.all()[0]
        max_results = config.max_results_returned
    except Exception:
        from TEKDB.settings import DEFAULT_MAXIMUM_RESULTS

        max_results = DEFAULT_MAXIMUM_RESULTS
        pass

    too_many_results = len(places) > max_results
    if too_many_results:
        resultlist = places[:max_results]
    else:
        resultlist = places

    for result in resultlist:
        result_geometry = json.loads(result.geometry.geojson)
        result_indigenousplacename = (
            result.indigenousplacename if result.indigenousplacename else ""
        )
        result_englishplacename = (
            result.englishplacename if result.englishplacename else ""
        )
        result_placeid = result.placeid if result.placeid else ""
        result_feature = {
            "type": "Feature",
            "geometry": result_geometry,
            "properties": {
                "indigenousplacename": result_indigenousplacename,
                "englishplacename": result_englishplacename,
                "placeid": result_placeid,
            },
        }
        geojson["features"].append(result_feature)

    return geojson


class CitationAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower

        if not self.request.user.is_authenticated:
            return Citations.objects.none()
        qs = Citations.objects.all()

        if self.q:
            qs = Citations.keyword_search(self.q)

        return qs.order_by(
            Lower("referencetype__documenttype"),
            Lower("title"),
            Lower("intervieweeid__firstname"),
            Lower("intervieweeid__lastname"),
            "year",
        )


class MediaAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower

        if not self.request.user.is_authenticated:
            return Media.objects.none()
        qs = Media.objects.all()

        if self.q:
            qs = qs.filter(
                Q(medianame__icontains=self.q)
                | Q(mediatype__mediatype__icontains=self.q)
                | Q(mediatype__mediacategory__icontains=self.q)
            )

        return qs.order_by(Lower("medianame"), Lower("mediatype__mediatype"))


class PlaceAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower

        if not self.request.user.is_authenticated:
            return Places.objects.none()
        qs = Places.objects.all()

        if self.q:
            qs = Places.keyword_search(self.q)

        return qs.order_by(Lower("indigenousplacename"), Lower("englishplacename"))


class PlaceResourceAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower

        if not self.request.user.is_authenticated:
            return PlacesResourceEvents.objects.none()
        qs = PlacesResourceEvents.objects.all()

        if self.q:
            qs = qs.filter(
                Q(placeid__indigenousplacename__icontains=self.q)
                | Q(placeid__englishplacename__icontains=self.q)
                | Q(resourceid__commonname__icontains=self.q)
                | Q(resourceid__indigenousname__icontains=self.q)
                | Q(resourceid__genus__icontains=self.q)
                | Q(resourceid__species__icontains=self.q)
            )

        return qs.order_by(
            Lower("resourceid__commonname"), Lower("placeid__indigenousplacename")
        )


class ResourceAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Resources.objects.none()
        qs = Resources.objects.all()

        if self.q:
            qs = Resources.keyword_search(self.q)

        return qs


class ResourceActivityAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower

        if not self.request.user.is_authenticated:
            return ResourcesActivityEvents.objects.none()
        qs = ResourcesActivityEvents.objects.all()

        if self.q:
            qs = qs.filter(
                Q(placeresourceid__placeid__indigenousplacename__icontains=self.q)
                | Q(placeresourceid__placeid__englishplacename__icontains=self.q)
                | Q(placeresourceid__resourceid__commonname__icontains=self.q)
                | Q(placeresourceid__resourceid__indigenousname__icontains=self.q)
                | Q(placeresourceid__resourceid__genus__icontains=self.q)
                | Q(placeresourceid__resourceid__species__icontains=self.q)
                | Q(activityshortdescription__activity__icontains=self.q)
            )

        return qs.order_by(
            Lower("activityshortdescription__activity"),
            Lower("placeresourceid__placeid__indigenousplacename"),
            Lower("placeresourceid__resourceid__commonname"),
        )
