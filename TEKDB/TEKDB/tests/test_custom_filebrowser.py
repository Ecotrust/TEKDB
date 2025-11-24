from base64 import b64encode
from os.path import join
from django.conf import settings
from django.test import TestCase, RequestFactory
from django.urls import reverse
from unittest.mock import patch, Mock

from TEKDB import tekdb_filebrowser
from TEKDB.tests.test_views import import_fixture_file


class MockFileObject:
    def __init__(self, val):
        # val can be bool or callable returning bool
        self._val = val

    def has_media_record(self):
        if callable(self._val):
            return self._val()
        return self._val


class CustomFileBrowserTests(TestCase):
    def setUp(self):
        import_fixture_file(
            join(settings.BASE_DIR, "TEKDB", "fixtures", "all_dummy_data.json")
        )
        self.factory = RequestFactory()
        self.credentials = b64encode(b"admin:admin").decode("ascii")

    def test_media_matches_no_filter(self):
        obj = MockFileObject(True)

        self.assertTrue(tekdb_filebrowser.media_matches(None, obj))

    def test_media_matches_has_record(self):
        obj_true = MockFileObject(True)
        obj_false = MockFileObject(False)
        self.assertTrue(tekdb_filebrowser.media_matches("has_record", obj_true))
        self.assertFalse(tekdb_filebrowser.media_matches("has_record", obj_false))

    def test_media_matches_no_record(self):
        obj_true = MockFileObject(True)
        obj_false = MockFileObject(False)
        self.assertFalse(tekdb_filebrowser.media_matches("no_record", obj_true))
        self.assertTrue(tekdb_filebrowser.media_matches("no_record", obj_false))

    def test_media_matches_callable_attribute(self):
        obj = MockFileObject(lambda: True)
        self.assertTrue(tekdb_filebrowser.media_matches("has_record", obj))

    def test_get_urls(self):
        confirm_url = reverse("filebrowser:fb_delete_all_media_without_record_confirm")
        delete_url = reverse("filebrowser:fb_delete_all_media_without_record")

        self.assertIn("delete-media-without-record-confirm", confirm_url)
        self.assertIn("delete-media-without-record", delete_url)

    def test_browse_media_filter_has_record(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        url = reverse("filebrowser:fb_browse")
        unfiltered_response = self.client.get(
            url, headers={"Authorization": f"Basic {self.credentials}"}
        )
        self.assertEqual(unfiltered_response.status_code, 200)

        filter_response = self.client.get(
            url,
            headers={"Authorization": f"Basic {self.credentials}"},
            QUERY_STRING="&filter_media_record=has_record",
        )
        self.assertEqual(filter_response.status_code, 200)
        self.assertEqual(
            filter_response.context_data["query"]["filter_media_record"], "has_record"
        )

        for item in filter_response.context_data["page"]:
            self.assertTrue(item.has_media_record())
        filtered_filelisting = filter_response.context_data.get("filelisting")
        unfiltered_filelisting = unfiltered_response.context_data.get("filelisting")

        filtered_results_current = filtered_filelisting.results_current
        unfiltered_results_current = unfiltered_filelisting.results_current

        filtered_results_total = filtered_filelisting.results_total
        unfiltered_results_total = unfiltered_filelisting.results_total

        self.assertTrue(filtered_results_current < unfiltered_results_current)
        self.assertTrue(filtered_results_total < unfiltered_results_total)

    def test_browse_media_filter_no_record(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        url = reverse("filebrowser:fb_browse")
        response = self.client.get(
            url,
            headers={"Authorization": f"Basic {self.credentials}"},
            QUERY_STRING="&filter_media_record=no_record",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context_data["query"]["filter_media_record"], "no_record"
        )

        for item in response.context_data["page"]:
            self.assertFalse(item.has_media_record())

    def test_browse_media_filter_multiple_filters(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        url = reverse("filebrowser:fb_browse")
        response = self.client.get(
            url,
            headers={"Authorization": f"Basic {self.credentials}"},
            QUERY_STRING="&filter_media_record=has_record&filter_type=Image",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context_data["query"]["filter_media_record"], "has_record"
        )
        self.assertEqual(response.context_data["query"]["filter_type"], "Image")

        for item in response.context_data["page"]:
            self.assertEqual(item.filetype, "Image")
            self.assertTrue(item.has_media_record())

    def test_browse_media_filter_invalid(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        url = reverse("filebrowser:fb_browse")
        response = self.client.get(
            url,
            headers={"Authorization": f"Basic {self.credentials}"},
            QUERY_STRING="&filter_media_record=invalid_value",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context_data["query"]["filter_media_record"], "invalid_value"
        )

        # With an invalid filter, all items should be returned
        all_items = list(response.context_data["page"])
        self.assertGreater(len(all_items), 0)

    def test_delete_media_without_record_confirm(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        # media file that has a related Media record
        media_file_name = "gumboot_chiton_fT5Kxtm.jpg"

        url = reverse("filebrowser:fb_delete_all_media_without_record_confirm")
        response = self.client.post(
            url,
            headers={"Authorization": f"Basic {self.credentials}"},
        )
        self.assertEqual(response.status_code, 200)

        filelisting = response.context_data["filelisting"]
        self.assertNotIn(media_file_name, [f.filename for f in filelisting])

    def test_delete_media_without_record(self):
        from TEKDB.models import Users

        user = Users.objects.get(username="admin")
        self.client.force_login(user)

        delete_url = reverse("filebrowser:fb_delete_all_media_without_record")

        confirm_url = reverse("filebrowser:fb_delete_all_media_without_record_confirm")
        confirm_resp = self.client.post(
            confirm_url,
            headers={"Authorization": f"Basic {self.credentials}"},
        )
        self.assertEqual(confirm_resp.status_code, 200)

        filelisting = confirm_resp.context_data.get("filelisting", [])
        if filelisting:
            file_obj_class = filelisting[0].__class__
        else:
            file_obj_class = None

        if file_obj_class is not None:
            with (
                patch.object(
                    file_obj_class, "delete_versions", new=Mock(return_value=None)
                ),
                patch.object(file_obj_class, "delete", new=Mock(return_value=None)),
            ):
                response = self.client.post(
                    delete_url,
                    headers={"Authorization": f"Basic {self.credentials}"},
                )

        self.assertEqual(response.status_code, 302)
