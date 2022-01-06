from django.test import TestCase
from TEKDB.models import *
from django.utils import timezone
from django.urls import reverse
# from .forms import *
from django.conf import settings

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

    def test_resources(self):
        # print("Testing Resources Model")
        # print("Total resources: {}".format(Resources.objects.all().count()))
        self.assertTrue(True)

    def test_search(self):
        # search 'chiton'
        chiton_results = Resources.keyword_search('chiton')
        # do we get 4 results?
        self.assertEqual(chiton_results.count(), 4)
        # is weighting appropriate? Chiton > Chiton, Gumboot > Sea Cucumber > Skunk Cabbage
        for result in chiton_results:
            self.assertTrue(hasattr(result,'rank'))
            self.assertTrue(result.rank > settings.MIN_SEARCH_RANK)
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
