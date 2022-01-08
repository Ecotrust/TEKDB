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

    def test_places_search(self):
        ##############################
        ### TEST TEXT FIELD SEARCH ###
        ##############################
        # search 'ame'
        # char fields:
        #   * englishplacename
        #   * indigenousplacename
        #   * Source
        #   * DigitizedBy
        keyword = 'ame'
        ame_results = Places.keyword_search(keyword)
        # do we get 3 results?
        self.assertEqual(ame_results.count(), 3)

        for result in ame_results:
            self.assertTrue(hasattr(result, 'rank'))
        
        #####################################
        ### TEST FOREIGN KEY FIELD SEARCH ###
        #####################################
        # Places model's foreign key field(s):
        #   * planningunitid
        #   * primaryhabitat
        #   * tribeid

        #######################################
        ### TEST MODEL SET REFERENCE SEARCH ###
        #######################################
        # Test Alternative Resource Name
        # This search term only tests the one foreign model we have considered in the past:
        #   * ResourceAltIndigenousName
        # The current search neglects the following models that reference Resources... why?
        #   * PlacesResourceEvents
        #   * ResourceResourceEvents
        #   * ResourcesCitationEvents
        #   * ResourcesMediaEvents
        # These 4 are the 'in-between' tables for the other 4 core models. Perhaps not searching these is intentional?

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
        ##############################
        ### TEST TEXT FIELD SEARCH ###
        ##############################
        # search 'chiton'
        # This particular search term is good as it should have hits on all char fields:
        #   * commonname
        #   * indigenousname
        #   * genus
        #   * species
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
        skunk_cabbage_id = 325
        sea_cucumber_id = 305
        gumboot_chiton_id = 188
        chiton_id = 187
        fields = ['commonname', 'indigenousname']
        fk_fields = []
        advanced_results = Resources.keyword_search(keyword, fields, fk_fields)
        # sea cukes and skunk cabbage only have 'chiton' in their genus or species name. They should not be present.
        self.assertEqual(advanced_results.count(), 2)
        for resource in advanced_results:
            self.assertTrue(resource.pk not in [skunk_cabbage_id, sea_cucumber_id])
        fields = ['genus', 'species']
        advanced_results = Resources.keyword_search(keyword, fields, fk_fields)
        # 'chiton' only has chiton in it's commonname. It should not be present.
        self.assertEqual(advanced_results.count(), 3)
        for resource in advanced_results:
            # self.assertTrue(resource.pk in [gumboot_chiton_id, skunk_cabbage_id, sea_cucumber_id])
            self.assertTrue(resource.pk != chiton_id)

        #####################################
        ### TEST FOREIGN KEY FIELD SEARCH ###
        #####################################
        # Test resourceclassificationgroup search
        # This keyword is good to test Resources model's only foreign key field:
        #   * resourceclassificationgroup
        keyword = 'anadromous'
        anadromous_results = Resources.keyword_search(keyword)
        self.assertEqual(anadromous_results.count(), 2)
        self.assertTrue(347 in [x.pk for x in anadromous_results])

        #######################################
        ### TEST MODEL SET REFERENCE SEARCH ###
        #######################################
        # Test Alternative Resource Name
        # This search term only tests the one foreign model we have considered in the past:
        #   * ResourceAltIndigenousName
        # The current search neglects the following models that reference Resources... why?
        #   * PlacesResourceEvents
        #   * ResourceResourceEvents
        #   * ResourcesCitationEvents
        #   * ResourcesMediaEvents
        # These 4 are the 'in-between' tables for the other 4 core models. Perhaps not searching these is intentional?

        keyword = 'flurpie'
        flurpie_results = Resources.keyword_search(keyword)
        self.assertEqual(flurpie_results.count(), 1)
        self.assertEqual(flurpie_results[0].commonname, 'Test')

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
