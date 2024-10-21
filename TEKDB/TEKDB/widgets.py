import logging

from django.conf import settings
from django.contrib.gis import gdal
from django.contrib.gis.geometry import json_regex
from django.contrib.gis.geos import GEOSException, GEOSGeometry
from django.forms.widgets import Widget
from django.utils import translation

logger = logging.getLogger('django.contrib.gis')

from django.contrib.gis.forms.widgets import OpenLayersWidget, BaseGeometryWidget

# class OpenLayersWidget(BaseGeometryWidget):
# class OpenLayers6Widget(OpenLayersWidget):
class OpenLayers6Widget(BaseGeometryWidget):
    template_name = 'gis/openlayers_widget_itkdb.html'
    map_srid = 3857

    class Media:
        css = {
            'all': (
                'assets/openlayers6/ol.css',
                'gis/css/ol3.css',
            )
        }
        js = (
            'assets/openlayers6/ol.js',
            'gis/js/OL6MapWidget.js',
        )

    def serialize(self, value):
        return value.json if value else ''

    def deserialize(self, value):
        geom = super().deserialize(value)
        # GeoJSON assumes WGS84 (4326). Use the map's SRID instead.
        if geom and json_regex.match(value) and self.map_srid != 4326:
            geom.srid = self.map_srid
        return geom

    def get_context(self, name, value, attrs):
        from TEKDB.context_processors import add_map_default_context
        request_context = add_map_default_context({})   # passing empty dict to represent unneccesary request value
        widget_context = super().get_context(name, value, attrs)
        widget_context.update(request_context)

        return widget_context

class OpenLayers6PolygonWidget(OpenLayers6Widget):
    class Media:
        css = {
            'all': (
                'assets/openlayers6/ol.css',
                'gis/css/ol3.css',
                'gis/css/OpenLayers6PolygonWidget.css',
            )
        }
        js = (
            'assets/openlayers6/ol.js',
            'gis/js/OL6MapPolygonWidget.js',
        )


from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe

class ThumbnailFileInput(ClearableFileInput):
    template_name = 'widgets/thumbnail_file_input.html'

    def format_value(self, value):
        if value and hasattr(value, 'url'):
            return mark_safe(f'<img src="{value.url}" width="100" height="100" />')
        return super().format_value(value)