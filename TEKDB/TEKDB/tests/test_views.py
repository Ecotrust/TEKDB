from datetime import datetime
from django.conf import settings
from django.db import connection
from django.test import TestCase
from django.test.client import RequestFactory
# from django.urls import reverse
# from django.utils import timezone
import hashlib
from os import listdir
from os.path import isfile, join
import shutil
# from TEKDB.forms import *
from TEKDB.models import *
import tempfile
from zipfile import ZipFile

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

class RelatedTest(TestCase):
    def test_related(self):
        from TEKDB.views import get_related
        print("TODO: Write TEKDB/test_views.RelatedTest")
        self.assertTrue(True)

class ExportTest(TestCase):
    fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    def setUp(self):
        self.factory = RequestFactory()

    def test_export(self):
        from TEKDB.views import export_database, import_database
        self.assertTrue(True)
        # add record
        print("TODO: Add record to TEKDB/test_views.ExportTest.test_export")
        print("TODO: Test non-admin user failure in TEKDB/test_views.ExportTest.test_export")
        datestamp = datetime.now().strftime('%Y%m%d')
        # dump data
        request = self.factory.get('/export_database')
        response = export_database(request)
        self.assertEqual(response.status_code, 200)
        # test for dump files
        #   * .zip
        zipname = join(settings.MEDIA_ROOT, "{}_backup.zip".format(datestamp))
        self.assertTrue(isfile(zipname))
        zip = ZipFile(zipname, "r")
        media_folder_name = path.split(settings.MEDIA_ROOT)[-1]
        zip.extract(media_folder_name, tempfile.gettempdir())
        # Test that all media files were captured in the zip
        for mediafile in listdir(settings.MEDIA_ROOT):
            source_file_location = join(settings.MEDIA_ROOT, mediafile)
            source_file_relative_name = join(media_folder_name, mediafile)
            temp_file_location = join(tempfile.gettempdir(), source_file_relative_name)
            self.assertTrue(source_file_relative_name in zip.namelist())
            self.assertTrue(isfile(temp_file_location))
            source_checksum = get_checksum(source_file_location, "md5")
            temp_checksum = get_checksum(temp_file_location, "md5")
            self.assertEqual(source_checksum, temp_checksum)
        zip.close()
        shutil.rmtree(join(tempfile.gettempdir(), media_folder_name))
        # import .zip
        # test for deleted media
        # test for added record
