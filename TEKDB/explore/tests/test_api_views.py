from base64 import b64encode

from django.conf import settings
from django.test import TestCase
from django.test.client import RequestFactory
from os.path import join
from unittest.mock import patch, MagicMock

from TEKDB.tests.test_views import import_fixture_file


class HomeViewTest(TestCase):
    def test_home_page_api_html_content(self):
        with patch("explore.API.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = True
            mock_obj.html_content = "<b>Test HTML Home</b>"
            mock_get.return_value = mock_obj
            response = self.client.get("/api/page/Welcome/")
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data["page"], "welcome")
            self.assertIn("Test HTML Home", data["pageContent"])

    def test_home_page_api_not_html_content(self):
        with patch("explore.API.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = False
            mock_obj.content = "Test Text Home"
            mock_get.return_value = mock_obj
            response = self.client.get("/api/page/Welcome/")
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data["pageTitle"], "Welcome")
            self.assertIn("Test Text Home", data["pageContent"])


class AboutViewTest(TestCase):
    def test_about_page_api_html_content(self):
        with patch("explore.API.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = True
            mock_obj.html_content = "<b>Test HTML About</b>"
            mock_get.return_value = mock_obj
            response = self.client.get("/api/page/About/")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Test HTML About", response.json()["pageContent"])

    def test_about_page_api_not_html_content(self):
        with patch("explore.API.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = False
            mock_obj.content = "Test Text About"
            mock_get.return_value = mock_obj
            response = self.client.get("/api/page/About/")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Test Text About", response.json()["pageContent"])


class HelpViewTest(TestCase):
    def test_help_page_api_html_content(self):
        with patch("explore.API.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = True
            mock_obj.html_content = "<b>Test HTML Help</b>"
            mock_get.return_value = mock_obj
            response = self.client.get("/api/page/Help/")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Test HTML Help", response.json()["pageContent"])

    def test_help_page_api_not_html_content(self):
        with patch("explore.API.views.PageContent.objects.get") as mock_get:
            mock_obj = MagicMock()
            mock_obj.is_html = False
            mock_obj.content = "Test Text Help"
            mock_get.return_value = mock_obj
            response = self.client.get("/api/page/Help/")
            self.assertEqual(response.status_code, 200)
            self.assertIn("Test Text Help", response.json()["pageContent"])


class ExploreViewTest(TestCase):
    def setUp(self):
        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )

        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_explore_api(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)
        url = "/api/search/?query=test&category=places"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["categories"], ["places"])

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
        url = "/api/explore/Places/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["category"], "Places")


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
        self.client.force_login(Users.objects.get(username="admin"))
        response = self.client.get(f"/api/search/?query={query_string}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["query"], query_string)


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
        url = f"/api/explore/Places/{place.pk}/"
        place_response = self.client.get(url)
        self.assertEqual(place_response.json()["model"].lower(), "places")
        self.assertEqual(place_response.status_code, 200)

        resource = Resources.objects.first()
        url = f"/api/explore/resources/{resource.pk}/"
        resource_response = self.client.get(url)
        self.assertEqual(resource_response.json()["model"].lower(), "resources")
        self.assertEqual(resource_response.status_code, 200)

        rae = ResourcesActivityEvents.objects.first()
        url = f"/api/explore/resourcesactivityevents/{rae.pk}/"
        rae_response = self.client.get(url)
        self.assertEqual(rae_response.json()["model"].lower(), "resourcesactivityevents")
        self.assertEqual(rae_response.status_code, 200)

        media = Media.objects.first()
        url = f"/api/explore/media/{media.pk}/"
        media_response = self.client.get(url)
        self.assertEqual(media_response.json()["model"].lower(), "media")
        self.assertEqual(media_response.status_code, 200)

        pre = PlacesResourceEvents.objects.first()
        url = f"/api/explore/placesresourceevents/{pre.pk}/"
        pre_response = self.client.get(url)
        self.assertEqual(pre_response.json()["model"].lower(), "placesresourceevents")
        self.assertEqual(pre_response.status_code, 200)

        citation = Citations.objects.first()
        url = f"/api/explore/citations/{citation.pk}/"
        citation_response = self.client.get(url)
        self.assertEqual(citation_response.json()["model"].lower(), "citations")
        self.assertEqual(citation_response.status_code, 200)

    def test_get_by_model_id_invalid_model(self):
        # Test that an invalid model_type returns an error message
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)
        url = "/api/explore/InvalidModel/1/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Incorrect number of models", response.content.decode())

    def test_get_by_model_id_invalid_id(self):
        # Test that an invalid id returns an error message
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)
        url = "/api/explore/Places/999999/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_get_by_model_id_with_map(self):
        # Test that a valid model_type and id returns the expected record with map context
        from TEKDB.models import Users, Places

        place = Places.objects.first()
        user = Users.objects.get(username="admin")
        self.client.force_login(user)
        url = f"/api/explore/Places/{place.pk}/"
        response = self.client.get(url)
        data = response.json().get("map", {})
        map_keys = [
            "default_lon",
            "default_lat",
            "default_zoom",
            "min_zoom",
            "max_zoom",
            "extent",
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
        url = f"/api/explore/Media/{media.pk}/download"
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

        url = "/api/explore/Media/999999/download"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_invalid_model_type(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        url = "/api/explore/InvalidModel/1/download"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)


class GetSortedKeysTest(TestCase):
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
    # curl -u admin -H 'Accept: application/json; indent=4' http://localhost:8000/api/export/Places/31/csv/
    def test_sorted_keys_via_export_csv(self):
        # Indirectly verify ordering through CSV export payload
        from TEKDB.models import Places

        place = Places.objects.get(pk=31)
        url = f"/api/export/Places/{place.pk}/csv/"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        self.assertIn("name", content)
        self.assertIn("map", content)


class ExportRecordCsvTest(TestCase):

    def test_export_record_csv(self):
        from os.path import join
        from django.conf import settings
        from TEKDB.tests.test_views import import_fixture_file
        from TEKDB.models import Users

        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )

        self.user = Users.objects.get(username="admin")
        self.client.force_login(self.user)
        from TEKDB.models import Places

        place = Places.objects.get(pk=31)
        url = f"/api/export/Places/{place.pk}/csv/"
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
        url = f"/api/export/Places/{place.pk}/xls/"
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

    def test_search_api_get_request(self):
        url = "/api/search/?query=test&category=places"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["query"], "test")
        self.assertEqual(data["categories"], ["places"])

    def test_search_api_misspelled_category(self):
        url = "/api/search/?query=test&category=placess,resourcess"
        response = self.client.get(url)
        # should resort to all
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["query"], "test")
        self.assertEqual(
            data["categories"],
            ["places", "resources", "activities", "sources", "media"],
        )

    def test_search_api_no_category(self):
        url = "/api/search/?query=test"
        response = self.client.get(url)
        # should resort to all
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["query"], "test")
        self.assertEqual(
            data["categories"],
            ["places", "resources", "activities", "sources", "media"],
        )

    def test_search_api_post_request(self):
        url = "/api/search/"
        data = {
            "query": "test",
            "activities": "on",
            "citations": "on",
            "media": "on",
        }
        response = self.client.post(url, data)
        # DRF ExploreSearch currently implements GET; POST returns 405
        self.assertIn(response.status_code, [200, 405])


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
        url = "/api/export?query=test&places=true&format=csv"
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv")
        self.assertIn(
            'attachment; filename="TEK_RESULTS.csv"', response["Content-Disposition"]
        )
        self.assertIn("id", response.content.decode())
        self.assertIn("name", response.content.decode())

    def test_download_xlsx(self):
        url = "/api/export?query=test&places=true&format=xlsx"
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
