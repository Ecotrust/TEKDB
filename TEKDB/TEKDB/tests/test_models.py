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
        SEQUENCE_NAME = '"{}_{}_seq"'.format(DB_TABLE, PK_FIELD)
        ORIGINAL_COUNT = model.objects.all().count()
        MAX_ID = model.objects.all().order_by('-pk')[0].pk

        cur = connection.cursor()
        cur.execute('SELECT setval(%s, %s)', (SEQUENCE_NAME, MAX_ID - 1))
        new_obj = model.objects.create(**insertion_object)
        new_obj.save()
        test.assertTrue(new_obj.pk > MAX_ID)
        NEW_COUNT = model.objects.all().count()
        test.assertTrue(NEW_COUNT > ORIGINAL_COUNT)
        new_obj.delete()
        FINAL_COUNT = model.objects.all().count()
        test.assertTrue(FINAL_COUNT == ORIGINAL_COUNT)
    except Exception as e:
        print("Error in test_model_id_collision: {}".format(e))
        return False
    return True


class ITKTestCase(TestCase):
    """
    Base class for all ITK tests.
    """

    @classmethod
    def setUpClass(self):
        """
        Set up the test case.
        """
        super().setUpClass()
        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))
        
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

# MediaBulkUpload
class MediaBulkUploadTest(TestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        import_fixture_file(join(settings.BASE_DIR, 'TEKDB', 'fixtures', 'all_dummy_data.json'))
        cur = connection.cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')

    def test_media_bulk_upload_id_collision(self):
        """
        Test that saving a bulk upload record can recover from an ID collision
        """
        insertion_object = {
        }
        if MediaBulkUpload.objects.all().count() == 0:
            MediaBulkUpload.objects.create(**{'pk':7})
            self.assertTrue(MediaBulkUpload.objects.all().count() > 0)
        existing_bulk_record = MediaBulkUpload.objects.all()[0]
        self.assertTrue(existing_bulk_record.pk > 0)
        collision_result = test_model_id_collision(MediaBulkUpload, insertion_object, self)
        self.assertTrue(collision_result)


####################################################
#   Relationship Tests
####################################################
# ResourceActivityMediaEvents ('Activity - Media')
class ResourceActivityMediaEventsTest(ITKTestCase):

    def test_activity_media_relationship_id_collision(self):
        """
        Test that saving an activity-media relationship can recover from an ID collision
        """
        insertion_object = { 
            'resourceactivityid': ResourcesActivityEvents.objects.all()[1],
            'mediaid': Media.objects.all()[1],
        }
        if ResourceActivityMediaEvents.objects.all().count() == 0 or ResourceActivityMediaEvents.objects.all().order_by('-pk')[0].pk < 2:
            ResourceActivityMediaEvents.objects.create(**{
                'pk':2,
                'resourceactivityid': ResourcesActivityEvents.objects.all()[0],
                'mediaid': Media.objects.all()[0],
            })
        self.assertTrue(ResourceActivityMediaEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(ResourceActivityMediaEvents, insertion_object, self)
        self.assertTrue(collision_result)

# ResourceActivityCitationEvents ('Activity - Sources')
class ResourceActivityCitationEventsTest(ITKTestCase):

    def test_activity_citation_relationship_id_collision(self):
        """
        Test that saving an activity-source relationship can recover from an ID collision
        """

        # Test was colliding with unique contstraint on resourceactivityid and citationid
        # so we need to create a new combo of activity and citation
        activities = ResourcesActivityEvents.objects.all()
        citations = Citations.objects.all()
        new_combo_1 = False
        new_combo_2 = False
        for activity in activities:
            for citation in citations:
                if ResourceActivityCitationEvents.objects.filter(
                    resourceactivityid=activity,
                    citationid=citation
                ).count() == 0:
                    combo = { 
                        'resourceactivityid': activity,
                        'citationid': citation,
                    }
                    if not new_combo_1:
                        new_combo_1 = combo
                    elif not new_combo_2:
                        new_combo_2 = combo
                    else:
                        break
            if new_combo_1 and new_combo_2:
                break
        self.assertTrue(new_combo_1 != False)
        self.assertTrue(new_combo_2 != False)
        self.assertTrue(new_combo_1 != new_combo_2)
                
        insertion_object = new_combo_2

        if ResourceActivityCitationEvents.objects.all().count() == 0 or ResourceActivityCitationEvents.objects.all().order_by('-pk')[0].pk < 2:
            new_combo_1['pk'] = 2
            ResourceActivityCitationEvents.objects.create(**new_combo_1)
        self.assertTrue(ResourceActivityCitationEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(ResourceActivityCitationEvents, insertion_object, self)
        self.assertTrue(collision_result)

# MediaCitationEvents ('Media - Sources')
class MediaCitationEventsTest(ITKTestCase):

    def test_media_citation_relationship_id_collision(self):
        """
        Test that saving a media-citation relationship can recover from an ID collision
        """
        insertion_object = { 
            'mediaid': Media.objects.all()[1],
            'citationid': Citations.objects.all()[1],
        }
        if MediaCitationEvents.objects.all().count() == 0 or MediaCitationEvents.objects.all().order_by('-pk')[0].pk < 2:
            MediaCitationEvents.objects.create(**{
                'pk':2,
                'mediaid': Media.objects.all()[0],
                'citationid': Citations.objects.all()[0],
            })
        self.assertTrue(MediaCitationEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(MediaCitationEvents, insertion_object, self)
        self.assertTrue(collision_result)

# PlacesResourceMediaEvents ('Place-Resources - Media')
class PlacesResourceMediaEventsTest(ITKTestCase):

    def test_place_resource_media_relationship_id_collision(self):
        """
        Test that saving a place-resource-media relationship can recover from an ID collision
        """
        insertion_object = { 
            'placeresourceid': PlacesResourceEvents.objects.all()[1],
            'mediaid': Media.objects.all()[1],
        }
        if PlacesResourceMediaEvents.objects.all().count() == 0 or PlacesResourceMediaEvents.objects.all().order_by('-pk')[0].pk < 2:
            PlacesResourceMediaEvents.objects.create(**{
                'pk':2,
                'placeresourceid': PlacesResourceEvents.objects.all()[0],
                'mediaid': Media.objects.all()[0],
            })
        self.assertTrue(PlacesResourceMediaEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(PlacesResourceMediaEvents, insertion_object, self)
        self.assertTrue(collision_result)

# PlacesResourceCitationEvents ('Place-Resources - Sources')
class PlacesResourceCitationEventsTest(ITKTestCase):

    def test_place_resource_citation_relationship_id_collision(self):
        """
        Test that saving a place-resource-citation relationship can recover from an ID collision
        """
        insertion_object = { 
            'placeresourceid': PlacesResourceEvents.objects.all()[1],
            'citationid': Citations.objects.all()[1],
        }
        if PlacesResourceCitationEvents.objects.all().count() == 0 or PlacesResourceCitationEvents.objects.all().order_by('-pk')[0].pk < 2:
            PlacesResourceCitationEvents.objects.create(**{
                'pk':2,
                'placeresourceid': PlacesResourceEvents.objects.all()[0],
                'citationid': Citations.objects.all()[0],
            })
        self.assertTrue(PlacesResourceCitationEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(PlacesResourceCitationEvents, insertion_object, self)
        self.assertTrue(collision_result)

# PlaceAltIndigenousName ('Places - Alternative Name')
class PlaceAltIndigenousNameTest(ITKTestCase):

    def test_place_alt_indigenous_name_id_collision(self):
        """
        Test that saving a place-alt-indigenous-name relationship can recover from an ID collision
        """
        insertion_object = { 
            'placeid': Places.objects.all()[0],
            'altindigenousname': "Sample Alt Name 1",
        }
        if PlaceAltIndigenousName.objects.all().count() == 0 or PlaceAltIndigenousName.objects.all().order_by('-pk')[0].pk < 2:
            PlaceAltIndigenousName.objects.create(**{
                'placeid': Places.objects.all()[0],
                'altindigenousnameid': 2,
                'altindigenousname': "Sample Alt Name 2",
            })
        self.assertTrue(PlaceAltIndigenousName.objects.all().count() > 0)
        collision_result = test_model_id_collision(PlaceAltIndigenousName, insertion_object, self)
        self.assertTrue(collision_result)

# PlacesMediaEvents ('Places - Media')
class PlacesMediaEventsTest(ITKTestCase):

    def test_place_media_relationship_id_collision(self):
        """
        Test that saving a place-media relationship can recover from an ID collision
        """
        insertion_object = { 
            'placeid': Places.objects.all()[1],
            'mediaid': Media.objects.all()[1],
        }
        if PlacesMediaEvents.objects.all().count() == 0 or PlacesMediaEvents.objects.all().order_by('-pk')[0].pk < 2:
            PlacesMediaEvents.objects.create(**{
                'pk':2,
                'placeid': Places.objects.all()[0],
                'mediaid': Media.objects.all()[0],
            })
        self.assertTrue(PlacesMediaEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(PlacesMediaEvents, insertion_object, self)
        self.assertTrue(collision_result)

# PlacesResourceEvents ('Places - Resources')
class PlacesResourceEventsTest(ITKTestCase):

    def test_place_resource_relationship_id_collision(self):
        """
        Test that saving a place-resource relationship can recover from an ID collision
        """
        insertion_object = { 
            'placeid': Places.objects.all()[1],
            'resourceid': Resources.objects.all()[1],
        }
        if PlacesResourceEvents.objects.all().count() == 0 or PlacesResourceEvents.objects.all().order_by('-pk')[0].pk < 2:
            PlacesResourceEvents.objects.create(**{
                'pk':2,
                'placeid': Places.objects.all()[0],
                'resourceid': Resources.objects.all()[0],
            })
        self.assertTrue(PlacesResourceEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(PlacesResourceEvents, insertion_object, self)
        self.assertTrue(collision_result)

# PlacesCitationEvents ('Places - Sources')
class PlacesCitationEventsTest(ITKTestCase):

    def test_place_citation_relationship_id_collision(self):
        """
        Test that saving a place-citation relationship can recover from an ID collision
        """
        insertion_object = { 
            'placeid': Places.objects.all()[1],
            'citationid': Citations.objects.all()[1],
        }
        if PlacesCitationEvents.objects.all().count() == 0 or PlacesCitationEvents.objects.all().order_by('-pk')[0].pk < 2:
            PlacesCitationEvents.objects.create(**{
                'pk':2,
                'placeid': Places.objects.all()[0],
                'citationid': Citations.objects.all()[0],
            })
        self.assertTrue(PlacesCitationEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(PlacesCitationEvents, insertion_object, self)
        self.assertTrue(collision_result)

# ResourceAltIndigenousName ('Resource Alternative Names')
class ResourceAltIndigenousNameTest(ITKTestCase):

    def test_resource_alt_indigenous_name_id_collision(self):
        """
        Test that saving a resource-alt-indigenous-name relationship can recover from an ID collision
        """
        insertion_object = { 
            'resourceid': Resources.objects.all()[0],
            'altindigenousname': "Sample Alt Name 1",
        }
        if ResourceAltIndigenousName.objects.all().count() == 0 or ResourceAltIndigenousName.objects.all().order_by('-pk')[0].pk < 2:
            ResourceAltIndigenousName.objects.create(**{
                'resourceid': Resources.objects.all()[0],
                'altindigenousnameid': 2,
                'altindigenousname': "Sample Alt Name 2",
            })
        self.assertTrue(ResourceAltIndigenousName.objects.all().count() > 0)
        collision_result = test_model_id_collision(ResourceAltIndigenousName, insertion_object, self)
        self.assertTrue(collision_result)

# ResourcesMediaEvents ('Resources - Media')
class ResourcesMediaEventsTest(ITKTestCase):

    def test_resource_media_relationship_id_collision(self):
        """
        Test that saving a resource-media relationship can recover from an ID collision
        """
        insertion_object = { 
            'resourceid': Resources.objects.all()[1],
            'mediaid': Media.objects.all()[1],
        }
        if ResourcesMediaEvents.objects.all().count() == 0 or ResourcesMediaEvents.objects.all().order_by('-pk')[0].pk < 2:
            ResourcesMediaEvents.objects.create(**{
                'pk':2,
                'resourceid': Resources.objects.all()[0],
                'mediaid': Media.objects.all()[0],
            })
        self.assertTrue(ResourcesMediaEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(ResourcesMediaEvents, insertion_object, self)
        self.assertTrue(collision_result)

# ResourceResourceEvents ('Resources - Resources')
class ResourceResourceEventsTest(ITKTestCase):

    def test_resource_resource_relationship_id_collision(self):
        """
        Test that saving a resource-resource relationship can recover from an ID collision
        """
        insertion_object = { 
            'resourceid': Resources.objects.all()[1],
            'altresourceid': Resources.objects.all()[0],
        }
        if ResourceResourceEvents.objects.all().count() == 0 or ResourceResourceEvents.objects.all().order_by('-pk')[0].pk < 2:
            ResourceResourceEvents.objects.create(**{
                'pk':2,
                'resourceid': Resources.objects.all()[2],
                'altresourceid': Resources.objects.all()[0],
            })
        self.assertTrue(ResourceResourceEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(ResourceResourceEvents, insertion_object, self)
        self.assertTrue(collision_result)

# ResourcesCitationEvents ('Resources - Sources')
class ResourcesCitationEventsTest(ITKTestCase):

    def test_resource_citation_relationship_id_collision(self):
        """
        Test that saving a resource-citation relationship can recover from an ID collision
        """
        insertion_object = { 
            'resourceid': Resources.objects.all()[1],
            'citationid': Citations.objects.all()[1],
        }
        if ResourcesCitationEvents.objects.all().count() == 0 or ResourcesCitationEvents.objects.all().order_by('-pk')[0].pk < 2:
            ResourcesCitationEvents.objects.create(**{
                'pk':2,
                'resourceid': Resources.objects.all()[0],
                'citationid': Citations.objects.all()[0],
            })
        self.assertTrue(ResourcesCitationEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(ResourcesCitationEvents, insertion_object, self)
        self.assertTrue(collision_result)

# LocalityPlaceResourceEvent



####################################################
#   Lookup Tests
####################################################

# LookupMediaType

# People




####################################################
#   Other Tests
####################################################

# Locality




