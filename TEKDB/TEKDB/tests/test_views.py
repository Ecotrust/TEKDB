from base64 import b64encode
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import connection
from django.test import TestCase, TransactionTestCase
from django.test.client import RequestFactory
from django.urls import reverse
# from django.utils import timezone
import hashlib
from os import listdir, remove, sep
from os.path import isfile, join, split, getsize
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


class RelatedTest(TestCase):
    def test_related(self):
        from TEKDB.views import get_related
        print("\n\tTODO: Write TEKDB/test_views.RelatedTest")
        self.assertTrue(True)

class ExportTest(TestCase):
    fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    def setUp(self):
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
                self.assertTrue("/".join(split(source_file_relative_name)) in zip.namelist())
                self.assertTrue(isfile(temp_file_location))
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
    fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUp(cls):
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
                media_name = sep.join(filename.split(sep)[1:])
                self.assertTrue(media_name in listdir(self.tempmediadir.name))
        shutil.rmtree(self.tempmediadir.name)



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
