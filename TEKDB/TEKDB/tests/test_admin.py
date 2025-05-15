from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from TEKDB.models import MediaBulkUpload, LookupMediaType, Media

User = get_user_model()

class MediaBulkUploadAdminTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='password', email='admin@example.com')
        self.client.login(username='admin', password='password')
        self.media_type = LookupMediaType.objects.create(mediatype='image')

    def test_media_bulk_upload_admin_add(self):
        url = reverse('admin:TEKDB_mediabulkupload_add')
        test_image = SimpleUploadedFile("./test_image.jpg", b"\x00\x00\x00\x00", content_type="image")
        response = self.client.post(url, {
            'mediabulkname': 'Test Bulk Upload',
            'mediabulkdate': '2024-12-12',
            'files': [test_image, test_image],
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(MediaBulkUpload.objects.filter(mediabulkname='Test Bulk Upload').exists())
        self.assertTrue(Media.objects.filter(medianame='test_image.jpg').exists())

    def test_media_bulk_upload_admin_change(self):
        media_bulk_upload = MediaBulkUpload.objects.create(mediabulkname='Test Bulk Upload', mediabulkdate='2023-10-01')
        url = reverse('admin:TEKDB_mediabulkupload_change', args=[media_bulk_upload.id])
        response = self.client.post(url, {
            'mediabulkname': 'Updated Bulk Upload',
            'mediabulkdate': '2023-10-01',
        })
        self.assertEqual(response.status_code, 302)
        media_bulk_upload.refresh_from_db()
        self.assertEqual(media_bulk_upload.mediabulkname, 'Updated Bulk Upload')

    def test_media_bulk_upload_admin_delete(self):
        media_bulk_upload = MediaBulkUpload.objects.create(mediabulkname='Test Bulk Upload', mediabulkdate='2023-10-01')
        url = reverse('admin:TEKDB_mediabulkupload_delete', args=[media_bulk_upload.id])
        response = self.client.post(url, {'post': 'yes'})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(MediaBulkUpload.objects.filter(id=media_bulk_upload.id).exists())