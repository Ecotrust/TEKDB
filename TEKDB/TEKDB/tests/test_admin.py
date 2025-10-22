# from django.conf import settings
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite
from django.urls import reverse
import os
from TEKDB.admin import MediaBulkUploadAdmin
from TEKDB.forms import MediaBulkUploadForm
from TEKDB.models import MediaBulkUpload, Media
from TEKDB.tests.test_models import ITKTestCase

User = get_user_model()


class MediaBulkUploadAdminTest(ITKTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="admin2", password="password", email="admin@example.com"
        )

    def test_media_bulk_upload_admin_add(self):
        url = reverse("admin:TEKDB_mediabulkupload_add")
        test_image = SimpleUploadedFile(
            "./test_image.jpg", b"\x00\x00\x00\x00", content_type="image"
        )

        # TODO: Associate the images with 1+ Places, Resources, Citations, Activities, and PlacesResources

        request = self.factory.post(
            url,
            {
                # 'mediabulkname': 'Test Bulk Upload',
                # 'mediabulkdate': '2024-12-12',
                "files": [test_image, test_image],
            },
        )
        request.user = self.user
        bulk_admin = MediaBulkUploadAdmin(model=MediaBulkUpload, admin_site=AdminSite())
        bulk_form = MediaBulkUploadForm(request.POST)
        bulk_form.is_valid()
        bulk_admin.save_model(
            obj=MediaBulkUpload(), request=request, form=bulk_form, change=None
        )

        self.assertTrue(Media.objects.filter(medianame="test_image").exists())
        self.assertTrue(Media.objects.filter(medianame="test_image").count() == 2)

        for media in Media.objects.filter(medianame="test_image"):
            self.assertTrue(os.path.exists(media.mediafile.path))
            os.remove(
                media.mediafile.path
            )  # Clean up the uploaded files after the test
            self.assertFalse(os.path.exists(media.mediafile.path))
            media.delete()

    ### We don't need to test the admin change and delete views for now
    # def test_media_bulk_upload_admin_change(self):
    #     media_bulk_upload = MediaBulkUpload.objects.create(mediabulkname='Test Bulk Upload', mediabulkdate='2023-10-01')
    #     url = reverse('admin:TEKDB_mediabulkupload_change', args=[media_bulk_upload.id])
    #     response = self.client.post(url, {
    #         'mediabulkname': 'Updated Bulk Upload',
    #         'mediabulkdate': '2023-10-01',
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     media_bulk_upload.refresh_from_db()
    #     self.assertEqual(media_bulk_upload.mediabulkname, 'Updated Bulk Upload')

    # def test_media_bulk_upload_admin_delete(self):
    #     media_bulk_upload = MediaBulkUpload.objects.create(mediabulkname='Test Bulk Upload', mediabulkdate='2023-10-01')
    #     url = reverse('admin:TEKDB_mediabulkupload_delete', args=[media_bulk_upload.id])
    #     response = self.client.post(url, {'post': 'yes'})
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(MediaBulkUpload.objects.filter(id=media_bulk_upload.id).exists())
