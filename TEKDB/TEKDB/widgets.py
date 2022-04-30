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
    template_name = 'gis/openlayers.html'
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