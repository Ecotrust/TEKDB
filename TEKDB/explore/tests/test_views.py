from base64 import b64encode

from django.conf import settings
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from os.path import join
from unittest.mock import patch, MagicMock

from TEKDB.tests.test_views import import_fixture_file

#########################################################################
# Run with:
#       coverage run manage.py test explore -v 2
#########################################################################


class HomeViewTest(TestCase):
    def test_home_view_html_content(self):
        with patch("explore.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = True
            mock_obj.html_content = "<b>Test HTML Home</b>"
            mock_get.return_value = mock_obj
            response = self.client.get("")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Test HTML Home", response.content.decode())

    def test_home_view_not_html_content(self):
        with patch("explore.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = False
            mock_obj.content = "Test Text Home"
            mock_get.return_value = mock_obj
            response = self.client.get("")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Test Text Home", response.content.decode())

    def test_home_view(self):
        url = ""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page"], "home")
        self.assertEqual(response.context["pageTitle"], "Welcome")
        self.assertEqual(
            response.context["pageContent"],
            "<h1>Welcome</h1><h3>Set Welcome Page Content In Admin</h3>",
        )


class AboutViewTest(TestCase):
    def test_about_view_html_content(self):
        with patch("explore.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = True
            mock_obj.html_content = "<b>Test HTML About</b>"
            mock_get.return_value = mock_obj
            response = self.client.get("/about/")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Test HTML About", response.content.decode())

    def test_about_view_not_html_content(self):
        with patch("explore.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = False
            mock_obj.content = "Test Text About"
            mock_get.return_value = mock_obj
            response = self.client.get("/about/")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Test Text About", response.content.decode())

    def test_about_view(self):
        url = "/about/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page"], "about")
        self.assertEqual(response.context["pageTitle"], "About")
        self.assertIn("Set About Page Content In Admin", response.content.decode())


class HelpViewTest(TestCase):
    def test_help_view_html_content(self):
        with patch("explore.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = True
            mock_obj.html_content = "<b>Test HTML Help</b>"
            mock_get.return_value = mock_obj
            response = self.client.get("/help/")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Test HTML Help", response.content.decode())

    def test_help_view_not_html_content(self):
        with patch("explore.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = False
            mock_obj.content = "Test Text Help"
            mock_get.return_value = mock_obj
            response = self.client.get("/help/")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Test Text Help", response.content.decode())

    def test_help_view(self):
        url = "/help/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page"], "help")
        self.assertEqual(response.context["pageTitle"], "Help")


class ExploreViewTest(TestCase):
    def setUp(self):
        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )

        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_explore_view(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)
        url = "/explore/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page"], "explore")
        self.assertEqual(response.context["pageTitle"], "Search")
        self.assertEqual(response.context["user"], user)


class GetByModelTypeTest(TestCase):
    def setUp(self):
        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )

        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_get_by_model_type(self):
        # Test that a valid model_type returns the expected records
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)
        url = "/explore/Places/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["category"], "Places")
        self.assertEqual(response.context["page"], "Results")
        self.assertEqual(response.context["pageTitle"], "Results")


class SearchTest(TestCase):
    # fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    def setUp(self):
        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )

        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_multi_word_search(self):
        # Test that the query string submitted matches the query string returned to the client/user
        from TEKDB.models import Users

        query_string = "A multi word search"
        request = self.factory.get(
            reverse("search"),
            headers={"Authorization": f"Basic {self.credentials}"},
            data={
                "query": query_string,
            },
        )
        request.user = Users.objects.get(username="admin")
        # Assert that the search query string matches the query string submitted
        self.assertEqual(query_string, request.GET["query"])


class GetByModelIdTest(TestCase):
    def setUp(self):
        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )

        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_get_by_model_id(self):
        # Test that a valid model_type and id returns the expected record
        from TEKDB.models import (
            Users,
            Places,
            Resources,
            Media,
            PlacesResourceEvents,
            Citations,
            ResourcesActivityEvents,
        )

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        place = Places.objects.first()
        url = f"/explore/Places/{place.pk}/"
        place_response = self.client.get(url)
        model_name = place_response.context[0]["model_name"]
        self.assertEqual(model_name, "Place")
        self.assertEqual(place_response.status_code, 200)

        resource = Resources.objects.first()
        url = f"/explore/resources/{resource.pk}/"
        resource_response = self.client.get(url)
        model_name = resource_response.context[0]["model_name"]
        self.assertEqual(model_name, "Resource")
        self.assertEqual(resource_response.status_code, 200)

        rae = ResourcesActivityEvents.objects.first()
        url = f"/explore/resourcesactivityevents/{rae.pk}/"
        rae_response = self.client.get(url)
        model_name = rae_response.context[0]["model_name"]
        self.assertEqual(model_name, "Activity")
        self.assertEqual(rae_response.status_code, 200)

        media = Media.objects.first()
        url = f"/explore/media/{media.pk}/"
        media_response = self.client.get(url)
        model_name = media_response.context[0]["model_name"]
        self.assertEqual(model_name, "Media")
        self.assertEqual(media_response.status_code, 200)

        pre = PlacesResourceEvents.objects.first()
        url = f"/explore/placesresourceevents/{pre.pk}/"
        pre_response = self.client.get(url)
        model_name = pre_response.context[0]["model_name"]
        self.assertEqual(model_name, "Place-Resource Event")
        self.assertEqual(pre_response.status_code, 200)

        citation = Citations.objects.first()
        url = f"/explore/citations/{citation.pk}/"
        citation_response = self.client.get(url)
        model_name = citation_response.context[0]["model_name"]
        self.assertEqual(model_name, "Bibliographic Source")
        self.assertEqual(citation_response.status_code, 200)

    def test_get_by_model_id_invalid_model(self):
        # Test that an invalid model_type returns an error message
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)
        url = "/explore/InvalidModel/1/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertIn("Incorrect number of models returned", response.content.decode())

    def test_get_by_model_id_invalid_id(self):
        # Test that an invalid id returns an error message
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)
        url = "/explore/Places/999999/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Error retrieving Places record with ID", response.content.decode()
        )

    def test_get_by_model_id_with_map(self):
        # Test that a valid model_type and id returns the expected record with map context
        from TEKDB.models import Users, Places

        place = Places.objects.first()
        user = Users.objects.get(username="admin")
        self.client.force_login(user)
        url = f"/explore/Places/{place.pk}/"
        response = self.client.get(url)
        data = response.context[0]
        map_keys = [
            "default_lon",
            "default_lat",
            "default_zoom",
            "min_zoom",
            "max_zoom",
            "map_extent",
        ]
        for key in map_keys:
            self.assertIn(key, data)


class DownloadMediaFileTest(TestCase):
    def setUp(self):
        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )

        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_download_media_file(self):
        from TEKDB.models import Users, Media

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        media = Media.objects.first()
        url = f"/explore/Media/{media.pk}/download"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Disposition"],
            f"attachment; filename={media.mediafile}",
        )
        self.assertEqual(response["Content-Type"], "application/force-download")

    def test_download_media_file_invalid_id(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        url = "/explore/Media/999999/download"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_invalid_model_type(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        url = "/explore/InvalidModel/1/download"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)


class GetSortedKeysTest(TestCase):
    def test_get_sorted_keys(self):
        from explore.views import get_sorted_keys

        keys = ["name", "link", "map"]
        sorted_keys = ["name", "map", "link"]
        self.assertEqual(sorted_keys, get_sorted_keys(keys))

    def test_get_sorted_keys_unique_key(self):
        from explore.views import get_sorted_keys

        keys = ["name", "link", "foo", "map", "bar"]
        # should append keys not in priority list to end
        sorted_keys = ["name", "map", "link", "foo", "bar"]
        self.assertEqual(sorted_keys, get_sorted_keys(keys))


class ExportRecordCsvTest(TestCase):
    def setUp(self):
        from os.path import join
        from django.conf import settings
        from TEKDB.tests.test_views import import_fixture_file

        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )
        from TEKDB.models import Users

        self.user = Users.objects.get(username="admin")
        self.client.force_login(self.user)

    def test_export_record_csv(self):
        from TEKDB.models import Places

        place = Places.objects.get(pk=31)
        url = f"/export/Places/{place.pk}/csv/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv")

        self.assertIn(
            f'attachment; filename="Places_{place.pk}_{str(place)}.csv"',
            response["Content-Disposition"],
        )
        self.assertIn("id", response.content.decode())
        self.assertIn("name", response.content.decode())


class ExportRecordXlsTest(TestCase):
    def setUp(self):
        from os.path import join
        from django.conf import settings
        from TEKDB.tests.test_views import import_fixture_file

        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )
        from TEKDB.models import Users

        self.user = Users.objects.get(username="admin")
        self.client.force_login(self.user)

    def test_export_record_xls(self):
        from TEKDB.models import Places

        place = Places.objects.get(pk=31)
        url = f"/export/Places/{place.pk}/xls/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Type"],
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

        self.assertIn(
            f'attachment; filename="Places_{place.pk}_{str(place)}.xlsx"',
            response["Content-Disposition"],
        )
        self.assertEqual(
            response.content[:2], b"PK"
        )  # XLSX files start with 'PK' (zip signature)


class SearchViewTest(TestCase):
    def setUp(self):
        from os.path import join
        from django.conf import settings
        from TEKDB.tests.test_views import import_fixture_file
        from TEKDB.models import Users

        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )
        self.user = Users.objects.get(username="admin")
        self.client.force_login(self.user)

    def test_search_view_get_request(self):
        url = "/search/?query=test&category=places"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page"], "Results")
        self.assertEqual(response.context["pageTitle"], "Results")
        self.assertEqual(response.context["query"], "test")
        self.assertEqual(response.context["keyword"], "test")
        self.assertEqual(response.context["categories"], '["places"]')
        self.assertIn(
            '<input type="checkbox" id="places" name="places" value="places" checked=true>',
            response.context["category_checkboxes"],
        )
        self.assertNotIn(
            '<input type="checkbox" id="resources" name="resources" value="resources" checked=true>',
            response.context["category_checkboxes"],
        )

    def test_search_view_misspelled_category(self):
        url = "/search/?query=test&category=placess,resourcess"
        response = self.client.get(url)
        # should resort to all
        self.assertEqual(response.status_code, 200)
        self.assertIn("test", response.context["query"])
        self.assertEqual(
            response.context["categories"],
            '["places", "resources", "activities", "sources", "media"]',
        )
        self.assertNotIn(
            '<input type="checkbox" id="places" name="places" value="places" checked=false>',
            response.context["category_checkboxes"],
        )

    def test_search_view_no_category(self):
        url = "/search/?query=test"
        response = self.client.get(url)
        # should resort to all
        self.assertEqual(response.status_code, 200)
        self.assertIn("test", response.context["query"])
        self.assertEqual(
            response.context["categories"],
            '["places", "resources", "activities", "sources", "media"]',
        )
        self.assertNotIn(
            '<input type="checkbox" id="places" name="places" value="places" checked=false>',
            response.context["category_checkboxes"],
        )

    def test_search_view_post_request(self):
        url = "/search/"
        data = {
            "query": "test",
            "activities": "on",
            "citations": "on",
            "media": "on",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page"], "Results")
        self.assertEqual(response.context["pageTitle"], "Results")
        self.assertIn("test", response.context["query"])
        self.assertEqual(
            response.context["categories"], '["activities", "sources", "media"]'
        )


class DownloadViewTest(TestCase):
    def setUp(self):
        from os.path import join
        from django.conf import settings
        from TEKDB.tests.test_views import import_fixture_file

        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )
        from TEKDB.models import Users

        self.user = Users.objects.get(username="admin")
        self.client.force_login(self.user)

    def test_download_csv(self):
        url = "/export?query=test&places=true&format=csv"
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv")
        self.assertIn(
            'attachment; filename="TEK_RESULTS.csv"', response["Content-Disposition"]
        )
        self.assertIn("id", response.content.decode())
        self.assertIn("name", response.content.decode())

    def test_download_xlsx(self):
        url = "/export?query=test&places=true&format=xlsx"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Type"],
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        self.assertIn(
            "attachment; filename=TEK_RESULTS.xlsx", response["Content-Disposition"]
        )
        self.assertEqual(
            response.content[:2], b"PK"
        )  # XLSX files start with 'PK' (zip signature)
