def explore_context(request):
    try:
        from django.conf import settings
    except Exception as e:
        try:
            from TEKDB import settings
        except Exception as e:
            print('Could not import settings from TEKDB')
            print(e)
            settings = False

    try:
        from configuration.models import Configuration
        configs = Configuration.objects.all()[0]
    except Exception as e:
        configs = False

    ######################################
    #     PROJ_LOGO_TEXT                 #
    ######################################

    project_logo_text = 'ITK'
    project_text_placement = 'default'

    if settings:
        try:
            if len(settings.PROJ_LOGO_TEXT) > 0:
                project_logo_text = settings.PROJ_LOGO_TEXT
        except Exception as e:
            pass
    
    if configs:
        try:
            project_logo_text = configs.preferredInitialism
            project_text_placement = configs.preferredInitialismPlacement
        except Exception as e:
            pass

    ######################################
    #     PROJ_CSS                       #
    ######################################

    proj_css = {
        'primary_a': '#8f371c',
        'primary_b': '#f7f3eb',
        'primary_c': '#0e1522',
        'primary_d': '#ced2da',
        'secondary_a': '#51723b',
        'secondary_b': '#839230',
        'secondary_c': '#6ea32e',
        'secondary_d': '#b44ba3',
        'font_face_primary': '/static/explore/fonts/Open_Sans/static/OpenSans-Regular-export/OpenSans-Regular.css',
        'font_face_primary_bold': '/static/explore/fonts/Open_Sans/static/OpenSans-Bold-export/OpenSans-Bold.css',
        'font_face_primary_extrabold': '/static/explore/fonts/Open_Sans/static/OpenSans-ExtraBold-export/OpenSans-ExtraBold.css',
    }

    if settings:
        for key in proj_css.keys():
            try:
                if key in settings.PROJ_CSS.keys():
                    proj_css[key] = settings.PROJ_CSS[key]
            except Exception as e:
                pass

    if configs:
        # TODO: allow for admin-defined 8-color palettes
        for key in proj_css.keys():
            try:
                if hasattr(configs, key) and getattr(configs, key):
                    proj_css[key] = getattr(configs, key)
            except Exception as e:
                pass


    ######################################
    #     PROJ_ICONS                     #
    ######################################

    proj_icons = {
        'logo': '/static/explore/img/logos/logo_weave.svg',
        'place_icon': 'explore/img/icons/i_place.svg',
        'resource_icon': 'explore/img/icons/i_resource.svg',
        'activity_icon': 'explore/img/icons/i_activity.svg',
        'source_icon': 'explore/img/icons/i_source.svg',
        'media_icon': 'explore/img/icons/i_media.svg',
    }
    
    if settings:
        for key in proj_icons.keys():
            try:
                if key in settings.PROJ_ICONS.keys():
                    proj_icons[key] = settings.PROJ_ICONS[key]
            except Exception as e:
                pass
        
    if configs:
        for key in proj_icons.keys():
            try:
                if hasattr(configs, key) and getattr(configs, key):
                    icon_value = getattr(configs, key)
                    if icon_value == 'Other':
                        if hasattr(configs, '{}_override'.format(key)) and getattr(configs, '{}_override'.format(key)):
                            abs_project_icon_override_filename = getattr(configs, '{}_override'.format(key)).file.name
                            rel_filename = abs_project_icon_override_filename.split(settings.MEDIA_ROOT)[-1]
                            icon_override_select = "{}{}".format(settings.MEDIA_URL, rel_filename)
                            proj_icons[key] = icon_override_select
                    else:
                        proj_icons[key] = getattr(configs, key)
            except Exception as e:
                pass

    ######################################
    #     HOME IMAGE/Attribution         #
    ######################################

    project_image_select = '/static/explore/img/homepage/5050508427_ec55eed5f4_o.jpg'
    home_image_attribution = 'Image courtesy of <a href="https://www.flickr.com/photos/monteregina/5050508427" target="_blank">Monteregina</a> and used under <a href="https://creativecommons.org/licenses/by-nc-sa/2.0/" target="_blank">the CC BY-NC-SA 2.0 Licence</a>. No changes were made.'

    if settings:
        try:
            if settings.PROJ_IMAGE_SELECT and len(settings.PROJ_IMAGE_SELECT) > 0:
                project_image_select = settings.PROJ_IMAGE_SELECT
        except ImportError as e:
            pass

        try:
            if settings.PROJ_IMAGE_ATTR and len(settings.PROJ_IMAGE_ATTR) > 0:
                home_image_attribution = settings.PROJ_IMAGE_ATTR
        except ImportError as e:
            pass

    if configs:
        try:
            if hasattr(configs, 'homepage_image') and getattr(configs, 'homepage_image'):
                abs_project_image_filename = getattr(configs, 'homepage_image').file.name
                rel_filename = abs_project_image_filename.split(settings.MEDIA_ROOT)[-1]
                project_image_select = "{}{}".format(settings.MEDIA_URL, rel_filename)
                home_image_attribution = False
        except Exception as e:
            pass

        try:
            if hasattr(configs, 'homepage_image_attribution') and getattr(configs, 'homepage_image_attribution'):
                home_image_attribution = getattr(configs, 'homepage_image_attribution')
        except Exception as e:
            pass

    ######################################
    #     HOME_COLORS                #
    ######################################

    home_font_color = '#FFFFFF'
    homepage_left_background = '#000000'
    homepage_right_background = '#000000'

    if settings:
        try:
            home_font_color = settings.HOME_FONT_COLOR
        except Exception as e:
            pass
        try:
            homepage_left_background = settings.HOME_LEFT_BACKGROUND
        except Exception as e:
            pass
        try:
            homepage_right_background = settings.HOME_RIGHT_BACKGROUND
        except Exception as e:
            pass
    
    if configs:
        try:
            if hasattr(configs, 'homepage_font_color') and getattr(configs, 'homepage_font_color'):
                home_font_color = getattr(configs, 'homepage_font_color')
        except Exception as e:
            pass
        try:
            if hasattr(configs, 'homepage_left_background') and getattr(configs, 'homepage_left_background'):
                homepage_left_background = getattr(configs, 'homepage_left_background')
        except Exception as e:
            pass
        try:
            if hasattr(configs, 'homepage_right_background') and getattr(configs, 'homepage_right_background'):
                homepage_right_background = getattr(configs, 'homepage_right_background')
        except Exception as e:
            pass

    from TEKDB.settings import RECORD_ICONS

    return {
        'proj_logo_text': project_logo_text,
        'proj_text_placement': project_text_placement,
        'proj_css': proj_css,
        'proj_icons': proj_icons,
        'proj_image_select': project_image_select,
        'home_image_attribution': home_image_attribution,
        'home_font_color': home_font_color,
        'homepage_left_background': homepage_left_background,
        'homepage_right_background': homepage_right_background,
        'map_pin': RECORD_ICONS['map_pin'],
        'map_pin_selected': RECORD_ICONS['map_pin_selected']
    }