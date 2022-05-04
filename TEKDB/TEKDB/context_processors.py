

def add_map_default_context(request):
    from django.conf import settings
    from configuration.models import Configuration
    
    # SET BASELINE
    MAP_DEFAULTS = {
        'default_lon': 0,
        'default_lat': 0,
        'default_zoom': 1,
        'map_extent': False
    }

    # Override BASELINE with any settings or local settings
    if hasattr(settings, 'DATABASE_GEOGRAPHY'):
        for key in settings.DATABASE_GEOGRAPHY.keys():
            MAP_DEFAULTS[key] = settings.DATABASE_GEOGRAPHY[key]

    try:
        configurations = Configuration.objects.all()
        if configurations.count() > 0:
            for config in configurations:
                if hasattr(config, 'geometry') and hasattr(config.geometry, 'extent') and len(config.geometry.extent) == 4:
                    MAP_DEFAULTS['map_extent'] = [x for x in config.geometry.extent]
                    break

    except Exception as e:
        pass

    return MAP_DEFAULTS

    

