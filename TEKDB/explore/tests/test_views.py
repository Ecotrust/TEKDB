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
