# from django.conf import settings
from django.test import RequestFactory
from unittest.mock import patch
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite
from django.urls import reverse
import os
from TEKDB.forms import MediaBulkUploadForm
from TEKDB.models import MediaBulkUpload, Media
from TEKDB.tests.test_models import ITKTestCase

User = get_user_model()


class MediaFormAdminTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin1", password="password", email="admin1@example.com"
        )

    def test_media_admin_add(self):
        from TEKDB.admin import MediaForm

        form = MediaForm()

        self.assertIn("mediatype", form.fields)
        queryset = form.fields["mediatype"].queryset
        self.assertTrue(queryset.exists())


class ResourcesActivityEventsFormAdminTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin3", password="password", email="admin3@example.com"
        )

    def test_resources_activity_events_admin_add(self):
        from TEKDB.admin import ResourcesActivityEventsForm

        form = ResourcesActivityEventsForm()

        self.assertIn("participants", form.fields)
        queryset = form.fields["participants"].queryset
        self.assertTrue(queryset.exists())

        self.assertIn("technique", form.fields)
        queryset = form.fields["technique"].queryset
        self.assertTrue(queryset.exists())

        self.assertIn("activityshortdescription", form.fields)
        queryset = form.fields["activityshortdescription"].queryset
        self.assertTrue(queryset.exists())


class CitationsFormAdminTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin4", password="password", email="admin4@example.com"
        )

    def test_citations_admin_add(self):
        from TEKDB.admin import CitationsForm

        form = CitationsForm()

        self.assertIn("referencetype", form.fields)
        queryset = form.fields["referencetype"].queryset
        self.assertTrue(queryset.exists())

        self.assertIn("intervieweeid", form.fields)
        queryset = form.fields["intervieweeid"].queryset
        self.assertTrue(queryset.exists())

        self.assertIn("interviewerid", form.fields)
        queryset = form.fields["interviewerid"].queryset
        self.assertTrue(queryset.exists())


class PlacesFormAdminTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin5", password="password", email="admin5@example.com"
        )

    def test_places_admin_add(self):
        from TEKDB.admin import PlacesForm

        form = PlacesForm()

        self.assertIn("planningunitid", form.fields)
        queryset = form.fields["planningunitid"].queryset
        self.assertTrue(queryset.exists())

        self.assertIn("primaryhabitat", form.fields)
        queryset = form.fields["primaryhabitat"].queryset
        self.assertTrue(queryset.exists())

        self.assertIn("tribeid", form.fields)
        queryset = form.fields["tribeid"].queryset
        self.assertTrue(queryset.exists())


class ResourcesFormAdminTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin6", password="password", email="admin6@example.com"
        )

    def test_resources_admin_add(self):
        from TEKDB.admin import ResourcesForm

        form = ResourcesForm()

        self.assertIn("resourceclassificationgroup", form.fields)
        queryset = form.fields["resourceclassificationgroup"].queryset
        self.assertTrue(queryset.exists())


class PlacesResourceEventFormAdminTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin7", password="password", email="admin7@example.com"
        )

    def test_places_resource_event_admin_add(self):
        from TEKDB.admin import PlacesResourceEventForm

        form = PlacesResourceEventForm()

        self.assertIn("partused", form.fields)
        queryset = form.fields["partused"].queryset
        self.assertTrue(queryset.exists())

        self.assertIn("season", form.fields)
        queryset = form.fields["season"].queryset
        self.assertTrue(queryset.exists())

        self.assertIn("timing", form.fields)
        queryset = form.fields["timing"].queryset
        self.assertTrue(queryset.exists())


class MediaBulkUploadAdminTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin2", password="password", email="admin@example.com"
        )

    def test_media_bulk_upload_admin_add(self):
        from TEKDB.models import (
            Places,
            Resources,
            Citations,
            ResourcesActivityEvents,
            PlacesResourceEvents,
        )
        from TEKDB.admin import MediaBulkUploadAdmin

        url = reverse("admin:TEKDB_mediabulkupload_add")
        test_image = SimpleUploadedFile(
            "./test_image.jpg", b"\x00\x00\x00\x00", content_type="image"
        )

        place = Places.objects.create(indigenousplacename="Test Place")
        resource = Resources.objects.create(commonname="Test Resource")
        citation = Citations.objects.create(
            referencetext="Test Citation", referencetype_id=1
        )
        placeresource = PlacesResourceEvents.objects.create(
            placeid=place, resourceid=resource
        )
        activity = ResourcesActivityEvents.objects.create(placeresourceid=placeresource)

        post_data = {
            "files": [test_image, test_image],
            "places": [place.pk],
            "resources": [resource.pk],
            "citations": [citation.pk],
            "activities": [activity.pk],
            "placesresources": [placeresource.pk],
        }

        request = self.factory.post(url, post_data)
        request.user = self.user
        bulk_admin = MediaBulkUploadAdmin(model=MediaBulkUpload, admin_site=AdminSite())
        bulk_form = MediaBulkUploadForm(request.POST)
        bulk_form.is_valid()
        bulk_admin.save_model(
            obj=MediaBulkUpload(), request=request, form=bulk_form, change=None
        )

        self.assertTrue(Media.objects.filter(medianame="test_image").exists())
        self.assertTrue(Media.objects.filter(medianame="test_image").count() == 2)

        self.assertTrue(Places.objects.filter(pk=place.pk).exists())
        self.assertTrue(Resources.objects.filter(pk=resource.pk).exists())
        self.assertTrue(Citations.objects.filter(pk=citation.pk).exists())
        self.assertTrue(ResourcesActivityEvents.objects.filter(pk=activity.pk).exists())
        self.assertTrue(
            PlacesResourceEvents.objects.filter(pk=placeresource.pk).exists()
        )

        for media in Media.objects.filter(medianame="test_image"):
            self.assertTrue(os.path.exists(media.mediafile.path))
            os.remove(
                media.mediafile.path
            )  # Clean up the uploaded files after the test
            self.assertFalse(os.path.exists(media.mediafile.path))
            media.delete()

        # Clean up related objects
        activity.delete()
        placeresource.delete()
        citation.delete()
        resource.delete()
        place.delete()

    def test_media_bulk_upload_admin_other_types(self):
        from TEKDB.admin import MediaBulkUploadAdmin

        url = reverse("admin:TEKDB_mediabulkupload_add")
        test_other_type = SimpleUploadedFile(
            "./test_thing.shp", b"\x00\x00\x00\x00", content_type="other"
        )

        request = self.factory.post(
            url,
            {
                "files": [test_other_type, test_other_type],
            },
        )

        request.user = self.user
        bulk_admin = MediaBulkUploadAdmin(model=MediaBulkUpload, admin_site=AdminSite())
        bulk_form = MediaBulkUploadForm(request.POST)
        bulk_form.is_valid()
        bulk_admin.save_model(
            obj=MediaBulkUpload(), request=request, form=bulk_form, change=None
        )

        for media in Media.objects.filter(medianame="test_thing"):
            self.assertTrue(os.path.exists(media.mediafile.path))
            os.remove(
                media.mediafile.path
            )  # Clean up the uploaded files after the test
            self.assertFalse(os.path.exists(media.mediafile.path))
            media.delete()

    def test_media_bulk_upload_admin_thumbnail_gallery(self):
        from TEKDB.admin import MediaBulkUploadAdmin
        from TEKDB.models import MediaBulkUpload, Media

        url = reverse("admin:TEKDB_mediabulkupload_add")
        test_image = SimpleUploadedFile(
            "./thumbnail_test_image.jpg", b"\x00\x00\x00\x00", content_type="image"
        )
        test_video = SimpleUploadedFile(
            "./thumbnail_test_video.mp4", b"\x00\x00\x00\x00", content_type="video"
        )
        test_audio = SimpleUploadedFile(
            "./thumbnail_test_audio.mp3", b"\x00\x00\x00\x00", content_type="audio"
        )
        test_text = SimpleUploadedFile(
            "./thumbnail_test_text.txt", b"\x00\x00\x00\x00", content_type="text"
        )
        test_other = SimpleUploadedFile(
            "./thumbnail_test_thing.shp", b"\x00\x00\x00\x00", content_type="other"
        )
        test_unknown_type = SimpleUploadedFile(
            "./thumbnail_test_unknown.xyz", b"\x00\x00\x00\x00", content_type="unknown"
        )

        post_data = {
            "files": [
                test_image,
                test_video,
                test_audio,
                test_text,
                test_other,
                test_unknown_type,
            ],
        }

        request = self.factory.post(url, post_data)
        request.user = self.user
        bulk_admin = MediaBulkUploadAdmin(model=MediaBulkUpload, admin_site=AdminSite())
        bulk_form = MediaBulkUploadForm(request.POST)
        bulk_form.is_valid()
        bulk_upload_obj = MediaBulkUpload()
        bulk_admin.save_model(
            obj=bulk_upload_obj, request=request, form=bulk_form, change=None
        )

        html = bulk_admin.thumbnail_gallery(bulk_upload_obj)

        self.assertIn("test_image", html)
        self.assertIn("img", html)
        self.assertIn("test_video", html)
        self.assertIn("Your browser does not support the video tag.", html)
        self.assertIn("test_audio", html)
        self.assertIn("audio-x-generic.svg", html)
        self.assertIn("test_text", html)
        self.assertIn("doc-text.svg", html)
        self.assertIn("test_thing", html)
        self.assertIn("unknown-mail.png", html)
        self.assertIn("test_unknown", html)

        # Clean up
        for media in Media.objects.filter(medianame__icontains="thumbnail_test"):
            if hasattr(media, "mediafile") and media.mediafile:
                if os.path.exists(media.mediafile.path):
                    os.remove(media.mediafile.path)
            media.delete()

    def test_media_bulk_upload_admin_get_readonly_fields(self):
        from TEKDB.models import MediaBulkUpload
        from TEKDB.admin import MediaBulkUploadAdmin

        bulk_admin = MediaBulkUploadAdmin(model=MediaBulkUpload, admin_site=AdminSite())
        readonly_fields_obj_exists = bulk_admin.get_readonly_fields(
            request=None, obj=MediaBulkUpload()
        )
        self.assertNotIn("thumbnail_gallery", readonly_fields_obj_exists)
        self.assertIn("id", readonly_fields_obj_exists)

        readonly_fields_obj_not_exists = bulk_admin.get_readonly_fields(
            request=None, obj=None
        )
        self.assertIn("thumbnail_gallery", readonly_fields_obj_not_exists)
        self.assertNotIn("id", readonly_fields_obj_not_exists)

    def test_media_bulk_upload_admin_has_change_permission(self):
        from TEKDB.models import MediaBulkUpload
        from TEKDB.admin import MediaBulkUploadAdmin

        bulk_admin = MediaBulkUploadAdmin(model=MediaBulkUpload, admin_site=AdminSite())
        has_change_perm = bulk_admin.has_change_permission(
            request=None, obj=MediaBulkUpload()
        )
        self.assertFalse(has_change_perm)

    def test_media_bulk_upload_admin_has_delete_permission(self):
        from TEKDB.models import MediaBulkUpload
        from TEKDB.admin import MediaBulkUploadAdmin

        bulk_admin = MediaBulkUploadAdmin(model=MediaBulkUpload, admin_site=AdminSite())
        has_delete_perm = bulk_admin.has_delete_permission(
            request=None, obj=MediaBulkUpload()
        )
        self.assertTrue(has_delete_perm)

    def test_media_bulk_upload_admin_has_add_permission(self):
        from TEKDB.models import MediaBulkUpload
        from TEKDB.admin import MediaBulkUploadAdmin

        bulk_admin = MediaBulkUploadAdmin(model=MediaBulkUpload, admin_site=AdminSite())
        has_add_perm = bulk_admin.has_add_permission(request=None)
        self.assertTrue(has_add_perm)


class RecordAdminProxyTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin8", password="password", email="admin8@example.com"
        )

    def test_save_model_sets_enteredby_fields(self):
        from TEKDB.admin import RecordAdminProxy
        from TEKDB.models import Media
        from django import forms

        class MediaForm(forms.ModelForm):
            class Meta:
                model = Media
                fields = "__all__"

        # Create a minimal Media instance
        media = Media.objects.create(medianame="test_media")
        request = self.factory.post("/test/")
        request.user = self.user
        form = MediaForm(instance=media)
        admin = RecordAdminProxy(Media, AdminSite())
        admin.save_model(request, media, form, change=False)
        self.assertEqual(media.enteredbyname, self.user.username)
        self.assertEqual(media.enteredbytribe, getattr(self.user, "affiliation", None))
        self.assertEqual(media.enteredbytitle, getattr(self.user, "title", None))
        self.assertEqual(media.modifiedbyname, self.user.username)
        self.assertEqual(media.modifiedbytribe, getattr(self.user, "affiliation", None))
        self.assertEqual(media.modifiedbytitle, getattr(self.user, "title", None))
        media.delete()

    def test_save_formset_sets_enteredby_fields(self):
        from TEKDB.admin import RecordAdminProxy
        from TEKDB.models import Media
        from django import forms

        class MediaForm(forms.ModelForm):
            class Meta:
                model = Media
                fields = "__all__"

        media1 = Media.objects.create(medianame="test_media1")
        media2 = Media.objects.create(medianame="test_media2")
        request = self.factory.post("/test/")
        request.user = self.user

        class MediaFormset:
            def save(self, commit):
                return [media1, media2]

        form = MediaForm()
        formset = MediaFormset()
        admin = RecordAdminProxy(Media, AdminSite())
        admin.save_formset(request, form, formset, change=False)
        for media in [media1, media2]:
            self.assertEqual(media.enteredbyname, self.user.username)
            self.assertEqual(
                media.enteredbytribe, getattr(self.user, "affiliation", None)
            )
            self.assertEqual(media.enteredbytitle, getattr(self.user, "title", None))
            self.assertEqual(media.modifiedbyname, self.user.username)
            self.assertEqual(
                media.modifiedbytribe, getattr(self.user, "affiliation", None)
            )
            self.assertEqual(media.modifiedbytitle, getattr(self.user, "title", None))
        media1.delete()
        media2.delete()


class NestedRecordAdminProxyTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin9", password="password", email="admin9@example.com"
        )

    def test_save_model(self):
        from TEKDB.admin import NestedRecordAdminProxy
        from TEKDB.models import Places
        from django import forms

        class PlacesForm(forms.ModelForm):
            class Meta:
                model = Places
                fields = "__all__"

        place = Places.objects.create(indigenousplacename="test_place")
        request = self.factory.post("/test/")
        request.user = self.user
        form = PlacesForm(instance=place)
        admin = NestedRecordAdminProxy(Places, AdminSite())
        admin.save_model(request, place, form, change=False)
        self.assertEqual(place.enteredbyname, self.user.username)
        self.assertEqual(place.enteredbytribe, getattr(self.user, "affiliation", None))
        self.assertEqual(place.enteredbytitle, getattr(self.user, "title", None))
        self.assertEqual(place.modifiedbyname, self.user.username)
        self.assertEqual(place.modifiedbytribe, getattr(self.user, "affiliation", None))
        self.assertEqual(place.modifiedbytitle, getattr(self.user, "title", None))
        place.delete()

    def test_save_formset(self):
        from TEKDB.admin import NestedRecordAdminProxy
        from TEKDB.models import Places
        from django import forms

        class PlacesForm(forms.ModelForm):
            class Meta:
                model = Places
                fields = "__all__"

        place1 = Places.objects.create(indigenousplacename="test_place1")
        place2 = Places.objects.create(indigenousplacename="test_place2")
        request = self.factory.post("/test/")
        request.user = self.user

        class PlacesFormset:
            def save(self, commit):
                return [place1, place2]

        form = PlacesForm()
        formset = PlacesFormset()
        admin = NestedRecordAdminProxy(Places, AdminSite())
        admin.save_formset(request, form, formset, change=False)
        for place in [place1, place2]:
            self.assertEqual(place.enteredbyname, self.user.username)
            self.assertEqual(
                place.enteredbytribe, getattr(self.user, "affiliation", None)
            )
            self.assertEqual(place.enteredbytitle, getattr(self.user, "title", None))
            self.assertEqual(place.modifiedbyname, self.user.username)
            self.assertEqual(
                place.modifiedbytribe, getattr(self.user, "affiliation", None)
            )
            self.assertEqual(place.modifiedbytitle, getattr(self.user, "title", None))
        place1.delete()
        place2.delete()

    def test_needs_review_true(self):
        from TEKDB.admin import NestedRecordAdminProxy
        from TEKDB.models import Places

        place = Places.objects.create(indigenousplacename="test_place")
        request = self.factory.post("/test/")
        request.user = self.user

        admin = NestedRecordAdminProxy(Places, AdminSite())
        result_true = admin.needs_Review(place)
        self.assertIn("icon-alert.svg", result_true)
        place.delete()

    def test_needs_review_false(self):
        from TEKDB.admin import NestedRecordAdminProxy
        from TEKDB.models import Places

        place = Places.objects.create(
            indigenousplacename="test_place", needsReview=False
        )
        request = self.factory.post("/test/")
        request.user = self.user

        admin = NestedRecordAdminProxy(Places, AdminSite())
        result_false = admin.needs_Review(place)
        self.assertIn("<span>", result_false)
        place.delete()


class RecordModelAdminTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin10", password="password", email="admin10@example.com"
        )

    def test_needs_review_true(self):
        from TEKDB.admin import RecordModelAdmin
        from TEKDB.models import Places

        place = Places.objects.create(indigenousplacename="test_place")
        request = self.factory.post("/test/")
        request.user = self.user

        admin = RecordModelAdmin(Places, AdminSite())
        result_true = admin.needs_Review(place)
        self.assertIn("icon-alert.svg", result_true)
        place.delete()

    def test_needs_review_false(self):
        from TEKDB.admin import RecordModelAdmin
        from TEKDB.models import Places

        place = Places.objects.create(
            indigenousplacename="test_place", needsReview=False
        )
        request = self.factory.post("/test/")
        request.user = self.user

        admin = RecordModelAdmin(Places, AdminSite())
        result_false = admin.needs_Review(place)
        self.assertIn("<span>", result_false)
        place.delete()

    def test_change_view(self):
        from TEKDB.admin import RecordModelAdmin
        from TEKDB.models import Places

        place = Places.objects.create(indigenousplacename="test_place")
        url = reverse("admin:TEKDB_places_change", args=[place.placeid])
        request = self.factory.get(url)
        request.user = self.user

        admin = RecordModelAdmin(Places, AdminSite())
        with patch.object(RecordModelAdmin, "has_change_permission", return_value=True):
            response = admin.change_view(request, str(place.placeid))
            self.assertEqual(response.status_code, 200)
        place.delete()


class PlacesAdminTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin11", password="password", email="admin11@example.com"
        )

    def test_places_admin_changelist_view(self):
        from TEKDB.admin import PlacesAdmin
        from TEKDB.models import Places

        place = Places.objects.create(indigenousplacename="test_place")
        url = reverse("admin:TEKDB_places_changelist")
        request = self.factory.get(url)
        request.user = self.user

        admin = PlacesAdmin(Places, AdminSite())
        with patch.object(PlacesAdmin, "has_change_permission", return_value=True):
            response = admin.changelist_view(request)
            self.assertEqual(response.status_code, 200)
            self.assertIn("results_geojson", response.context_data)
        place.delete()
