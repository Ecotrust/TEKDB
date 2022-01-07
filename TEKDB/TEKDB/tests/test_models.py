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
class PlacesTest(TestCase):
    fixtures = ['TEKDB/fixtures/all_dummy_data.json',]
    def test_resources(self):
        # print("Testing Places Model")
        # print("Total places: {}".format(Places.objects.all().count()))
        self.assertTrue(True)


# Resources
class ResourcesTest(TestCase):
    fixtures = ['TEKDB/fixtures/all_dummy_data.json',]


    @classmethod
    def setUpClass(self):
        super().setUpClass()
        cur = connection.cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')



    def test_resources(self):
        # print("Testing Resources Model")
        # print("Total resources: {}".format(Resources.objects.all().count()))
        self.assertTrue(True)

    def test_search(self):
        # search 'chiton'
        keyword = 'chiton'
        chiton_results = Resources.keyword_search(keyword)
        # do we get 4 results?
        self.assertEqual(chiton_results.count(), 4)
        # is weighting appropriate? Chiton > Chiton, Gumboot > Sea Cucumber > Skunk Cabbage
        for result in chiton_results:
            self.assertTrue(hasattr(result,'rank'))
            self.assertTrue(hasattr(result,'similarity'))
            self.assertTrue(
                (
                    result.similarity and
                    result.similarity > settings.MIN_SEARCH_SIMILARITY
                ) or
                result.rank > settings.MIN_SEARCH_RANK or
                keyword in result.commonname.lower() or
                (
                    result.indigenousname and
                    keyword in result.indigenousname.lower()
                ) or (
                    result.resourceclassificationgroup and
                    keyword in result.resourceclassificationgroup.resourceclassificationgroup.lower()
                ) or (
                    result.genus and
                    keyword in result.genus.lower()
                ) or (
                    result.species and
                    keyword in result.species.lower()
                )
            )
        # Advanced search name, description ONLY (no genus/spceies): 2 results

# PlacesResourceEvents


# ResourcesActivityEvents


# People


# Citations


# PlacesCitationEvents


# Locality


# LocalityPlaceResourceEvent


# LookupMediaType


# Media


# MediaCitationEvents


# PlacesMediaEvents


# PlacesResourceCitationEvents


# PlacesResourceMediaEvents


# ResourceActivityCitationEvents


# ResourceActivityMediaEvents


# ResourceResourceEvents


# ResourcesCitationEvents


# ResourcesMediaEvents
