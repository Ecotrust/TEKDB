from base64 import b64encode
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.contrib.contenttypes.models import ContentType
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import connection
from django.test import TestCase, TransactionTestCase
from django.test.client import RequestFactory
from django.urls import reverse
# from django.utils import timezone
import hashlib
import json
from os import listdir, remove, sep
from os.path import isfile, isdir, join, split, getsize
import shutil
# from TEKDB.forms import *
from TEKDB.models import *
from TEKDB.views import ExportDatabase, ImportDatabase
import tempfile
import zipfile

#########################################################################
# Run with:
#       coverage run manage.py test TEKDB -v 2
#########################################################################

# Courtesy of DelftStack: https://www.delftstack.com/howto/python/python-checksum/#use-the-os-module-to-generate-and-check-the-checksum-of-an-md5-file-in-python
def get_checksum(filename, hash_function):
    hash_function = hash_function.lower()

    with open(filename, "rb") as f:
        bytes = f.read()
        if hash_function == "md5":
            readable_hash = hashlib.md5(bytes).hexdigest()

        else:
            Raise("{} is an invalid hash function. Please Enter MD5 value")

    return readable_hash

def create_export_request(self):
    return self.factory.get(
        reverse('export_database'),
        headers = {
            "Authorization": f"Basic {self.credentials}"
        },
    )

def get_export_file_from_response(response, tempdir=False, datestamp=False):
    if not tempdir:
        tempdir = tempfile.gettempdir()
    if not datestamp:
        datestamp = datetime.now().strftime('%Y%m%d')
    zipname = join(tempdir, "{}_backup.zip".format(datestamp))
    fileresponse = bytes('test', 'utf-8')
    stream = b''.join(response.streaming_content)
    with open(zipname, "wb") as f:
        f.write(stream)

    response.file_to_stream.close()
    remove(response.file_to_stream.name)

    return zipname

def get_content_type_map(import_cts):
    ct_map = {}
    model_map = {}
    for ct in import_cts:
        ct_map[ct['pk']] = {
            'import': {
                'model': ct['fields']['model'],
                'app_label': ct['fields']['app_label']
            }
        }
        model_map["{}__{}".format(ct['fields']['app_label'],ct['fields']['model'])] = ct['pk']

    for ct in ContentType.objects.all():
        key = "{}__{}".format(ct.app_label, ct.model)
        if key in model_map.keys():
            ct_map[model_map[key]]['existing_pk'] = ct.pk
    
    return ct_map

def get_perm_map(import_perms):
    from django.contrib.auth.models import Permission
    perm_map = {}
    for perm in import_perms:
        new_perm = Permission.objects.get(content_type_id=perm['fields']['content_type'], codename=perm['fields']['codename'])
        perm_map[perm['pk']] = {
            'import': {
                'codename': perm['fields']['codename'],
                'content_type': perm['fields']['content_type'],
                'name': perm['fields']['name']
            },
            'existing_pk': new_perm.pk
        }
        
    return perm_map

def update_json_content_types(json_dict):
    import_cts = []
    import_perms = []
    len_json_dict = len(json_dict)
    for record in json_dict:
        if record['model'] == 'contenttypes.contenttype':
            import_cts.append(record)
        if record['model'] == 'auth.permission':
            import_perms.append(record)
    for record in import_cts:
        json_dict.remove(record)
    for record in import_perms:
        json_dict.remove(record)
    
    ct_map = get_content_type_map(import_cts)

    for (index, record) in enumerate(import_perms):
        if 'fields' in import_perms[index].keys() and 'content_type' in import_perms[index]['fields'].keys():
            import_perms[index]['fields']['content_type'] = ct_map[record['fields']['content_type']]['existing_pk']

    perm_map = get_perm_map(import_perms)

    for (index, record) in enumerate(json_dict):
        if 'fields' in json_dict[index].keys():
            if 'content_type' in json_dict[index]['fields'].keys():
                json_dict[index]['fields']['content_type'] = ct_map[record['fields']['content_type']]['existing_pk']
            if 'permissions' in json_dict[index]['fields'].keys():
                for (perm_index, perm) in enumerate(json_dict[index]['fields']['permissions']):
                    if perm in perm_map.keys():
                        json_dict[index]['fields']['permissions'][perm_index] = perm_map[perm]['existing_pk']

    return json_dict

def import_fixture_file(filepath):
    # Even test databases seem to pre-populate themselves with permissions and content types
    #   * This is a problem when importing fixtures that have been exported from a database that has
    #     different content types and permissions and sets them explicitly. This function and its related
    #     functions attempt to fix this.
    from django.core.management import call_command
    from tempfile import NamedTemporaryFile
    with open(filepath) as json_in:
        json_dict = json.load(json_in)
    json_dict = update_json_content_types(json_dict)

    tempfile = NamedTemporaryFile(suffix='.json', delete=False)
    with open(tempfile.name, 'w') as json_out:
        json.dump(json_dict, json_out)
    call_command('loaddata', tempfile.name)
    remove(tempfile.name)


class RelatedTest(TestCase):
    def test_related(self):
        from TEKDB.views import get_related
        print("\n\tTODO: Write TEKDB/test_views.RelatedTest")
        self.assertTrue(True)

class ExportTest(TestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    def setUp(self):
        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))

        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")
        new_record = Resources.objects.create(commonname="Dummy Record 1")
        new_record.save()
        # Resources.moderated_object.fget(new_record).approve()

    def test_export(self):
        # dump data
        export_request = create_export_request(self)

        # Test non-admin user failure
        # Users w/out adequate permissions should be redirected (302)
        export_request.user = AnonymousUser()
        anon_response = ExportDatabase(export_request)
        self.assertEqual(anon_response.status_code, 302)

        export_request.user = Users.objects.get(username='readonly')
        bad_response = ExportDatabase(export_request)
        self.assertEqual(bad_response.status_code, 302)

        export_request.user = Users.objects.get(username='admin')
        response = ExportDatabase(export_request, test=True)
        self.assertEqual(response.status_code, 200)

        with tempfile.TemporaryDirectory() as tempdir:
            datestamp = datetime.now().strftime('%Y%m%d')
            zipname = get_export_file_from_response(response, tempdir, datestamp)

            # test for dump files
            #   * .zip
            self.assertTrue(isfile(zipname))
            self.assertTrue(zipfile.is_zipfile(zipname))
            zip = zipfile.ZipFile(zipname, "r")
            media_folder_name = split(settings.MEDIA_ROOT)[-1]
            try:
                zip.extractall(tempdir)
            except Exception as e:
                print(e)
                self.assertTrue(False)

            # Test that all media files were captured in the zip
            zip.close()
            for mediafile in listdir(settings.MEDIA_ROOT):
                source_file_location = join(settings.MEDIA_ROOT, mediafile)
                source_file_relative_name = join('media', mediafile)
                temp_file_location = join(tempdir, source_file_relative_name)
                # if a directory exists in media, then the folder name won't be the whole match
                if not isdir(source_file_relative_name):
                    self.assertTrue(source_file_relative_name in zip.namelist())
                    self.assertTrue(isfile(temp_file_location) or isdir(temp_file_location))
                    source_checksum = get_checksum(source_file_location, "md5")
                    temp_checksum = get_checksum(temp_file_location, "md5")
                    self.assertEqual(source_checksum, temp_checksum)
            shutil.rmtree(join(tempdir, media_folder_name))
            dumpfile = join(tempdir, "{}_backup.json".format(datestamp))
            self.assertTrue(isfile(dumpfile))

            new_record_found = False
            with open(dumpfile) as outfile:
                fixture_lines = outfile.readlines()
            for line in fixture_lines:
                if '"commonname": "Dummy Record 1"' in line:
                    new_record_found = True
                    break
            self.assertTrue(new_record_found)

class ImportTest(TransactionTestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUp(cls):
        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))

        cls.factory = RequestFactory()

        cls.credentials = b64encode(b"admin:admin").decode("ascii")
        cls.dummy_1_name = "Dummy Record 1"

        cls.old_resources_count = Resources.objects.all().count()
        new_record = Resources.objects.create(commonname=cls.dummy_1_name)
        new_record.save()
        # Resources.moderated_object.fget(new_record).approve()

        cls.zipname = join(settings.BASE_DIR, 'TEKDB', 'tests', 'test_files', 'exported_db.zip')
        cls.tempmediadir = tempfile.TemporaryDirectory()
        cls.import_request = cls.factory.post(
            reverse('import_database'),
            {
                'MEDIA_DIR': cls.tempmediadir.name,
                'content_type':'application/zip',
                'content_disposition':"attachment; filename=uploaded.dump"
            },
            headers = {
                "Authorization": f"Basic {cls.credentials}"
            },
        )
        with open(cls.zipname, 'rb') as z:
            import_file = InMemoryUploadedFile(
                z,
                'import_file',
                'exported_db.zip',
                'application/zip',
                getsize(cls.zipname),
                None
            )
            cls.import_request.FILES['import_file'] = import_file

            cls.import_request.user = Users.objects.get(username='admin')
            response = ImportDatabase(cls.import_request)

    def test_import(self):
        self.assertEqual(Resources.objects.all().count(), self.old_resources_count)
        self.assertEqual(Resources.objects.filter(commonname=self.dummy_1_name).count(), 0)
        # Test for media files in the temp dir
        zip = zipfile.ZipFile(self.zipname, "r")
        for filename in zip.namelist():
            if 'media' in filename and filename.index('media') == 0:
                # NOTE: zipfiles always use "/" as a separator.
                media_name = sep.join(filename.split("/")[1:])
                self.assertTrue(media_name in listdir(self.tempmediadir.name))
        shutil.rmtree(self.tempmediadir.name)


class PlaceMapTest(TestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUp(cls):
        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))

        cls.factory = RequestFactory()
        cls.credentials = b64encode(b"admin:admin").decode("ascii")
        cls.dummy_1_name = "Dummy Record 1"

        new_record = Places.objects.create(commonname="Dummy Record 1")
        new_record.save()

    def test_placeMap(self):
        request = self.factory.get(reverse('placeMap'))
        request.user = Users.objects.get(username='admin')
        response = placeMap(request)
        self.assertEqual(response.status_code, 200)


# class ExportImportTest(TestCase):
#     # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]
#
#     @classmethod
#     def setUpTestData(cls):
#         cls.factory = RequestFactory()
#         cls.credentials = b64encode(b"admin:admin").decode("ascii")
#
#         cls.dummy_1_name = "Dummy Record 1"
#         cls.dummy_2_name = "Dummy Record 2"
#
#         import ipdb; ipdb.set_trace()
#
#         new_record = Resources.objects.create(commonname=cls.dummy_1_name)
#         new_record.save()
#
#         # Count records
#         cls.original_media_count = Media.objects.all().count()
#         cls.original_places_count = Places.objects.all().count()
#         cls.original_resources_count = Resources.objects.all().count()
#         cls.original_citations_count = Citations.objects.all().count()
#         cls.original_activities_count = ResourcesActivityEvents.objects.all().count()
#
#         export_request = create_export_request(cls)
#         export_request.user = Users.objects.get(username='admin')
#         response = ExportDatabase(export_request)
#         cls.tempdir = tempfile.gettempdir()
#         zipname = get_export_file_from_response(response, cls.tempdir)
#
#         new_record2 = Resources.objects.create(commonname=cls.dummy_2_name)
#         new_record2.save()
#
#         cls.tempmediadir = tempfile.gettempdir()
#         cls.import_request = cls.factory.post(
#             reverse('import_database'),
#             {
#                 'MEDIA_DIR': cls.tempmediadir,
#             },
#             headers = {
#                 "Authorization": f"Basic {cls.credentials}"
#             },
#         )
#         #   Attach .zip to request
#         with open(zipname, 'rb') as z:
#             cls.import_request.FILES['import_file'] = z
#             cls.import_request.FILES['import_file'].read()
#             z.seek(0)
#
#         cls.import_request.user = Users.objects.get(username='admin')
#         response = ImportDatabase(cls.import_request)
#
#         remove(zipname)
#
#     def test_export_import(self):
#         ############################################################
#         ### IMPORT
#         ############################################################
#         tempdir = self.tempdir
#         # zipname = self.zipname
#
#         # Prep for test import:
#         #   Create temp dir to write media to
#
#         #   view must take optional MEDIA_DIR location
#         #   MAKE SURE TEST DOESN"T OVERRIDE LIVE DB!!!
#         self.assertEqual(Resources.objects.all().count(), self.original_resources_count )
#         self.assertEqual(Media.objects.all().count(), self.original_media_count)
#         self.assertEqual(Places.objects.all().count(), self.original_places_count)
#         self.assertEqual(Resources.objects.all().count(), self.original_resources_count)
#         self.assertEqual(Citations.objects.all().count(), self.original_citations_count)
#         self.assertEqual(ResourcesActivityEvents.objects.all().count(), self.original_activities_count)
#         # test for added record
#         dummy1_q = Resources.objects.filter(commonname=self.dummy_1_name)
#         dummy2_q = Resources.objects.filter(commonname=self.dummy_2_name)
#         self.assertEqual(dummy1_q.count(), 1)
#         self.assertEqual(dummy2_q.count(), 0)
#         self.assertEqual(dummy1_q[0].pk, first_resource.pk)
#         #
#         # import .zip
#         #   Create Request
#
#         self.import_request.user = AnonymousUser()
#         anon_response = ImportDatabase(self.import_request)
#         # Users w/out adequate permissions should be redirected (302)
#         self.assertEqual(anon_response.status_code, 302)
#         self.import_request.user = Users.objects.get(username='readonly')
#         bad_response = ImportDatabase(self.import_request)
#         self.assertEqual(bad_response.status_code, 302)
#
#         # self.assertEqual(response.status_code, 200)
#         #   Specify target MEDIA_DIR in request
