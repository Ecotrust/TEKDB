from base64 import b64encode

from django.conf import settings
from django.db import connection
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

#########################################################################
# Run with:
#       coverage run manage.py test explore -v 2
#########################################################################

class SearchTest(TestCase):
    fixtures = ['TEKDB/fixtures/all_dummy_data.json',]

    def setUp(self):
        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_multi_word_search(self):
        # Test that the query string submitted matches the query string returned to the client/user
        from explore.views import search
        from TEKDB.models import Users
        query_string = "A multi word search"
        request = self.factory.get(
            reverse('search'), 
            headers = {
                "Authorization": f"Basic {self.credentials}"
            }, 
            data = {
                'query': query_string,
            }
        )
        request.user = Users.objects.get(username='admin')
        # Assert that the search query string matches the query string submitted
        self.assertEqual(query_string, request.GET['query'])
