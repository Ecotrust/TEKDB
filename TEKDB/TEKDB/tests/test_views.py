from datetime import datetime
from django.conf import settings
from django.db import connection
from django.test import TestCase
from django.test.client import RequestFactory
# from django.urls import reverse
# from django.utils import timezone
from os import listdir
from os.path import isfile, join
# from TEKDB.forms import *
from TEKDB.models import *
from zipfile import ZipFile

#########################################################################
# Run with:
#       coverage run manage.py test TEKDB -v 2
#########################################################################

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
        # Test that all media files were captured in the zip
        for mediafile in listdir(settings.MEDIA_ROOT):
            self.assertTrue("media/{}".format(mediafile) in zip.namelist())
        # import .zip
        # test for deleted media
        # test for added record
