from base64 import b64encode
from datetime import datetime
from django.conf import settings
from django.db import connection
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
# from django.utils import timezone
import hashlib
from os import listdir, remove
from os.path import isfile, join, split
import shutil
# from TEKDB.forms import *
from TEKDB.models import *
from TEKDB.views import ExportDatabase, ImportDatabase
import tempfile
import zipfile
# from zipfile import ZipFile

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
        print("\n\tTODO: Write TEKDB/test_views.RelatedTest")
        self.assertTrue(True)

class ExportTest(TestCase):
    fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    def setUp(self):
        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_export(self):
        self.assertTrue(True)
        # add record
        print("\n\tTODO: Add record to TEKDB/test_views.ExportTest.test_export")
        print("\tTODO: Test non-admin user failure in TEKDB/test_views.ExportTest.test_export")
        datestamp = datetime.now().strftime('%Y%m%d')
        # dump data
        request = self.factory.get(
            reverse('export_database'),
            headers = {
                "Authorization": f"Basic {self.credentials}"
            },
        )

        request.user = Users.objects.get(username='admin')
        response = ExportDatabase(request)
        self.assertEqual(response.status_code, 200)

        tempdir = tempfile.gettempdir()
        zipname = join(tempdir, "{}_backup.zip".format(datestamp))
        fileresponse = bytes('test', 'utf-8')
        stream = b''.join(response.streaming_content)
        with open(zipname, "wb") as f:
            f.write(stream)
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
        for mediafile in listdir(settings.MEDIA_ROOT):
            source_file_location = join(settings.MEDIA_ROOT, mediafile)
            source_file_relative_name = join('media', mediafile)
            temp_file_location = join(tempdir, source_file_relative_name)
            self.assertTrue(source_file_relative_name in zip.namelist())
            self.assertTrue(isfile(temp_file_location))
            source_checksum = get_checksum(source_file_location, "md5")
            temp_checksum = get_checksum(temp_file_location, "md5")
            self.assertEqual(source_checksum, temp_checksum)
        zip.close()
        shutil.rmtree(join(tempdir, media_folder_name))
        dumpfile = join(tempdir, "{}_backup.json".format(datestamp))
        self.assertTrue(isfile(dumpfile))
        remove(dumpfile)
        
        # import .zip
        # test for deleted media
        # test for added record
