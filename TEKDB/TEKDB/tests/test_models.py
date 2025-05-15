from django.test import TestCase
from TEKDB.models import *
from django.utils import timezone
from django.urls import reverse
# from .forms import *
from django.conf import settings
from django.db import connection
from os.path import join
from TEKDB.tests.test_views import import_fixture_file

#########################################################################
# Run with:
#       coverage run manage.py test TEKDB -v 2 --keepdb
#########################################################################

###
#   MODELS W/ keyword_search
###

def test_model_id_collision(model, insertion_object, test):
    """
    Test that saving an object can recover from an ID collision
    """
    try:
        test.assertTrue(model.objects.all().count() > 0)
        DB_TABLE = model._meta.db_table
        PK_FIELD = model._meta.pk.name
        SEQUENCE_NAME = '{}_{}_seq'.format(DB_TABLE, PK_FIELD)
        ORIGINAL_COUNT = model.objects.all().count()
        MAX_ID = model.objects.all().order_by('-pk')[0].pk

        cur = connection.cursor()
        cur.execute('SELECT setval(%s, %s)', (SEQUENCE_NAME, MAX_ID - 1))
        new_obj = model.objects.create(**insertion_object)
        new_obj.save()
        test.assertTrue(new_obj.pk > MAX_ID)
        NEW_COUNT = model.objects.all().count()
        test.assertTrue(NEW_COUNT == ORIGINAL_COUNT + 1)
        new_obj.delete()
        FINAL_COUNT = model.objects.all().count()
        test.assertTrue(FINAL_COUNT == ORIGINAL_COUNT)
    except Exception as e:
        print("Error in test_model_id_collision: {}".format(e))
        return False
    return True

####################################################
#   Search Tests
####################################################



class MiscSearchTest(TestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUpClass(self):
        super().setUpClass()

        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))

        cur = connection.cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')

    def test_empty_string_search(self):
        """
        Test that an empty string search returns all objects
        """
        keyword = ''
        categories = ['places','resources','activities','sources','media']
        
        from explore.views import get_model_by_type

        for category in categories:
            query_models = get_model_by_type(category)
            resultlist = []
            for model in query_models:
                # Find all results matching keyword in this model
                print("\n\ttest empty string search for {} equals count of {}.objects.count".format(model.__name__, model.__name__))
                model_results = model.keyword_search(keyword)
                for result in model_results:
                    resultlist.append(result)

                self.assertTrue(len(resultlist) == model.objects.count())

    def test_phrase_search(self):
        """
        Test that a phrase search returns all objects that contain the phrase
        """
        keyword = "salmon trout"
        
        from explore.views import getResults
        
        search_results = getResults(keyword, categories=['places','resources','activities','sources','media'])
        # 24 is king salmon
        self.assertTrue(24 in [x['id'] for x in search_results])
        # 362 is cutthroat trout
        self.assertTrue(362 in [x['id'] for x in search_results])


# LookupTribe

####################################################
#   Record Tests
####################################################

# Places
class PlacesTest(TestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))
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
            self.assertTrue(hasattr(result, 'similarity'))
            self.assertTrue(
                (
                    result.similarity and
                    result.similarity > settings.MIN_SEARCH_SIMILARITY
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
        self.assertEqual(planning_unit_fk_search.count(), 10)
        self.assertTrue(25 in [x.pk for x in planning_unit_fk_search])

        keyword = 'Rocky Intertidal'
        habitat_fk_search = Places.keyword_search(keyword)
        self.assertEqual(habitat_fk_search.count(), 8)
        self.assertTrue(25 in [x.pk for x in habitat_fk_search])

        keyword = 'Tolowa'
        tribe_fk_search = Places.keyword_search(keyword)
        self.assertEqual(tribe_fk_search.count(), 13)
        self.assertTrue(25 in [x.pk for x in tribe_fk_search])

        #######################################
        ### TEST MODEL SET REFERENCE SEARCH ###
        #######################################
        # Test Alternative Place Name
        #   * PlacesResourceEvents
        keyword = 'flurpie'
        flurpie_results = Places.keyword_search(keyword)
        self.assertEqual(flurpie_results.count(), 3)
        self.assertEqual(flurpie_results[0].indigenousplacename, 'Test')

    def test_place_id_collision(self):
        """
        Test that saving an activity can recover from an ID collision
        """
        insertion_object = {
        }
        collision_result = test_model_id_collision(Places, insertion_object, self)
        self.assertTrue(collision_result)

# Resources
class ResourcesTest(TestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]


    @classmethod
    def setUpClass(self):
        super().setUpClass()
        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))
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
        # do we get 16 results?
        self.assertEqual(chiton_results.count(), 16)
        # is weighting appropriate? Chiton > Chiton, Gumboot > Sea Cucumber > Skunk Cabbage
        for result in chiton_results:
            self.assertTrue(hasattr(result,'similarity'))
            self.assertTrue(
                (
                    result.similarity and
                    result.similarity >= settings.MIN_SEARCH_SIMILARITY
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
        self.assertEqual(advanced_results.count(), 10)
        for resource in advanced_results:
            self.assertTrue(resource.pk not in [skunk_cabbage_id, sea_cucumber_id])
        fields = ['genus', 'species']
        advanced_results = Resources.keyword_search(keyword, fields, fk_fields)
        # 'chiton' only has chiton in it's commonname. It should not be present.
        self.assertEqual(advanced_results.count(), 7)
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
        self.assertEqual(anadromous_results.count(), 16)
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
        self.assertEqual(flurpie_results.count(), 2)
        self.assertEqual(flurpie_results[0].commonname, 'Test')


    def test_resource_id_collision(self):
        """
        Test that saving a resource can recover from an ID collision
        """
        insertion_object = {
            # 'resourceclassificationgroup': ResourceClassificationGroup.objects.all()[0],
        }
        collision_result = test_model_id_collision(Resources, insertion_object, self)
        self.assertTrue(collision_result)
# PlacesResourceEvents


# ResourcesActivityEvents ('Activities')
class ResourcesActivityEventsTest(TestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))
        cur = connection.cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')

    def test_activity(self):
        # print("Testing ResourcesActivityEvents Model")
        # print("Total activities: {}".format(ResourcesActivityEvents.objects.all().count()))
        self.assertTrue(True)

    def test_activities_search(self):
        #####################################
        ### TEST TEXT & CHAR FIELD SEARCH ###
        #####################################
        # fields:

        keyword = 'men'
        activity_results = ResourcesActivityEvents.keyword_search(keyword)
        self.assertEqual(activity_results.count(), 2)

        for result in activity_results:
            self.assertTrue(hasattr(result, 'similarity'))
            self.assertTrue(
                (
                    result.similarity and
                    result.similarity > settings.MIN_SEARCH_SIMILARITY
                )
            )

    def test_activity_id_collision(self):
        """
        Test that saving an activity can recover from an ID collision
        """
        insertion_object = {
            'placeresourceid': PlacesResourceEvents.objects.all()[0],
        }
        collision_result = test_model_id_collision(ResourcesActivityEvents, insertion_object, self)
        self.assertTrue(collision_result)


# Citations (Bibliographic 'Sources')
class CitationsTest(TestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))
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
            self.assertTrue(hasattr(result, 'similarity'))
            self.assertTrue(
                (
                    result.similarity and
                    result.similarity > settings.MIN_SEARCH_SIMILARITY
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

    def test_citation_id_collision(self):
        """
        Test that saving a citation can recover from an ID collision
        """
        insertion_object = {
            'referencetype': LookupReferenceType.objects.all()[0],
        }
        collision_result = test_model_id_collision(Citations, insertion_object, self)
        self.assertTrue(collision_result)


# Media
class MediaTest(TestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))
        cur = connection.cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')

    def test_media(self):
        # print("Testing Media Model")
        # print("Total media: {}".format(Media.objects.all().count()))
        self.assertTrue(True)

    def test_media_search(self):
        #####################################
        ### TEST TEXT & CHAR FIELD SEARCH ###
        #####################################
        # fields:

        keyword = 'sample'
        media_results = Media.keyword_search(keyword)
        self.assertEqual(media_results.count(), 2)

        for result in media_results:
            self.assertTrue(hasattr(result, 'similarity'))
            self.assertTrue(
                (
                    result.similarity and
                    result.similarity > settings.MIN_SEARCH_SIMILARITY
                )
            )

    def test_media_id_collision(self):
        """
        Test that saving a media can recover from an ID collision
        """
        insertion_object = {
        }
        collision_result = test_model_id_collision(Media, insertion_object, self)
        self.assertTrue(collision_result)




####################################################
#   Relationship Tests
####################################################
# PlacesCitationEvents

# LocalityPlaceResourceEvent

# MediaCitationEvents


# PlacesMediaEvents


# PlacesResourceCitationEvents


# PlacesResourceMediaEvents


# ResourceActivityCitationEvents


# ResourceActivityMediaEvents


# ResourceResourceEvents


# ResourcesCitationEvents


# ResourcesMediaEvents


####################################################
#   Lookup Tests
####################################################

# LookupMediaType

# People




####################################################
#   Other Tests
####################################################

# Locality




