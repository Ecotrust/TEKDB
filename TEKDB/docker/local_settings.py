TIME_ZONE = 'America/Los_Angeles' # To see all Timezone options, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
REGISTRATION_OPEN = False
DATABASE_GEOGRAPHY = {
    ###EPSG:4326###
    # 'default_lon': -124.325,
    # 'default_lat': 42.065,
    ###EPSG:3857###
    'default_lon': -13839795.69,
    'default_lat': 5171448.926,
    'default_zoom': 8,
    'map_template': 'gis/admin/ol2osm.html',
    'map_extent': [-24000000, 1450000, -6200000, 13000000], #US Territories
    'min_zoom': 2,
    'max_zoom': 19,
}
STATIC_ROOT = '/vol/web/static'
MEDIA_ROOT = '/vol/web/media'
