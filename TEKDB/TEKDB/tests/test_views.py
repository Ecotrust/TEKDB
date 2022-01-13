from django.test import TestCase
from TEKDB.models import *
from django.utils import timezone
from django.urls import reverse
# from .forms import *
from django.conf import settings
from django.db import connection

#########################################################################
# Run with:
#       coverage run manage.py test TEKDB -v 2 --keepdb
#########################################################################

###
#   MODELS W/ keyword_search
###

# LookupTribe


# Places
class ExportTest(TestCase):
    fixtures = ['TEKDB/fixtures/all_dummy_data.json',]
    def test_export(self):
        self.assertTrue(True)
        # add record
        # dump data
        # test for dump files
        #   * .zip
        # delete media
        # import .zip
        # test for deleted media
        # test for added record
