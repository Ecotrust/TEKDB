from ..models import PageContent
from rest_framework import serializers


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ["page", "content", "is_html", "html_content"]
        read_only_fields = ["page"]  # Make 'page' read-only to prevent changes


class SiteConfigurationSerializer(serializers.Serializer):
    proj_logo_text = serializers.CharField(max_length=100)
    proj_text_placement = serializers.CharField(max_length=50)
    proj_css = serializers.DictField(child=serializers.CharField(max_length=100))
    proj_icons = serializers.DictField(child=serializers.CharField(max_length=100))
    proj_image_select = serializers.CharField(max_length=100)
    home_image_attribution = serializers.CharField(max_length=255, allow_blank=True)
    home_font_color = serializers.CharField(max_length=7)
    homepage_left_background = serializers.CharField(max_length=7)
    homepage_right_background = serializers.CharField(max_length=7)
    map_pin = serializers.CharField(max_length=100)
    map_pin_selected = serializers.CharField(max_length=100)
