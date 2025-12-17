from ..models import PageContent
from rest_framework import serializers

class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ['page', 'content', 'is_html', 'html_content']
        read_only_fields = ['page']  # Make 'page' read-only to prevent changes
