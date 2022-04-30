from django.shortcuts import render
from configuration.models import Configuration

def get_default_geography():
    DEFAULT_GEOGRAPHY = {}
    try:
        if Configuration.objects.all().count() > 0:
            default_geography_geometry = Configuration.objects.all()[0].geometry
            DEFAULT_GEOGRAPHY['map_extent'] = [x for x in default_geography_geometry.extent]
    except Exception as e:
        print(e)
        pass

    if not 'map_extent' in DEFAULT_GEOGRAPHY.keys():
        from TEKDB.settings import DATABASE_GEOGRAPHY
        DEFAULT_GEOGRAPHY['map_extent'] = DATABASE_GEOGRAPHY['map_extent']
        #TODO: check SRID from settings, set lat/lon in 4326, then convert to 3857 if necessary
        # default_lon = DATABASE_GEOGRAPHY['default_lon']
        # default_lat = DATABASE_GEOGRAPHY['default_lat']
        # default_zoom = DATABASE_GEOGRAPHY['default_zoom']
        # map_template = DATABASE_GEOGRAPHY['map_template']

    return DEFAULT_GEOGRAPHY