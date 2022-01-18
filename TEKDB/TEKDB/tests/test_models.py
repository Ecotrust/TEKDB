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

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        cur = connection.cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')

    def test_placess(self):
        # print("Testing Places Model")
        # print("Total places: {}".format(Places.objects.all().count()))
        self.assertTrue(True)

    def test_places_search(self):
        #####################################
        ### TEST TEXT & CHAR FIELD SEARCH ###
        #####################################
        # search 'ame'
        # char fields:
        #   * englishplacename
        #   * indigenousplacename
        #   * indigenousplacenamemeaning
        #   * placealtindigenousname
        #   * Source
        #   * DigitizedBy
        keyword = 'place'
        place_results = Places.keyword_search(keyword)
        # do we get 3 results? also checks that we do not return all results in Place category
        self.assertEqual(place_results.count(), 3)
        # checkout results belong to one of the search fields
        for result in place_results:
            self.assertTrue(hasattr(result, 'rank'))
            self.assertTrue(hasattr(result, 'similarity'))
            self.assertTrue(
                (
                    result.similarity and
                    result.similarity > settings.MIN_SEARCH_SIMILARITY
                ) or
                result.rank > settings.MIN_SEARCH_RANK or
                keyword in result.indigenousplacename.lower() or 
                (
                    result.englishplacename and
                    keyword in result.englishplacename.lower()
                ) or (
                    result.planningunitid and
                    keyword in result.planningunitid.planningunitname.lower()
                ) or (
                    result.primaryhabitat and
                    keyword in result.primaryhabitat.habitat.lower()
                ) or (
                    result.tribeid and
                    keyword in result.tribeid.tribe.lower() or
                    keyword in result.tribeid.tribeunit.lower() or
                    keyword in result.tribeid.federaltribe.lower()
                )
            )
        
        #####################################
        ### TEST FOREIGN KEY FIELD SEARCH ###
        #####################################
        # Places model's foreign key field(s):
        #   * planningunitid
        #   * primaryhabitat
        #   * tribeid
        keyword = 'Northern'
        planning_unit_fk_search = Places.keyword_search(keyword)
        self.assertEqual(planning_unit_fk_search.count(), 8)
        self.assertTrue(25 in [x.pk for x in planning_unit_fk_search])
        
        keyword = 'Rocky Intertidal'
        habitat_fk_search = Places.keyword_search(keyword)
        self.assertEqual(habitat_fk_search.count(), 5)
        self.assertTrue(25 in [x.pk for x in habitat_fk_search])

        keyword = 'Tolowa'
        tribe_fk_search = Places.keyword_search(keyword)
        self.assertEqual(tribe_fk_search.count(), 15)
        self.assertTrue(25 in [x.pk for x in tribe_fk_search])

        #######################################
        ### TEST MODEL SET REFERENCE SEARCH ###
        #######################################
        # Test Alternative Place Name
        #   * PlacesResourceEvents
        keyword = 'flurpie'
        flurpie_results = Places.keyword_search(keyword)
        self.assertEqual(flurpie_results.count(), 1)
        self.assertEqual(flurpie_results[0].indigenousplacename, 'Test')

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

    def test_resources_search(self):
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
    fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        cur = connection.cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')

    def test_activity(self):
        print("Testing ResourcesActivityEvents Model")
        print("Total activities: {}".format(ResourcesActivityEvents.objects.all().count()))
        self.assertTrue(True)

    def test_activities_search(self):
        #####################################
        ### TEST TEXT & CHAR FIELD SEARCH ###
        #####################################
        # fields:
        
        keyword = 'men'
        activity_results = Citations.keyword_search(keyword) 
        self.assertEqual(activity_results.count(), 2)
        


# People


# Citations
class CitationsTest(TestCase):
    fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        cur = connection.cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')

    def test_citations(self):
        # print("Testing Places Model")
        # print("Total places: {}".format(Places.objects.all().count()))
        self.assertTrue(True)

    def test_citations_search(self):
        #####################################
        ### TEST TEXT & CHAR FIELD SEARCH ###
        #####################################
        # fields:
        #   * referencetext
        #   * authorprimary
        #   * authorsecondary
        #   * placeofinterview
        #   * seriestitle
        #   * seriesvolume
        #   * serieseditor
        #   * publisher
        #   * publishercity
        #   * preparedfor
        #   * referencetype (foreign key)
        #   * authortype (foreign key) (no records for testing)
        #   X intervieweeid (foreign key) (not ready for testing)
        #   X interviewerid (foreign key) (not ready for testing)

        keyword = 'traditional'
        cit_results = Citations.keyword_search(keyword) 
        self.assertEqual(cit_results.count(), 1)
        
        for result in cit_results:
            self.assertTrue(hasattr(result, 'rank'))
            self.assertTrue(hasattr(result, 'similarity'))
            self.assertTrue(
                (
                    result.similarity and
                    result.similarity > settings.MIN_SEARCH_SIMILARITY
                ) or (
                    result.rank and
                    result.rank > settings.MIN_SEARCH_RANK    
                ) or
                    keyword in result.referencetext.lower() 
                or (
                    result.authorprimary and
                    keyword in result.authorprimary.lower()
                ) or (
                    result.authorsecondary and
                    keyword in result.authorsecondary.lower()
                ) or (
                    result.placeofinterview and
                    keyword in result.placeofinterview.lower()
                ) or (
                    result.seriestitle and
                    keyword in result.seriestitle.lower()
                ) or (
                    result.seriesvolume and
                    keyword in result.seriesvolume.lower()
                ) or (
                    result.serieseditor and
                    keyword in result.serieseditor.lower()
                ) or (
                    result.publisher and
                    keyword in result.publisher.lower()
                ) or (
                    result.publishercity and
                    keyword in result.publishercity.lower()
                ) or (
                    result.preparedfor and
                    keyword in result.preparedfor.lower()
                ) or (
                    result.referencetype and
                    keyword in result.referencetype.documenttype.lower()
                ) or (
                    result.authortype and
                    keyword in result.authortype.authortype.lower()
                )
            )
        
        #####################################
        ### TEST FOREIGN KEY FIELD SEARCH ###
        #####################################
        # Citation model's foreign key field(s):
        keyword = 'book'
        reftype_results = Citations.keyword_search(keyword)
        self.assertEqual(reftype_results.count(), 1)
        self.assertTrue(11 in [x.pk for x in reftype_results])

        ## Future test for authortype
        # keyword = 'book'
        # authortype_results = Citations.keyword_search(keyword)
        # self.assertEqual(authortype_results.count(), 1)
        # self.assertTrue(11 in [x.pk for x in authortype_results])


        #######################################
        ### TEST MODEL SET REFERENCE SEARCH ###
        #######################################
        # 
        #   * 

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
