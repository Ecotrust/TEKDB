from base64 import b64encode

from django.test import TestCase
from django.test.client import RequestFactory
from TEKDB.models import (
    Places,
    Resources,
    ResourcesActivityEvents,
    Citations,
    Media,
    MediaBulkUpload,
    ResourceActivityMediaEvents,
    ResourceActivityCitationEvents,
    MediaCitationEvents,
    PlacesResourceMediaEvents,
    PlacesResourceCitationEvents,
    PlaceAltIndigenousName,
    PlacesMediaEvents,
    PlacesResourceEvents,
    ResourcesCitationEvents,
    PlacesCitationEvents,
    ResourceAltIndigenousName,
    ResourcesMediaEvents,
    ResourceResourceEvents,
    LookupActivity,
    LookupAuthorType,
    LookupCustomaryUse,
    LookupHabitat,
    LookupPlanningUnit,
    LookupReferenceType,
    LookupMediaType,
    LookupParticipants,
    LookupPartUsed,
    People,
    LookupResourceGroup,
    LookupSeason,
    LookupTechniques,
    LookupTiming,
    LookupTribe,
    LookupUserInfo,
    Locality,
    Users,
)

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
        MAX_ID = model.objects.all().order_by("-pk")[0].pk

        cur = connection.cursor()
        cur.execute("SELECT setval(%s, %s)", (SEQUENCE_NAME, MAX_ID - 1))
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

    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    @classmethod
    def setUpClass(self):
        """
        Set up the test case.
        """
        super().setUpClass()
        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )


class ITKSearchTest(ITKTestCase):
    """
    Base class for all ITK search tests.
    """

    @classmethod
    def setUpClass(self):
        """
        Set up the test case.
        """
        super().setUpClass()
        cur = connection.cursor()
        cur.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")


####################################################
#   Search Tests
####################################################


class MiscSearchTest(ITKSearchTest):
    def test_empty_string_search(self):
        """
        Test that an empty string search returns all objects
        """
        keyword = ""
        categories = ["places", "resources", "activities", "sources", "media"]

        from explore.views import get_model_by_type

        for category in categories:
            query_models = get_model_by_type(category)
            resultlist = []
            for model in query_models:
                # Find all results matching keyword in this model
                print(
                    "\n\ttest empty string search for {} equals count of {}.objects.count".format(
                        model.__name__, model.__name__
                    )
                )
                model_results = model.keyword_search(keyword)
                for result in model_results:
                    resultlist.append(result)

                self.assertTrue(len(resultlist) == model.objects.count())

    def test_all_search_results(self):
        """
        Test that a model_type of 'all' returns results from specific categories
        """
        categories = [
            "resources",
            "places",
            "citations",
            "media",
            "resourcesactivityevents",
        ]

        from explore.views import get_model_by_type

        query_models = get_model_by_type("all")
        lowercase_query_model_names = [model.__name__.lower() for model in query_models]

        for category in categories:
            self.assertIn(category, lowercase_query_model_names)

    def test_no_keyword_get_results(self):
        """
        Test that an empty string search returns all objects
        """
        keyword = None

        from explore.views import get_results

        search_results = get_results(
            keyword,
            categories=["resources"],
        )
        all_ranks = set([x["rank"] for x in search_results])
        all_similarities = set([x["similarity"] for x in search_results])
        all_headlines = set([x["headline"] for x in search_results])

        self.assertEqual(all_ranks, {0})
        self.assertEqual(all_similarities, {0})
        self.assertEqual(all_headlines, {None})

    def test_phrase_search(self):
        """
        Test that a phrase search returns all objects that contain the phrase
        """
        keyword = "salmon trout"

        from explore.views import get_results

        search_results = get_results(
            keyword,
            categories=["places", "resources", "activities", "sources", "media"],
        )
        # 24 is king salmon
        self.assertTrue(24 in [x["id"] for x in search_results])
        # 362 is cutthroat trout
        self.assertTrue(362 in [x["id"] for x in search_results])

    def test_resource_search(self):
        """
        Test that a phrase search returns all objects that contain the phrase
        """
        keyword = "flurpie"

        from explore.views import get_results

        search_results = get_results(
            keyword,
            categories=["resources"],
        )
        ids = [x["id"] for x in search_results]
        # 387 is test with altindigenousname 'flurpie'
        self.assertIn(387, ids)


class GetVerboseFieldNameTest(TestCase):
    def setUp(self):
        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )

        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_get_verbose_field_name_one_model_deep(self):
        from TEKDB.models import Resources
        from explore.views import get_verbose_field_name

        model = Resources
        field_name = "commonname"
        verbose_name = get_verbose_field_name(model, field_name)
        self.assertEqual(verbose_name, "Common Name")

    def test_get_verbose_field_name_two_deep(self):
        from TEKDB.models import Resources
        from explore.views import get_verbose_field_name

        model = Resources
        field_name = "resourcealtindigenousname__altindigenousname"
        verbose_name = get_verbose_field_name(model, field_name)
        self.assertEqual(verbose_name, "Alt Name")

    def test_get_verbose_field_name_three_models_deep(self):
        from TEKDB.models import ResourcesActivityEvents
        from explore.views import get_verbose_field_name

        model = ResourcesActivityEvents
        field_name = "placeresourceid__resourceid__commonname"
        verbose_name = get_verbose_field_name(model, field_name)
        self.assertEqual(verbose_name, "Common Name")

    def test_get_verbose_field_name_four_deep(self):
        from TEKDB.models import ResourcesActivityEvents
        from explore.views import get_verbose_field_name

        model = ResourcesActivityEvents
        field_name = (
            "placeresourceid__placeid__placealtindigenousname__altindigenousname"
        )
        verbose_name = get_verbose_field_name(model, field_name)
        self.assertEqual(verbose_name, "Alternate Name")


class GreatestSimilarityAttributeTest(TestCase):
    def setUp(self):
        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )

        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_get_greatest_similarity_attribute(self):
        from TEKDB.models import Resources
        from explore.views import get_greatest_similarity_attribute

        keyword = "chiton"
        model_results = Resources.keyword_search(keyword)

        pks = {}
        for result in model_results:
            if result.pk not in pks:
                pks[result.pk] = 1
            else:
                pks[result.pk] += 1
        for result in model_results:
            greatest_similarity_attribute = get_greatest_similarity_attribute(
                result, pks
            )
            self.assertIsNotNone(greatest_similarity_attribute)

    def test_get_greatest_similarity_attribute_no_matches(self):
        from TEKDB.models import Resources
        from explore.views import get_greatest_similarity_attribute

        keyword = "gisegiuesgeapgesijeh"  # nonsense keyword to ensure no matches
        model_results = Resources.keyword_search(keyword)

        pks = {}
        for result in model_results:
            if result.pk not in pks:
                pks[result.pk] = 1
            else:
                pks[result.pk] += 1
        for result in model_results:
            greatest_similarity_attribute = get_greatest_similarity_attribute(
                result, pks
            )
            self.assertIsNone(greatest_similarity_attribute)

    def test_get_greatest_similarity_attribute_multiple_matches(self):
        from TEKDB.models import Places
        from explore.views import get_greatest_similarity_attribute

        keyword = "test"  # common keyword with multiple matches
        model_results = Places.keyword_search(keyword)

        pks = {}
        for result in model_results:
            if result.pk in pks:
                pks[result.pk] += 1
            else:
                pks[result.pk] = 1

        similarity_attribute_per_pk = {}
        pks_before = pks.copy()
        for result in model_results:
            greatest_similarity_attribute = get_greatest_similarity_attribute(
                result, pks
            )
            if result.pk not in similarity_attribute_per_pk:
                similarity_attribute_per_pk[result.pk] = [greatest_similarity_attribute]
            else:
                similarity_attribute_per_pk[result.pk].append(
                    greatest_similarity_attribute
                )

        for pk, attributes in similarity_attribute_per_pk.items():
            # remove duplicates from attributes to ensure they are all different
            unique_attributes = set(attributes)
            self.assertEqual(len(unique_attributes), pks_before[pk])


# LookupTribe

####################################################
#   Record Tests
####################################################


class RecordTest(ITKTestCase):
    def test_get_related_objects(self):
        from TEKDB.models import Record

        related_objects = Record.get_related_objects(Record, 1)
        self.assertEqual(len(related_objects), 0)


# Places
class PlacesTest(ITKSearchTest):
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
        keyword = "place"
        place_results = Places.keyword_search(keyword)
        # do we get 3 results? also checks that we do not return all results in Place category
        self.assertEqual(place_results.count(), 3)
        # checkout results belong to one of the search fields
        for result in place_results:
            self.assertTrue(hasattr(result, "similarity"))
            self.assertTrue(
                (
                    result.similarity
                    and result.similarity > settings.MIN_SEARCH_SIMILARITY
                )
            )

    def test_search_foreign_key_field(self):
        #####################################
        ### TEST FOREIGN KEY FIELD SEARCH ###
        #####################################
        # Places model's foreign key field(s):
        #   * planningunitid
        #   * primaryhabitat
        #   * tribeid
        keyword = "Northern"
        planning_unit_fk_search = Places.keyword_search(keyword)
        self.assertEqual(planning_unit_fk_search.count(), 10)
        self.assertTrue(25 in [x.pk for x in planning_unit_fk_search])

        keyword = "Rocky Intertidal"
        habitat_fk_search = Places.keyword_search(keyword)
        self.assertEqual(habitat_fk_search.count(), 8)
        self.assertTrue(25 in [x.pk for x in habitat_fk_search])

        keyword = "Tolowa"
        tribe_fk_search = Places.keyword_search(keyword)
        self.assertEqual(tribe_fk_search.count(), 13)
        self.assertTrue(25 in [x.pk for x in tribe_fk_search])

    def test_search_model_set_reference(self):
        #######################################
        ### TEST MODEL SET REFERENCE SEARCH ###
        #######################################
        # Test Alternative Place Name
        #   * PlacesResourceEvents
        keyword = "flurpie"
        flurpie_results = Places.keyword_search(keyword)
        self.assertEqual(flurpie_results.count(), 3)
        self.assertEqual(flurpie_results[0].indigenousplacename, "Test")

    def test_place_id_collision(self):
        """
        Test that saving an activity can recover from an ID collision
        """
        insertion_object = {}
        collision_result = test_model_id_collision(Places, insertion_object, self)
        self.assertTrue(collision_result)

    def test_relationships(self):
        """
        Test that place relationships are correctly identified
        """
        place = Places.objects.get(pk=21)  # Place with all types of relationships
        relationships = place.relationships()
        self.assertEqual(len(relationships), 4)

    def test_link(self):
        """
        Test that place link is correctly generated
        """
        place = Places.objects.get(pk=21)
        link = place.link()
        self.assertEqual(link, "/explore/places/21/")

    def test_get_response_format_no_feature(self):
        """
        Test that get_response_format works when no feature is provided
        """
        place = Places.objects.get(pk=28)  # Place with no geometry
        response = place.get_response_format()
        self.assertIn("id", response)
        self.assertIn("feature", response)
        self.assertIsNone(response["feature"])


# Resources
class ResourcesTest(ITKSearchTest):
    def test_resources(self):
        # print("Testing Resources Model")
        # print("Total resources: {}".format(Resources.objects.all().count()))
        self.assertTrue(True)

    def test_search_text_field(self):
        ##############################
        ### TEST TEXT FIELD SEARCH ###
        ##############################
        # search 'chiton'
        # This particular search term is good as it should have hits on all char fields:
        #   * commonname
        #   * indigenousname
        #   * genus
        #   * species
        keyword = "chiton"
        chiton_results = Resources.keyword_search(keyword)
        # do we get 16 results?
        self.assertEqual(chiton_results.count(), 16)
        # is weighting appropriate? Chiton > Chiton, Gumboot > Sea Cucumber > Skunk Cabbage
        for result in chiton_results:
            self.assertTrue(hasattr(result, "similarity"))
            self.assertTrue(
                (
                    result.similarity
                    and result.similarity >= settings.MIN_SEARCH_SIMILARITY
                )
            )
        # Advanced search name, description ONLY (no genus/spceies): 2 results
        skunk_cabbage_id = 325
        sea_cucumber_id = 305
        chiton_id = 187
        fields = ["commonname", "indigenousname"]
        fk_fields = []
        advanced_results = Resources.keyword_search(keyword, fields, fk_fields)
        # sea cukes and skunk cabbage only have 'chiton' in their genus or species name. They should not be present.
        self.assertEqual(advanced_results.count(), 10)
        for resource in advanced_results:
            self.assertTrue(resource.pk not in [skunk_cabbage_id, sea_cucumber_id])
        fields = ["genus", "species"]
        advanced_results = Resources.keyword_search(keyword, fields, fk_fields)
        # 'chiton' only has chiton in it's commonname. It should not be present.
        self.assertEqual(advanced_results.count(), 7)
        for resource in advanced_results:
            # self.assertTrue(resource.pk in [gumboot_chiton_id, skunk_cabbage_id, sea_cucumber_id])
            self.assertTrue(resource.pk != chiton_id)

    def test_search_foreign_key_field(self):
        #####################################
        ### TEST FOREIGN KEY FIELD SEARCH ###
        #####################################
        # Test resourceclassificationgroup search
        # This keyword is good to test Resources model's only foreign key field:
        #   * resourceclassificationgroup
        keyword = "anadromous"
        anadromous_results = Resources.keyword_search(keyword)
        self.assertEqual(anadromous_results.count(), 16)
        self.assertTrue(347 in [x.pk for x in anadromous_results])

    def test_search_model_set_reference(self):
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

        keyword = "flurpie"
        flurpie_results = Resources.keyword_search(keyword)
        self.assertEqual(flurpie_results.count(), 2)
        self.assertEqual(flurpie_results[1].commonname, "Test")
        self.assertTrue(hasattr(flurpie_results[1], "match_commonname"))
        self.assertTrue(
            hasattr(
                flurpie_results[1], "match_resourcealtindigenousname__altindigenousname"
            )
        )

    def test_resource_id_collision(self):
        """
        Test that saving a resource can recover from an ID collision
        """
        insertion_object = {
            # 'resourceclassificationgroup': ResourceClassificationGroup.objects.all()[0],
        }
        collision_result = test_model_id_collision(Resources, insertion_object, self)
        self.assertTrue(collision_result)

    def test_subtitle(self):
        """
        Test that resource subtitle is correctly generated
        """
        resource = Resources.objects.get(pk=151)  # abalone, Black
        subtitle = resource.subtitle()
        self.assertEqual(subtitle, "cracherdoii")

    def test_relationships(self):
        """
        Test that resource relationships are correctly identified
        """
        ResourcesMediaEvents.objects.create(
            **{
                "resourceid": Resources.objects.get(pk=207),
                "mediaid": Media.objects.get(pk=6),
            }
        )
        resource = Resources.objects.get(
            pk=207
        )  # Resource with multiple types of relationships
        relationships = resource.relationships()

        self.assertEqual(len(relationships), 4)


# ResourcesActivityEvents ('Activities')
class ResourcesActivityEventsTest(ITKSearchTest):
    def test_activity(self):
        # print("Testing ResourcesActivityEvents Model")
        # print("Total activities: {}".format(ResourcesActivityEvents.objects.all().count()))
        self.assertTrue(True)

    def test_activities_search(self):
        #####################################
        ### TEST TEXT & CHAR FIELD SEARCH ###
        #####################################
        # fields:

        keyword = "men"
        activity_results = ResourcesActivityEvents.keyword_search(keyword)
        self.assertEqual(activity_results.count(), 2)

        for result in activity_results:
            self.assertTrue(hasattr(result, "similarity"))
            self.assertTrue(
                (
                    result.similarity
                    and result.similarity > settings.MIN_SEARCH_SIMILARITY
                )
            )

    def test_activity_id_collision(self):
        """
        Test that saving an activity can recover from an ID collision
        """
        insertion_object = {
            "placeresourceid": PlacesResourceEvents.objects.all()[0],
        }
        collision_result = test_model_id_collision(
            ResourcesActivityEvents, insertion_object, self
        )
        self.assertTrue(collision_result)

    def test_relationships(self):
        """
        Test that activity relationships are correctly returned
        """
        activity = ResourcesActivityEvents.objects.get(pk=31)
        ResourceActivityMediaEvents.objects.create(
            **{
                "pk": 2,
                "resourceactivityid": activity,
                "mediaid": Media.objects.all()[0],
            }
        )
        relationships = activity.relationships()

        self.assertEqual(len(relationships), 3)

    def test_data(self):
        """
        Test that activity data is correctly generated with all fields
        """
        activity = ResourcesActivityEvents.objects.create(
            **{
                "placeresourceid": PlacesResourceEvents.objects.all()[0],
                "relationshipdescription": "This is a test activity.",
                "partused": LookupPartUsed.objects.all()[0],
                "activityshortdescription": LookupActivity.objects.all()[0],
                "activitylongdescription": "This is a long description of the activity.",
                "participants": LookupParticipants.objects.all()[0],
                "technique": LookupTechniques.objects.all()[0],
                "gear": "Test gear",
                "customaryuse": "customary use",
                "timing": LookupTiming.objects.all()[0],
                "timingdescription": "This is a description of the timing.",
            }
        )
        activity.save()
        retrieved_activity = ResourcesActivityEvents.objects.get(pk=activity.pk)
        data = retrieved_activity.data()

        keys = [
            "place",
            "resource",
            "excerpt",
            "part used",
            "activity type",
            "full description",
            "participants",
            "technique",
            "gear",
            "customary use",
            "timing",
            "timing description",
        ]

        data_keys = [item["key"].lower() for item in data]
        for key in keys:
            self.assertIn(key, data_keys)


# Citations (Bibliographic 'Sources')
class CitationsTest(ITKSearchTest):
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

        keyword = "traditional"
        cit_results = Citations.keyword_search(keyword)
        self.assertEqual(cit_results.count(), 1)

        for result in cit_results:
            self.assertTrue(hasattr(result, "similarity"))
            self.assertTrue(
                (
                    result.similarity
                    and result.similarity > settings.MIN_SEARCH_SIMILARITY
                )
            )

        #####################################
        ### TEST FOREIGN KEY FIELD SEARCH ###
        #####################################
        # Citation model's foreign key field(s):
        keyword = "book"
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
            "referencetype": LookupReferenceType.objects.all()[0],
        }
        collision_result = test_model_id_collision(Citations, insertion_object, self)
        self.assertTrue(collision_result)

    def test_relationships(self):
        """
        Test that citation relationships are correctly identified
        """
        interviewee = People.objects.create(firstname="Test", lastname="Interviewee")
        interviewer = People.objects.create(firstname="Test", lastname="Interviewer")
        citation = Citations.objects.create(
            referencetext="Test Citation for Relationships",
            referencetype=LookupReferenceType.objects.get(
                pk=3
            ),  # interview documenttype
            intervieweeid=interviewee,
            interviewerid=interviewer,
        )

        # create one of each relationship type
        PlacesCitationEvents.objects.create(
            placeid=Places.objects.first(), citationid=citation
        )
        ResourcesCitationEvents.objects.create(
            resourceid=Resources.objects.first(), citationid=citation
        )
        MediaCitationEvents.objects.create(
            mediaid=Media.objects.first(), citationid=citation
        )
        ResourceActivityCitationEvents.objects.create(
            resourceactivityid=ResourcesActivityEvents.objects.first(),
            citationid=citation,
        )
        PlacesResourceCitationEvents.objects.create(
            placeresourceid=PlacesResourceEvents.objects.first(), citationid=citation
        )
        relationships = citation.relationships()
        self.assertEqual(len(relationships), 6)

    def test_title_text_interview(self):
        """
        Test that citation title_text is correctly generated for interview type
        """
        citation = Citations.objects.get(pk=12)  # Citation with interview referencetype
        title_text = citation.title_text
        self.assertEqual(title_text, "Jay Tosanic: interviewed by Manahe Herman")

    def test_title_text_non_interview(self):
        """
        Test that citation title_text is correctly generated
        """
        citation = Citations.objects.get(
            pk=11
        )  # Citation of non interview referencetype
        title_text = citation.title_text
        self.assertEqual(
            title_text, "Traditional Marine Harvesting of Native Americans"
        )

    def test_description_text(self):
        """
        Test that citation description_text is correctly generated
        """
        citation = Citations.objects.get(
            pk=11
        )  # Citation of non interview referencetype
        description_text = citation.description_text
        expected_description = "Text on marine flora and fauna"
        self.assertEqual(description_text, expected_description)


# Media
class MediaTest(ITKSearchTest):
    def test_media(self):
        # print("Testing Media Model")
        # print("Total media: {}".format(Media.objects.all().count()))
        self.assertTrue(True)

    def test_media_search(self):
        #####################################
        ### TEST TEXT & CHAR FIELD SEARCH ###
        #####################################
        # fields:

        keyword = "sample"
        media_results = Media.keyword_search(keyword)
        self.assertEqual(media_results.count(), 2)

        for result in media_results:
            self.assertTrue(hasattr(result, "similarity"))
            self.assertTrue(
                (
                    result.similarity
                    and result.similarity > settings.MIN_SEARCH_SIMILARITY
                )
            )

    def test_media_id_collision(self):
        """
        Test that saving a media can recover from an ID collision
        """
        insertion_object = {}
        collision_result = test_model_id_collision(Media, insertion_object, self)
        self.assertTrue(collision_result)


# MediaBulkUpload
class MediaBulkUploadTest(ITKSearchTest):
    def test_media_bulk_upload_id_collision(self):
        """
        Test that saving a bulk upload record can recover from an ID collision
        """
        insertion_object = {}
        if MediaBulkUpload.objects.all().count() == 0:
            MediaBulkUpload.objects.create(**{"pk": 7})
            self.assertTrue(MediaBulkUpload.objects.all().count() > 0)
        existing_bulk_record = MediaBulkUpload.objects.all()[0]
        self.assertTrue(existing_bulk_record.pk > 0)
        collision_result = test_model_id_collision(
            MediaBulkUpload, insertion_object, self
        )
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
            "resourceactivityid": ResourcesActivityEvents.objects.all()[1],
            "mediaid": Media.objects.all()[1],
        }
        if (
            ResourceActivityMediaEvents.objects.all().count() == 0
            or ResourceActivityMediaEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            ResourceActivityMediaEvents.objects.create(
                **{
                    "pk": 2,
                    "resourceactivityid": ResourcesActivityEvents.objects.all()[0],
                    "mediaid": Media.objects.all()[0],
                }
            )
        self.assertTrue(ResourceActivityMediaEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            ResourceActivityMediaEvents, insertion_object, self
        )
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
                if (
                    ResourceActivityCitationEvents.objects.filter(
                        resourceactivityid=activity, citationid=citation
                    ).count()
                    == 0
                ):
                    combo = {
                        "resourceactivityid": activity,
                        "citationid": citation,
                    }
                    if not new_combo_1:
                        new_combo_1 = combo
                    elif not new_combo_2:
                        new_combo_2 = combo
                    else:
                        break
            if new_combo_1 and new_combo_2:
                break
        self.assertTrue(new_combo_1 is not False)
        self.assertTrue(new_combo_2 is not False)
        self.assertTrue(new_combo_1 != new_combo_2)

        insertion_object = new_combo_2

        if (
            ResourceActivityCitationEvents.objects.all().count() == 0
            or ResourceActivityCitationEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            new_combo_1["pk"] = 2
            ResourceActivityCitationEvents.objects.create(**new_combo_1)
        self.assertTrue(ResourceActivityCitationEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            ResourceActivityCitationEvents, insertion_object, self
        )
        self.assertTrue(collision_result)


# MediaCitationEvents ('Media - Sources')
class MediaCitationEventsTest(ITKTestCase):
    def test_media_citation_relationship_id_collision(self):
        """
        Test that saving a media-citation relationship can recover from an ID collision
        """
        insertion_object = {
            "mediaid": Media.objects.all()[1],
            "citationid": Citations.objects.all()[1],
        }
        if (
            MediaCitationEvents.objects.all().count() == 0
            or MediaCitationEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            MediaCitationEvents.objects.create(
                **{
                    "pk": 2,
                    "mediaid": Media.objects.all()[0],
                    "citationid": Citations.objects.all()[0],
                }
            )
        self.assertTrue(MediaCitationEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            MediaCitationEvents, insertion_object, self
        )
        self.assertTrue(collision_result)


class MediaCitationEventsCascadeTest(ITKTestCase):
    def setUp(self):
        self.media = Media.objects.create(
            medianame="Cascade Media", mediadescription="Cascade Media Description"
        )
        self.citation = Citations.objects.create(
            referencetype=LookupReferenceType.objects.get(pk=1),
            referencetext="Cascade Citation",
        )
        self.event = MediaCitationEvents.objects.create(
            mediaid=self.media,
            citationid=self.citation,
            relationshipdescription="Cascade Relationship",
        )

    def test_cascade_delete_media(self):
        event_pks = list(
            MediaCitationEvents.objects.filter(mediaid=self.media).values_list(
                "pk", flat=True
            )
        )
        self.assertIn(self.event.pk, event_pks)
        total_before = MediaCitationEvents.objects.count()
        self.media.delete()
        for pk in event_pks:
            self.assertFalse(
                MediaCitationEvents.objects.filter(pk=pk).exists(),
                f"event {pk} should have been cascade‐deleted",
            )
        total_after = MediaCitationEvents.objects.count()
        self.assertEqual(total_before - total_after, len(event_pks))

    def test_cascade_delete_citation(self):
        event_pks = list(
            MediaCitationEvents.objects.filter(citationid=self.citation).values_list(
                "pk", flat=True
            )
        )
        self.assertIn(self.event.pk, event_pks)
        total_before = MediaCitationEvents.objects.count()
        self.citation.delete()
        for pk in event_pks:
            self.assertFalse(
                MediaCitationEvents.objects.filter(pk=pk).exists(),
                f"event {pk} should have been cascade‐deleted",
            )
        total_after = MediaCitationEvents.objects.count()
        self.assertEqual(total_before - total_after, len(event_pks))


# PlacesResourceMediaEvents ('Place-Resources - Media')
class PlacesResourceMediaEventsTest(ITKTestCase):
    def test_place_resource_media_relationship_id_collision(self):
        """
        Test that saving a place-resource-media relationship can recover from an ID collision
        """
        insertion_object = {
            "placeresourceid": PlacesResourceEvents.objects.all()[1],
            "mediaid": Media.objects.all()[1],
        }
        if (
            PlacesResourceMediaEvents.objects.all().count() == 0
            or PlacesResourceMediaEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            PlacesResourceMediaEvents.objects.create(
                **{
                    "pk": 2,
                    "placeresourceid": PlacesResourceEvents.objects.all()[0],
                    "mediaid": Media.objects.all()[0],
                }
            )
        self.assertTrue(PlacesResourceMediaEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            PlacesResourceMediaEvents, insertion_object, self
        )
        self.assertTrue(collision_result)


# PlacesResourceCitationEvents ('Place-Resources - Sources')
class PlacesResourceCitationEventsTest(ITKTestCase):
    def test_place_resource_citation_relationship_id_collision(self):
        """
        Test that saving a place-resource-citation relationship can recover from an ID collision
        """
        insertion_object = {
            "placeresourceid": PlacesResourceEvents.objects.all()[1],
            "citationid": Citations.objects.all()[1],
        }
        if (
            PlacesResourceCitationEvents.objects.all().count() == 0
            or PlacesResourceCitationEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            PlacesResourceCitationEvents.objects.create(
                **{
                    "pk": 2,
                    "placeresourceid": PlacesResourceEvents.objects.all()[0],
                    "citationid": Citations.objects.all()[0],
                }
            )
        self.assertTrue(PlacesResourceCitationEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            PlacesResourceCitationEvents, insertion_object, self
        )
        self.assertTrue(collision_result)


# PlaceAltIndigenousName ('Places - Alternative Name')
class PlaceAltIndigenousNameTest(ITKTestCase):
    def test_place_alt_indigenous_name_id_collision(self):
        """
        Test that saving a place-alt-indigenous-name relationship can recover from an ID collision
        """
        insertion_object = {
            "placeid": Places.objects.all()[0],
            "altindigenousname": "Sample Alt Name 1",
        }
        if (
            PlaceAltIndigenousName.objects.all().count() == 0
            or PlaceAltIndigenousName.objects.all().order_by("-pk")[0].pk < 2
        ):
            PlaceAltIndigenousName.objects.create(
                **{
                    "placeid": Places.objects.all()[0],
                    "altindigenousnameid": 2,
                    "altindigenousname": "Sample Alt Name 2",
                }
            )
        self.assertTrue(PlaceAltIndigenousName.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            PlaceAltIndigenousName, insertion_object, self
        )
        self.assertTrue(collision_result)


# PlacesMediaEvents ('Places - Media')
class PlacesMediaEventsTest(ITKTestCase):
    def test_place_media_relationship_id_collision(self):
        """
        Test that saving a place-media relationship can recover from an ID collision
        """
        insertion_object = {
            "placeid": Places.objects.all()[1],
            "mediaid": Media.objects.all()[1],
        }
        if (
            PlacesMediaEvents.objects.all().count() == 0
            or PlacesMediaEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            PlacesMediaEvents.objects.create(
                **{
                    "pk": 2,
                    "placeid": Places.objects.all()[0],
                    "mediaid": Media.objects.all()[0],
                }
            )
        self.assertTrue(PlacesMediaEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            PlacesMediaEvents, insertion_object, self
        )
        self.assertTrue(collision_result)

    def test_places_media_get_relationship_json(self):
        """
        Test that the response from get_relationship_json includes a file field with the media url
        """
        place = Places.objects.first()
        media = Media.objects.create(
            medianame="Test Media",
            mediadescription="Test Media Description",
            mediafile="test_media_file.jpg",
        )
        event = PlacesMediaEvents.objects.create(
            placeid=place,
            mediaid=media,
            relationshipdescription="Test Relationship",
        )
        relationship_json = event.get_relationship_json(Places)

        self.assertIn("file", relationship_json)
        self.assertDictEqual(relationship_json["file"], media.media())


class PlacesMediaEventsCascadeTest(ITKTestCase):
    def setUp(self):
        # Create a Places instance
        self.place = Places.objects.create(
            indigenousplacename="Test Place",
            englishplacename="Test Place English",
        )
        # Create a Media instance
        self.media = Media.objects.create(
            medianame="Test Media", mediadescription="Test Media Description"
        )

        # Create a PlacesMediaEvents instance
        self.places_media_event = PlacesMediaEvents.objects.create(
            placeid=self.place,
            mediaid=self.media,
            relationshipdescription="Test Relationship",
        )

    def test_cascade_delete_place(self):
        # grab the PKs of all events for our test place
        event_pks = list(
            PlacesMediaEvents.objects.filter(placeid=self.place).values_list(
                "pk", flat=True
            )
        )

        self.assertIn(self.places_media_event.pk, event_pks)

        # Get total
        total_before = PlacesMediaEvents.objects.count()

        # Delete the Places instance
        self.place.delete()

        # those specific events must be gone
        for pk in event_pks:
            self.assertFalse(
                PlacesMediaEvents.objects.filter(pk=pk).exists(),
                f"event {pk} should have been cascade‐deleted",
            )

        # and total should have dropped by exactly len(event_pks)
        total_after = PlacesMediaEvents.objects.count()
        self.assertEqual(total_before - total_after, len(event_pks))

    def test_cascade_delete_media(self):
        media_pks = list(
            PlacesMediaEvents.objects.filter(mediaid=self.media).values_list(
                "pk", flat=True
            )
        )

        self.assertIn(self.places_media_event.pk, media_pks)

        total_before = PlacesMediaEvents.objects.count()

        # Delete the Media instance
        self.media.delete()

        for pk in media_pks:
            self.assertFalse(
                PlacesMediaEvents.objects.filter(pk=pk).exists(),
                f"event {pk} should have been cascade‐deleted",
            )
        total_after = PlacesMediaEvents.objects.count()
        self.assertEqual(total_before - total_after, len(media_pks))


# PlacesResourceEvents ('Places - Resources')
class PlacesResourceEventsTest(ITKTestCase):
    def test_place_resource_relationship_id_collision(self):
        """
        Test that saving a place-resource relationship can recover from an ID collision
        """
        insertion_object = {
            "placeid": Places.objects.all()[1],
            "resourceid": Resources.objects.all()[1],
        }
        if (
            PlacesResourceEvents.objects.all().count() == 0
            or PlacesResourceEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            PlacesResourceEvents.objects.create(
                **{
                    "pk": 2,
                    "placeid": Places.objects.all()[0],
                    "resourceid": Resources.objects.all()[0],
                }
            )
        self.assertTrue(PlacesResourceEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            PlacesResourceEvents, insertion_object, self
        )
        self.assertTrue(collision_result)

    def test_places_resource_get_query_json_has_map(self):
        """
        Test that the response from get_query_json includes map data when map is True
        """
        place = Places.objects.get(pk=19)
        resource = Resources.objects.create(
            commonname="Test Resource", indigenousname="Test Resource Indigenous"
        )
        event = PlacesResourceEvents.objects.create(
            placeid=place,
            resourceid=resource,
            relationshipdescription="Test Relationship",
        )
        query_json = event.get_query_json()

        self.assertIn("map", query_json)

    def test_places_resource_get_query_json_no_map(self):
        """
        Test that the response from get_query_json includes no map data when map is False
        """
        place = Places.objects.create(
            indigenousplacename="Test Place",
            englishplacename="Test Place English",
        )
        resource = Resources.objects.create(
            commonname="Test Resource", indigenousname="Test Resource Indigenous"
        )
        event = PlacesResourceEvents.objects.create(
            placeid=place,
            resourceid=resource,
            relationshipdescription="Test Relationship",
        )
        query_json = event.get_query_json()

        self.assertNotIn("map", query_json)

    def test_keyword_search(self):
        """
        Test that keyword_search returns expected results
        """
        place = Places.objects.create(
            indigenousplacename="Keyword Place",
            englishplacename="Keyword Place English",
        )
        resource = Resources.objects.create(
            commonname="Keyword Resource", indigenousname="Keyword Indigenous Resource"
        )
        timing = LookupTiming.objects.create(timing="Seasonal")
        event = PlacesResourceEvents.objects.create(
            placeid=place,
            resourceid=resource,
            timing=timing,
        )
        keyword = "keyword"
        results = PlacesResourceEvents.keyword_search(keyword)
        self.assertIn(event, results)

    def test_relationships(self):
        place = Places.objects.get(pk=19)
        resource = Resources.objects.create(
            commonname="Test Resource", indigenousname="Test Resource Indigenous"
        )

        citation = Citations.objects.create(
            referencetype=LookupReferenceType.objects.get(pk=1),
            referencetext="Test Citation",
        )

        event = PlacesResourceEvents.objects.create(
            placeid=place,
            resourceid=resource,
            relationshipdescription="Test Relationship",
        )
        PlacesResourceCitationEvents.objects.create(
            placeresourceid=event,
            citationid=citation,
            relationshipdescription="Test Place-Resource-Citation Relationship",
        )
        ResourcesActivityEvents.objects.create(
            placeresourceid=event,
            relationshipdescription="Test Activity",
        )
        relationships = event.relationships()

        self.assertEqual(len(relationships), 4)


class PlacesResourceEventsCascadeTest(ITKTestCase):
    # fixtures = ['/usr/local/apps/TEKDB/TEKDB/TEKDB/fixtures/all_dummy_data.json',]

    def setUp(self):
        self.place = Places.objects.create(
            indigenousplacename="Cascade Place",
            englishplacename="Cascade Place English",
        )
        self.resource = Resources.objects.create(
            commonname="Cascade Resource", indigenousname="Cascade Indigenous Resource"
        )
        self.event = PlacesResourceEvents.objects.create(
            placeid=self.place,
            resourceid=self.resource,
            relationshipdescription="Cascade Relationship",
        )

    def test_cascade_delete_place(self):
        event_pks = list(
            PlacesResourceEvents.objects.filter(placeid=self.place).values_list(
                "pk", flat=True
            )
        )
        self.assertIn(self.event.pk, event_pks)
        total_before = PlacesResourceEvents.objects.count()
        self.place.delete()
        for pk in event_pks:
            self.assertFalse(
                PlacesResourceEvents.objects.filter(pk=pk).exists(),
                f"event {pk} should have been cascade‐deleted",
            )
        total_after = PlacesResourceEvents.objects.count()
        self.assertEqual(total_before - total_after, len(event_pks))

    def test_cascade_delete_resource(self):
        event_pks = list(
            PlacesResourceEvents.objects.filter(resourceid=self.resource).values_list(
                "pk", flat=True
            )
        )
        self.assertIn(self.event.pk, event_pks)
        total_before = PlacesResourceEvents.objects.count()
        self.resource.delete()
        for pk in event_pks:
            self.assertFalse(
                PlacesResourceEvents.objects.filter(pk=pk).exists(),
                f"event {pk} should have been cascade‐deleted",
            )
        total_after = PlacesResourceEvents.objects.count()
        self.assertEqual(total_before - total_after, len(event_pks))


# PlacesCitationEvents ('Places - Sources')
class PlacesCitationEventsTest(ITKTestCase):
    def test_place_citation_relationship_id_collision(self):
        """
        Test that saving a place-citation relationship can recover from an ID collision
        """
        insertion_object = {
            "placeid": Places.objects.all()[1],
            "citationid": Citations.objects.all()[1],
        }
        if (
            PlacesCitationEvents.objects.all().count() == 0
            or PlacesCitationEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            PlacesCitationEvents.objects.create(
                **{
                    "pk": 2,
                    "placeid": Places.objects.all()[0],
                    "citationid": Citations.objects.all()[0],
                }
            )
        self.assertTrue(PlacesCitationEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            PlacesCitationEvents, insertion_object, self
        )
        self.assertTrue(collision_result)

    def test_keyword_search(self):
        """
        Test that keyword_search returns expected results
        """
        place = Places.objects.create(
            indigenousplacename="Keyword Place",
            englishplacename="Keyword Place English",
        )
        citation = Citations.objects.create(
            referencetext="Keyword Citation",
            referencetype=LookupReferenceType.objects.create(documenttype="Book"),
        )
        event = PlacesCitationEvents.objects.create(
            placeid=place,
            citationid=citation,
            relationshipdescription="Keyword Relationship",
        )
        keyword = "keyword"
        results = PlacesCitationEvents.keyword_search(keyword)
        self.assertIn(event, results)

    def test_property_and_methods(self):
        """
        Test that description_text is correctly generated
        """
        place = Places.objects.create(
            indigenousplacename="Description Place",
            englishplacename="Description Place English",
        )
        citation = Citations.objects.create(
            referencetext="Description Citation",
            referencetype=LookupReferenceType.objects.create(documenttype="Book"),
        )
        relationship_description = "Description Relationship"
        event = PlacesCitationEvents.objects.create(
            placeid=place,
            citationid=citation,
            relationshipdescription=relationship_description,
        )
        description_text = event.description_text

        self.assertEqual(description_text, relationship_description)
        self.assertEqual(event.image(), settings.RECORD_ICONS["activity"])
        self.assertEqual(event.subtitle(), event.relationshipdescription)
        self.assertEqual(event.link(), f"/explore/placescitationevents/{event.pk}/")

    def test_relationships(self):
        place = Places.objects.create(
            indigenousplacename="Relationship Place",
            englishplacename="Relationship Place English",
        )
        citation = Citations.objects.create(
            referencetext="Relationship Citation",
            referencetype=LookupReferenceType.objects.create(documenttype="Book"),
        )
        event = PlacesCitationEvents.objects.create(
            placeid=place,
            citationid=citation,
            relationshipdescription="Relationship Description",
        )
        relationships = event.relationships()

        self.assertEqual(
            len(relationships), 2
        )  # should have place and citation relationships


class PlacesCitationEventsCascadeTest(ITKTestCase):
    def setUp(self):
        self.place = Places.objects.create(
            indigenousplacename="Cascade Place",
            englishplacename="Cascade Place English",
        )
        self.citation = Citations.objects.create(
            referencetext="Cascade Citation",
            referencetype=LookupReferenceType.objects.create(documenttype="Book"),
        )
        self.event = PlacesCitationEvents.objects.create(
            placeid=self.place,
            citationid=self.citation,
            relationshipdescription="Cascade Relationship",
        )

    def test_cascade_delete_place(self):
        event_pks = list(
            PlacesCitationEvents.objects.filter(placeid=self.place).values_list(
                "pk", flat=True
            )
        )
        self.assertIn(self.event.pk, event_pks)
        total_before = PlacesCitationEvents.objects.count()
        self.place.delete()
        for pk in event_pks:
            self.assertFalse(
                PlacesCitationEvents.objects.filter(pk=pk).exists(),
                f"event {pk} should have been cascade‐deleted",
            )
        total_after = PlacesCitationEvents.objects.count()
        self.assertEqual(total_before - total_after, len(event_pks))

    def test_cascade_delete_citation(self):
        event_pks = list(
            PlacesCitationEvents.objects.filter(citationid=self.citation).values_list(
                "pk", flat=True
            )
        )
        self.assertIn(self.event.pk, event_pks)
        total_before = PlacesCitationEvents.objects.count()
        self.citation.delete()
        for pk in event_pks:
            self.assertFalse(
                PlacesCitationEvents.objects.filter(pk=pk).exists(),
                f"event {pk} should have been cascade‐deleted",
            )
        total_after = PlacesCitationEvents.objects.count()
        self.assertEqual(total_before - total_after, len(event_pks))


# ResourceAltIndigenousName ('Resource Alternative Names')
class ResourceAltIndigenousNameTest(ITKTestCase):
    def test_resource_alt_indigenous_name_id_collision(self):
        """
        Test that saving a resource-alt-indigenous-name relationship can recover from an ID collision
        """
        insertion_object = {
            "resourceid": Resources.objects.all()[0],
            "altindigenousname": "Sample Alt Name 1",
        }
        if (
            ResourceAltIndigenousName.objects.all().count() == 0
            or ResourceAltIndigenousName.objects.all().order_by("-pk")[0].pk < 2
        ):
            ResourceAltIndigenousName.objects.create(
                **{
                    "resourceid": Resources.objects.all()[0],
                    "altindigenousnameid": 2,
                    "altindigenousname": "Sample Alt Name 2",
                }
            )
        self.assertTrue(ResourceAltIndigenousName.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            ResourceAltIndigenousName, insertion_object, self
        )
        self.assertTrue(collision_result)


# ResourcesMediaEvents ('Resources - Media')
class ResourcesMediaEventsTest(ITKTestCase):
    def test_resource_media_relationship_id_collision(self):
        """
        Test that saving a resource-media relationship can recover from an ID collision
        """
        insertion_object = {
            "resourceid": Resources.objects.all()[1],
            "mediaid": Media.objects.all()[1],
        }
        if (
            ResourcesMediaEvents.objects.all().count() == 0
            or ResourcesMediaEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            ResourcesMediaEvents.objects.create(
                **{
                    "pk": 2,
                    "resourceid": Resources.objects.all()[0],
                    "mediaid": Media.objects.all()[0],
                }
            )
        self.assertTrue(ResourcesMediaEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            ResourcesMediaEvents, insertion_object, self
        )
        self.assertTrue(collision_result)

    def test_resource_media_relationship_json(self):
        """
        Test that the response from get_relationship_json includes a file field with the media url
        """
        resource = Resources.objects.first()
        media = Media.objects.create(
            medianame="Test Media with File",
            mediadescription="Test Media Description",
            mediafile="test_media_file.png",
        )
        event = ResourcesMediaEvents.objects.create(
            resourceid=resource,
            mediaid=media,
            relationshipdescription="Test Relationship with File",
        )

        relationship_json = event.get_relationship_json(Resources)

        self.assertIn("file", relationship_json)
        self.assertDictEqual(relationship_json["file"], media.media())


# ResourceResourceEvents ('Resources - Resources')
class ResourceResourceEventsTest(ITKTestCase):
    def test_resource_resource_relationship_id_collision(self):
        """
        Test that saving a resource-resource relationship can recover from an ID collision
        """
        insertion_object = {
            "resourceid": Resources.objects.all()[1],
            "altresourceid": Resources.objects.all()[0],
        }
        if (
            ResourceResourceEvents.objects.all().count() == 0
            or ResourceResourceEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            ResourceResourceEvents.objects.create(
                **{
                    "pk": 2,
                    "resourceid": Resources.objects.all()[2],
                    "altresourceid": Resources.objects.all()[0],
                }
            )
        self.assertTrue(ResourceResourceEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            ResourceResourceEvents, insertion_object, self
        )
        self.assertTrue(collision_result)


# ResourcesCitationEvents ('Resources - Sources')
class ResourcesCitationEventsTest(ITKTestCase):
    def test_resource_citation_relationship_id_collision(self):
        """
        Test that saving a resource-citation relationship can recover from an ID collision
        """
        insertion_object = {
            "resourceid": Resources.objects.all()[1],
            "citationid": Citations.objects.all()[1],
        }
        if (
            ResourcesCitationEvents.objects.all().count() == 0
            or ResourcesCitationEvents.objects.all().order_by("-pk")[0].pk < 2
        ):
            ResourcesCitationEvents.objects.create(
                **{
                    "pk": 2,
                    "resourceid": Resources.objects.all()[0],
                    "citationid": Citations.objects.all()[0],
                }
            )
        self.assertTrue(ResourcesCitationEvents.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            ResourcesCitationEvents, insertion_object, self
        )
        self.assertTrue(collision_result)


# LocalityPlaceResourceEvent


####################################################
#   Lookup Tests
####################################################


# LookupActivity
class LookupActivityTest(ITKTestCase):
    def test_lookup_activity_id_collision(self):
        """
        Test that saving a lookup activity can recover from an ID collision
        """
        insertion_object = {
            "activity": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupActivity, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupAuthorType
class LookupAuthorTypeTest(ITKTestCase):
    def test_lookup_author_type_id_collision(self):
        """
        Test that saving a lookup author type can recover from an ID collision
        """
        insertion_object = {
            "authortype": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupAuthorType, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupCustomaryUse
class LookupCustomaryUseTest(ITKTestCase):
    def test_lookup_customary_use_id_collision(self):
        """
        Test that saving a lookup customary use can recover from an ID collision
        """
        insertion_object = {
            "usedfor": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupCustomaryUse, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupHabitat
class LookupHabitatTest(ITKTestCase):
    def test_lookup_habitat_id_collision(self):
        """
        Test that saving a lookup habitat can recover from an ID collision
        """
        insertion_object = {
            "habitat": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupHabitat, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupMediaType
class LookupMediaTypeTest(ITKTestCase):
    def test_lookup_media_type_search(self):
        #####################################
        ### TEST TEXT & CHAR FIELD SEARCH ###
        #####################################
        # search 'Aud'
        # char fields:
        #   * mediatype
        #   * mediacategory
        keyword = "Aud"
        search_results = LookupMediaType.keyword_search(keyword)
        # do we get 1 result? also checks that we do not return all results in Place category
        self.assertEqual(search_results.count(), 1)
        # checkout results belong to one of the search fields
        for result in search_results:
            if hasattr(result, "similarity"):
                self.assertTrue(
                    (
                        result.similarity
                        and result.similarity > settings.MIN_SEARCH_SIMILARITY
                    )
                )

    def test_lookup_media_type_id_collision(self):
        """
        Test that saving a lookup media type can recover from an ID collision
        """
        insertion_object = {
            "mediatype": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupMediaType, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupParticipants
class LookupParticipantsTest(ITKTestCase):
    def test_lookup_participants_id_collision(self):
        """
        Test that saving a lookup participants can recover from an ID collision
        """
        insertion_object = {
            "participants": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupParticipants, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupPartUsed
class LookupPartUsedTest(ITKTestCase):
    def test_lookup_part_used_id_collision(self):
        """
        Test that saving a lookup part used can recover from an ID collision
        """
        insertion_object = {
            "partused": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupPartUsed, insertion_object, self
        )
        self.assertTrue(collision_result)


# People
class PeopleTest(ITKSearchTest):
    def test_people_search(self):
        #####################################
        ### TEST TEXT & CHAR FIELD SEARCH ###
        #####################################
        # search 'Mana'
        # char fields:
        #   * firstname
        #   * lastname
        #   * village
        #   * relationshiptootherpeople
        keyword = "Mana"
        search_results = People.keyword_search(keyword)
        # do we get 1 result? also checks that we do not return all results in Place category
        self.assertEqual(search_results.count(), 1)
        # checkout results belong to one of the search fields
        for result in search_results:
            if hasattr(result, "similarity"):
                self.assertTrue(
                    (
                        result.similarity
                        and result.similarity > settings.MIN_SEARCH_SIMILARITY
                    )
                )

    def test_people_id_collision(self):
        """
        Test that saving a people can recover from an ID collision
        """
        insertion_object = {
            "firstname": "Testing",
            "lastname": "Person",
        }
        collision_result = test_model_id_collision(People, insertion_object, self)
        self.assertTrue(collision_result)

    def test_image(self):
        """
        Test that the image is from the settings
        """
        person = People.objects.create(
            firstname="Image",
            lastname="Tester",
        )
        image_data = person.image()

        self.assertEqual(settings.RECORD_ICONS["person"], image_data)

    def test_link(self):
        """
        Test that the link is correctly generated
        """
        person = People.objects.create(
            firstname="Link",
            lastname="Tester",
        )
        link = person.link()

        expected_link = f"/explore/people/{person.pk}"
        self.assertEqual(expected_link, link)

    def test_data(self):
        """
        Test that data method returns correct structure
        """
        person = People.objects.create(
            firstname="John",
            lastname="Doe",
            yearborn=1980,
            village="Sample Village",
            relationshiptootherpeople="Sample Relationship",
        )
        data = person.data()

        keys = [
            "first name",
            "last name",
            "year born",
            "village",
            "relationship to others",
        ]

        for item in data:
            key = item["key"]
            val = item["value"]
            self.assertIn(key, keys)
            if key == "first name":
                self.assertEqual(val, "John")
            elif key == "last name":
                self.assertEqual(val, "Doe")
            elif key == "year born":
                self.assertEqual(val, "1980")
            elif key == "village":
                self.assertEqual(val, "Sample Village")
            elif key == "relationship to others":
                self.assertEqual(val, "Sample Relationship")

    def test_relationships(self):
        """
        Test that relationships method returns correct sources
        """
        person = People.objects.create(
            firstname="John",
            lastname="Doe",
        )
        Citations.objects.create(
            referencetype=LookupReferenceType.objects.get(pk=1),
            referencetext="Interview Citation",
            intervieweeid=person,
        )
        Citations.objects.create(
            referencetype=LookupReferenceType.objects.get(pk=1),
            referencetext="Interviewer Citation",
            interviewerid=person,
        )

        relationships = person.relationships()
        self.assertEqual(len(relationships), 2)

    def test_get_query_json(self):
        """
        Test that get_query_json method returns correct structure
        """
        person = People.objects.create(
            firstname="John",
            lastname="Doe",
        )
        query_json = person.get_query_json()

        self.assertEqual(query_json["name"], "John Doe")
        self.assertEqual(query_json["link"], f"/explore/people/{person.pk}")
        self.assertEqual(query_json["image"], settings.RECORD_ICONS["person"])

    def test_get_record_dict(self):
        """
        Test that get_record_dict method returns correct structure
        """
        person = People.objects.create(
            firstname="John",
            lastname="Doe",
            village="Sample Village",
        )
        user = Users.objects.get(username="admin")
        record_dict = person.get_record_dict(user=user)

        self.assertEqual(record_dict["name"], "John Doe")
        self.assertEqual(record_dict["subtitle"], "Sample Village")
        self.assertFalse(record_dict["map"])


# LookupPlanningUnit
class LookupPlanningUnitTest(ITKTestCase):
    def test_planning_unit_id_collision(self):
        """
        Test that saving a planning unit can recover from an ID collision
        """
        insertion_object = {
            "planningunitname": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupPlanningUnit, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupReferenceType
class LookupReferenceTypeTest(ITKTestCase):
    def test_lokup_reference_type_id_collision(self):
        """
        Test that saving a reference type lookup can recover from an ID collision
        """
        insertion_object = {
            "documenttype": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupReferenceType, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupResourceGroup
class LookupResourceGroupTest(ITKTestCase):
    def test_lookup_resource_group_id_collision(self):
        """
        Test that saving a resource group lookup can recover from an ID collision
        """
        insertion_object = {
            "resourceclassificationgroup": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupResourceGroup, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupSeason
class LookupSeasonTest(ITKTestCase):
    def test_lookup_season_id_collision(self):
        """
        Test that saving a season lookup can recover from an ID collision
        """
        insertion_object = {
            "season": "Testing",
        }
        collision_result = test_model_id_collision(LookupSeason, insertion_object, self)
        self.assertTrue(collision_result)


# LookupTechniques
class LookupTechniquesTest(ITKTestCase):
    def test_lookup_technique_id_collision(self):
        """
        Test that saving a technique lookup can recover from an ID collision
        """
        insertion_object = {
            "techniques": "Testing",
        }
        collision_result = test_model_id_collision(
            LookupTechniques, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupTiming
class LookupTimingTest(ITKTestCase):
    def test_lookup_timing_id_collision(self):
        """
        Test that saving a timing lookup can recover from an ID collision
        """
        insertion_object = {
            "timing": "Testing",
        }
        collision_result = test_model_id_collision(LookupTiming, insertion_object, self)
        self.assertTrue(collision_result)


# LookupTribe
class LookupTribeTest(ITKTestCase):
    def test_people_search(self):
        #####################################
        ### TEST TEXT & CHAR FIELD SEARCH ###
        #####################################
        # search 'Rancheria'
        # char fields:
        #   * tribeunit
        #   * tribe
        #   * federaltribe
        keyword = "Rancheria"
        search_results = LookupTribe.keyword_search(keyword)
        # do we get 1 result? also checks that we do not return all results in Place category
        self.assertEqual(search_results.count(), 1)
        # checkout results belong to one of the search fields
        for result in search_results:
            if hasattr(result, "similarity"):
                self.assertTrue(
                    (
                        result.similarity
                        and result.similarity > settings.MIN_SEARCH_SIMILARITY
                    )
                )

    def test_lookup_tribe_id_collision(self):
        """
        Test that saving a tribe lookup can recover from an ID collision
        """
        insertion_object = {
            "tribeunit": "Subunit",
            "tribe": "Tribe",
            "federaltribe": "Government",
        }
        if (
            LookupTribe.objects.all().count() == 0
            or LookupTribe.objects.all().order_by("-pk")[0].pk < 2
        ):
            LookupTribe.objects.create(
                **{
                    "pk": 2,
                    "tribeunit": "Subunit1",
                    "tribe": "Tribe1",
                    "federaltribe": "Government1",
                }
            )
        self.assertTrue(LookupTribe.objects.all().count() > 0)
        collision_result = test_model_id_collision(LookupTribe, insertion_object, self)
        self.assertTrue(collision_result)


# LookupUserInfo
class LookupUserInfoTest(ITKTestCase):
    def test_lookup_user_inf_id_collision(self):
        """
        Test that saving a user info lookup can recover from an ID collision
        """
        insertion_object = {
            "username": "Name",
            "usertitle": "Title",
            "useraffiliation": "Affiliation",
        }
        if (
            LookupUserInfo.objects.all().count() == 0
            or LookupUserInfo.objects.all().order_by("-pk")[0].pk < 2
        ):
            LookupUserInfo.objects.create(
                **{
                    "pk": 2,
                    "username": "Name1",
                    "usertitle": "Title1",
                    "useraffiliation": "Affiliation1",
                }
            )
        self.assertTrue(LookupUserInfo.objects.all().count() > 0)
        collision_result = test_model_id_collision(
            LookupUserInfo, insertion_object, self
        )
        self.assertTrue(collision_result)


# LookupLocalityType


####################################################
#   Other Tests
####################################################

# Locality


class LocalityTest(ITKTestCase):
    def test_keyword_search(self):
        """
        Test that keyword_search returns expected results
        """
        place = Places.objects.create(
            indigenousplacename="Keyword Place",
            englishplacename="Keyword Place English",
        )
        locality = Locality.objects.create(
            englishname="Keyword Locality",
            placeid=place,
        )
        keyword = "keyword"
        results = Locality.keyword_search(keyword)
        self.assertIn(locality, results)

    def test_methods_properties(self):
        """
        Test that methods and properties return expected results
        """
        place = Places.objects.create(
            indigenousplacename="Place",
            englishplacename="Place English",
        )
        locality = Locality.objects.create(
            englishname="Locality",
            indigenousname="Indigenous Locality",
            placeid=place,
        )
        self.assertEqual(locality.image(), settings.RECORD_ICONS["place"])
        self.assertEqual(locality.subtitle(), locality.indigenousname)
        self.assertEqual(locality.link(), f"/explore/locality/{locality.pk}/")
