# TEKDB/apps.py

from django.apps import AppConfig


class TEKDBConfig(AppConfig):
    name = "TEKDB"
    verbose_name = "Records"

    def ready(self):
        from filebrowser.base import FileObject
        from .models import Media
        
        def get_related_media(self):
            """
            Returns QuerySet of Media records that reference this file
            The file field stores paths relative to MEDIA_ROOT
            """
            # self.path gives the relative path from MEDIA_ROOT
            # which should match what's stored in the mediafile field
            return Media.objects.filter(mediafile=self.path)
        
        
        def has_media_record(self):
            """Check if this file has any related Media records"""
            return self.get_related_media().exists()
        
        def get_media_count(self):
            """Returns count of related Media records"""
            return self.get_related_media().count()
        
        # Add methods to FileObject
        FileObject.get_related_media = get_related_media
        FileObject.has_media_record = has_media_record
        FileObject.get_media_count = get_media_count