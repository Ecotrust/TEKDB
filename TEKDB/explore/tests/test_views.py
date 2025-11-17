from base64 import b64encode

from django.conf import settings
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from os.path import join
from TEKDB.tests.test_views import import_fixture_file

#########################################################################
# Run with:
#       coverage run manage.py test explore -v 2
#########################################################################


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
        from TEKDB.models import Users, Places

        place = Places.objects.first()
        user = Users.objects.get(username="admin")
        self.client.force_login(user)
        url = f"/explore/Places/{place.pk}/"
        response = self.client.get(url)
        model_name = response.context[0]["model_name"]
        self.assertEqual(model_name, "Place")
        self.assertEqual(response.status_code, 200)

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
