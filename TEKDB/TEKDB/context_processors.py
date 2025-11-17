def search_settings(request=None):
    try:
        from django.conf import settings
    except Exception:
        try:
            from TEKDB import settings
        except Exception as e:
            print("Could not import settings from TEKDB")
            print(e)
            settings = False

    try:
        from configuration.models import Configuration

        configs = Configuration.objects.all()[0]
    except Exception:
        configs = False

    search_config = {
        "MIN_SEARCH_RANK": 0.01,  # Default value
        "MIN_SEARCH_SIMILARITY": 0.1,  # Default
    }

    if settings:
        try:
            search_config = {
                "MIN_SEARCH_RANK": settings.MIN_SEARCH_RANK,
                "MIN_SEARCH_SIMILARITY": settings.MIN_SEARCH_SIMILARITY,
            }
        except Exception:
            print("No MIN_SEARCH_RANK or MIN_SEARCH_SIMILARITY in settings")
            pass

    if configs:
        try:
            min_search_rank = (
                configs.min_search_rank
                if configs.min_search_rank
                else search_config["MIN_SEARCH_RANK"]
            )
            min_search_similarity = (
                configs.min_search_similarity
                if configs.min_search_similarity
                else search_config["MIN_SEARCH_SIMILARITY"]
            )
            search_config = {
                "MIN_SEARCH_RANK": min_search_rank,
                "MIN_SEARCH_SIMILARITY": min_search_similarity,
            }
        except Exception:
            print("No min_search_rank or min_search_similarity in Configuration")
            pass

    return search_config


def add_map_default_context(request):
    from django.conf import settings
    from configuration.models import Configuration

    # SET BASELINE
    MAP_DEFAULTS = {
        "default_lon": 0,
        "default_lat": 0,
        "default_zoom": 1,
        "map_extent": False,
    }

    # Override BASELINE with any settings or local settings
    if hasattr(settings, "DATABASE_GEOGRAPHY"):
        for key in settings.DATABASE_GEOGRAPHY.keys():
            MAP_DEFAULTS[key] = settings.DATABASE_GEOGRAPHY[key]

    try:
        configurations = Configuration.objects.all()
        if configurations.count() > 0:
            for config in configurations:
                if (
                    hasattr(config, "geometry")
                    and hasattr(config.geometry, "extent")
                    and len(config.geometry.extent) == 4
                ):
                    MAP_DEFAULTS["map_extent"] = [x for x in config.geometry.extent]
                    break

    except Exception:
        pass

    return MAP_DEFAULTS
