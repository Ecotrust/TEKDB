import contextlib
from dal import autocomplete
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test
from django.core import management
from django.core.management.commands import loaddata, dumpdata
from django.db import connection
from django.db.models import Q
from django.db.utils import OperationalError
from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import render
import io
import os
import shutil
from TEKDB.models import *
import tempfile
import zipfile

def get_related(request, model_name, id):
    from django.apps import apps
    import json
    if not (request.user.is_authenticated and request.user.has_perm('TEKDB.change_%s' % model_name.lower())):
        return HttpResponse('Unauthorized', status=401)
    data = json.dumps([])
    try:
        model = apps.get_model('TEKDB', model_name)
        instance = model.objects.get(pk=id)
        if hasattr(instance, 'get_related_objects'):
            data = json.dumps(instance.get_related_objects(id))
    except:
        pass
    return HttpResponse(data, content_type='application/json')

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

# Only Admins!
@user_passes_test(lambda u: u.is_superuser)
def ExportDatabase(request):
    datestamp = datetime.now().strftime('%Y%m%d')
    tmp_zip = tempfile.NamedTemporaryFile(delete=False, prefix="{}_backup_".format(datestamp), suffix='.zip')
    os.chdir(os.path.join(settings.MEDIA_ROOT, '..'))
    relative_media_directory = settings.MEDIA_ROOT.split(os.path.sep)[-1]
    media_paths = get_all_file_paths(relative_media_directory, cwd=os.getcwd())
    try:
        with tempfile.TemporaryDirectory() as tmp_dir:
            # create filename
            dumpfile = "{}_backup.json".format(datestamp)
            dumpfile_location = os.path.join(tmp_dir, dumpfile)
            with open(dumpfile_location, 'w') as of:
                management.call_command('dumpdata', '--indent=2', stdout=of)
            # zip up:
            #   * Data Dump file
            #   * Media files
            with zipfile.ZipFile(tmp_zip.name, 'w') as zip:
                zip.write(dumpfile_location, dumpfile)
                for media_file in media_paths:
                    zip.write(media_file)

        response = FileResponse(open(tmp_zip.name, 'rb'))
        return response
    finally:
        os.remove(tmp_zip.name)

    return HttpResponse()

def getDBTruncateCommand():
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        management.call_command('sqlflush')
    full_output = f.getvalue()
    cmd_list = full_output.split('\n')
    return [x for x in cmd_list if not x == '']


# Only Admins!
@user_passes_test(lambda u: u.is_superuser)
def ImportDatabase(request):
    if request.method == 'POST':
        if 'MEDIA_DIR' in request.POST.keys() and os.path.exists(request.POST['MEDIA_DIR']):
            media_dir = request.POST['MEDIA_DIR']
        else:
            media_dir = os.path.split(settings.MEDIA_ROOT)[-1]
        # Unzip file
        if 'import_file' in request.FILES.keys():
            with tempfile.TemporaryDirectory() as tempdir:
                # tempdir = tempfile.gettempdir()
                # import_file = request.FILES['import_file']
                tmp_zip_file = tempfile.NamedTemporaryFile(mode='wb+',delete=True, suffix='.zip')
                for chunk in request.FILES['import_file'].chunks():
                    tmp_zip_file.write(chunk)
                tmp_zip_file.seek(0)
                if zipfile.is_zipfile(tmp_zip_file.name):
                    zip = zipfile.ZipFile(tmp_zip_file.name, "r")
                    non_media = [x for x in zip.namelist() if 'media' not in x and '.json' in x]
                    # Validate Zip Contents
                    if not len(non_media) == 1 or len(zip.namelist()) < 2:
                        return HttpResponse(500, "Received malformed import file. Must be a zipfile contailing one JSON file and a directory named 'media'")
                    fixture_name = non_media[0]
                    try:
                        zip.extractall(tempdir)
                        # for mediafile in os.scandir(os.path.join(tempdir, 'media')):
                        #     shutil.move(os.path.join(tempdir, 'media', mediafile.name), media_dir)

                        # Emptying DB tables
                        truncate_tables_cmds = getDBTruncateCommand()
                        with connection.cursor() as cursor:
                            for sql_command in truncate_tables_cmds:
                                cursor.execute(sql_command)

                    except Exception as e:
                        return HttpResponse(500, e)

                    # Loading in DB Fixture
                    management.call_command('loaddata', os.path.join(tempdir, fixture_name))

                    # Copy media into MEDIA dir
                    shutil.copytree(os.path.join(tempdir, 'media'), media_dir)

    return HttpResponse()

class CitationAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return Citations.objects.none()
        qs = Citations.objects.all()

        if self.q:
            qs = Citations.keyword_search(self.q)

        return qs.order_by(Lower('referencetype__documenttype'), Lower('title'), Lower('intervieweeid__firstname'), Lower('intervieweeid__lastname'), 'year')

class MediaAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return Media.objects.none()
        qs = Media.objects.all()

        if self.q:
            qs = qs.filter(
                Q(medianame__icontains=self.q) |
                Q(mediatype__mediatype__icontains=self.q) |
                Q(mediatype__mediacategory__icontains=self.q)
            )

        return qs.order_by(Lower('medianame'), Lower('mediatype__mediatype'))

class PlaceAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return Places.objects.none()
        qs = Places.objects.all()

        if self.q:
            qs = Places.keyword_search(self.q)

        return qs.order_by(Lower('indigenousplacename'), Lower('englishplacename'))

class PlaceResourceAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return PlacesResourceEvents.objects.none()
        qs = PlacesResourceEvents.objects.all()

        if self.q:
            qs = qs.filter(
                Q(placeid__indigenousplacename__icontains=self.q) |
                Q(placeid__englishplacename__icontains=self.q) |
                Q(resourceid__commonname__icontains=self.q) |
                Q(resourceid__indigenousname__icontains=self.q) |
                Q(resourceid__genus__icontains=self.q) |
                Q(resourceid__species__icontains=self.q)
            )

        return qs.order_by(Lower('resourceid__commonname'), Lower('placeid__indigenousplacename'))

class ResourceAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return Resources.objects.none()
        qs = Resources.objects.all()

        if self.q:
            qs = Resources.keyword_search(self.q)

        return qs.order_by(Lower('commonname'))

class ResourceActivityAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        from django.db.models.functions import Lower
        if not self.request.user.is_authenticated:
            return ResourcesActivityEvents.objects.none()
        qs = ResourcesActivityEvents.objects.all()

        if self.q:
            qs = qs.filter(
                Q(placeresourceid__placeid__indigenousplacename__icontains=self.q) |
                Q(placeresourceid__placeid__englishplacename__icontains=self.q) |
                Q(placeresourceid__resourceid__commonname__icontains=self.q) |
                Q(placeresourceid__resourceid__indigenousname__icontains=self.q) |
                Q(placeresourceid__resourceid__genus__icontains=self.q) |
                Q(placeresourceid__resourceid__species__icontains=self.q) |
                Q(activityshortdescription__activity__icontains=self.q)
            )

        return qs.order_by(Lower('placeresourceid__resourceid__commonname'), Lower('placeresourceid__placeid__indigenousplacename'), Lower('activityshortdescription__activity'))
