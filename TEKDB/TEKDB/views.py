import contextlib
import logging
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
import psutil
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


logger = logging.getLogger(__name__)


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


def _format_bytes(num_bytes):
    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(num_bytes)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"
        value /= 1024


def _get_directory_size(path):
    total = 0
    for root, _dirs, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                total += os.path.getsize(filepath)
            except OSError:
                continue
    return total


def _log_storage_snapshot(stage, monitored_paths):
    disk_info = {}
    for label, path in monitored_paths.items():
        try:
            usage = shutil.disk_usage(path)
            disk_info[label] = {
                "path": path,
                "free": _format_bytes(usage.free),
                "used": _format_bytes(usage.used),
                "total": _format_bytes(usage.total),
            }
        except OSError:
            disk_info[label] = {"path": path, "error": "unavailable"}
    print(f"Storage snapshot [{stage}]: {disk_info}")


# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


# decorator function
def profile(func):
    def wrapper(*args, **kwargs):

        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print(
            f"{func.__name__}: consumed memory: {mem_before:,} -> {mem_after:,} (delta: {mem_after - mem_before:,})"
        )

        return result

    return wrapper


# Only Admins!
@user_passes_test(lambda u: u.is_superuser)
@profile
def ExportDatabase(request, test=False):
    datestamp = datetime.now().strftime("%Y%m%d")
    tmp_zip = tempfile.NamedTemporaryFile(
        delete=False, prefix="{}_backup_".format(datestamp), suffix=".zip"
    )
    _log_storage_snapshot(
        "export:start",
        {
            "temp": tempfile.gettempdir(),
            "media": settings.MEDIA_ROOT,
        },
    )
    os.chdir(os.path.join(settings.MEDIA_ROOT, ".."))
    relative_media_directory = settings.MEDIA_ROOT.split(os.path.sep)[-1]
    media_paths = get_all_file_paths(relative_media_directory, cwd=os.getcwd())
    media_size_bytes = _get_directory_size(settings.MEDIA_ROOT)
    print(
        f"Export source media footprint: files={len(media_paths)}, size={_format_bytes(media_size_bytes)}"
    )
    response = HttpResponse()
    try:
        with tempfile.TemporaryDirectory() as tmp_dir:
            # create filename
            dumpfile = "{}_backup.json".format(datestamp)
            dumpfile_location = os.path.join(tmp_dir, dumpfile)
            with open(dumpfile_location, "w") as of:
                excludes = getattr(settings, "EXPORT_DUMP_EXCLUDE", [])
                management.call_command(
                    "dumpdata",
                    exclude=excludes,
                    indent=2,
                    stdout=of,
                )
            dump_size_bytes = os.path.getsize(dumpfile_location)
            print(f"Export dumpdata size: {_format_bytes(dump_size_bytes)}")
            # zip up:
            #   * Data Dump file
            #   * Media files
            with zipfile.ZipFile(tmp_zip.name, "w") as zip:
                zip.write(dumpfile_location, dumpfile)
                for media_file in media_paths:
                    zip.write(media_file)

        archive_size_bytes = os.path.getsize(tmp_zip.name)
        print(f"Export archive size: {_format_bytes(archive_size_bytes)}")
        _log_storage_snapshot(
            "export:archive-created",
            {
                "temp": tempfile.gettempdir(),
                "media": settings.MEDIA_ROOT,
            },
        )

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
@profile
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
            _log_storage_snapshot(
                "import:start",
                {
                    "temp": tempfile.gettempdir(),
                    "media": media_dir,
                },
            )
            with tempfile.TemporaryDirectory() as tempdir:
                try:
                    tmp_zip_file = tempfile.NamedTemporaryFile(
                        mode="wb+", delete=True, suffix=".zip"
                    )
                    for chunk in request.FILES["import_file"].chunks():
                        tmp_zip_file.write(chunk)
                    tmp_zip_file.seek(0)
                    print(
                        f"Import uploaded archive size: {_format_bytes(tmp_zip_file.tell())}"
                    )

                except Exception as e:
                    status_code = 500
                    status_message = 'Unable to read the provided file. Be sure it is a zipped file containing a .json representing the database and a "media" directory containing any static files. {}'.format(
                        e
                    )
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
                    fixture_name = non_media[0]
                    try:
                        zip.extractall(tempdir)
                        extracted_size_bytes = _get_directory_size(tempdir)
                        print(
                            f"Import extracted payload size: {_format_bytes(extracted_size_bytes)}"
                        )
                        _log_storage_snapshot(
                            "import:after-extract",
                            {
                                "temp": tempfile.gettempdir(),
                                "media": media_dir,
                            },
                        )
                    except Exception as e:
                        status_code = 500
                        status_message = 'Unable to unzip the provided file. Be sure it is a zipped file containing a .json representing the database and a "media" directory containing any static files. {}'.format(
                            e
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
                        status_message = "Error while attempting to remove old database data. New data has NOT been imported. Significant data loss possible. Please check your import file and try again. {}".format(
                            e
                        )
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
                        status_message = "Error while loading in data from provided zipfile. Your old data has been removed. Please coordinate with IT to restore your database, and share this error message with them:\n {}".format(
                            e
                        )
                        return JsonResponse(
                            {
                                "status_code": status_code,
                                "status_message": status_message,
                            },
                            status=status_code,
                        )

                    try:
                        # Copy media into MEDIA dir
                        shutil.copytree(
                            os.path.join(tempdir, "media"),
                            media_dir,
                            dirs_exist_ok=True,
                        )
                        media_size_after_import = _get_directory_size(media_dir)
                        print(
                            f"Import media footprint after restore: {_format_bytes(media_size_after_import)}"
                        )
                        _log_storage_snapshot(
                            "import:complete",
                            {
                                "temp": tempfile.gettempdir(),
                                "media": media_dir,
                            },
                        )
                    except Exception as e:
                        status_code = 500
                        status_message = "Error while restoring your media files. Please work with IT to restore these, providing them your zipfile and this error message:\n {}".format(
                            e
                        )
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
