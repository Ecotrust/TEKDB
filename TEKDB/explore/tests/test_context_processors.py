from django.test import TestCase, RequestFactory, override_settings
from explore.context_processors import explore_context


class TestExploreContext(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_search_settings_no_settings(self):
        from unittest import mock
        import builtins

        request = self.factory.get("/")

        real_import = builtins.__import__

        def mock_import(name, globals=None, locals=None, fromlist=(), level=0):
            if (
                name == "django.conf"
                or name.startswith("django.conf")
                or name == "TEKDB"
            ):
                raise ImportError("Mock missing settings module")
            return real_import(name, globals, locals, fromlist, level)

        with mock.patch("builtins.__import__", side_effect=mock_import):
            context = explore_context(request)

        self.assertIn("proj_logo_text", context)
        self.assertIn("proj_text_placement", context)

    @override_settings(
        PROJ_LOGO_TEXT="",
        PROJ_CSS={},
        PROJ_ICONS={},
        PROJ_IMAGE_SELECT="",
        PROJ_IMAGE_ATTR="",
        HOME_FONT_COLOR="#FFFFFF",
        HOME_LEFT_BACKGROUND="#000000",
        HOME_RIGHT_BACKGROUND="#000000",
        MEDIA_ROOT="/media/",
        MEDIA_URL="/media/",
    )
    def test_explore_context_with_default_values(self):
        request = self.factory.get("/")
        context = explore_context(request)

        # Assertions for default values
        self.assertEqual(context["proj_logo_text"], "ITK")
        self.assertEqual(context["proj_text_placement"], "default")
        self.assertEqual(context["proj_css"]["primary_a"], "#8f371c")
        self.assertEqual(
            context["proj_icons"]["logo"], "/static/explore/img/logos/logo_weave.svg"
        )
        self.assertEqual(
            context["proj_image_select"],
            "/static/explore/img/homepage/5050508427_ec55eed5f4_o.jpg",
        )
        self.assertEqual(
            context["home_image_attribution"],
            'Image courtesy of <a href="https://www.flickr.com/photos/monteregina/5050508427" target="_blank">Monteregina</a> and used under <a href="https://creativecommons.org/licenses/by-nc-sa/2.0/" target="_blank">the CC BY-NC-SA 2.0 Licence</a>. No changes were made.',
        )
        self.assertEqual(context["home_font_color"], "#FFFFFF")
        self.assertEqual(context["homepage_left_background"], "#000000")
        self.assertEqual(context["homepage_right_background"], "#000000")
        self.assertEqual(
            context["map_pin"], "/static/explore/img/icons/explore_map_pin.svg"
        )
        self.assertEqual(
            context["map_pin_selected"],
            "/static/explore/img/icons/explore_map_pin_selected.svg",
        )

    @override_settings(
        PROJ_LOGO_TEXT="Custom Logo",
        PROJ_CSS={"primary_a": "#123456"},
        PROJ_ICONS={"logo": "/custom/logo.svg"},
        PROJ_IMAGE_SELECT="/custom/image.jpg",
        PROJ_IMAGE_ATTR="Custom Attribution",
        HOME_FONT_COLOR="#ABCDEF",
        HOME_LEFT_BACKGROUND="#123123",
        HOME_RIGHT_BACKGROUND="#321321",
        MEDIA_ROOT="/media/",
        MEDIA_URL="/media/",
    )
    def test_explore_context_with_custom_settings(self):
        request = self.factory.get("/")
        context = explore_context(request)

        # Assertions for custom settings
        self.assertEqual(context["proj_logo_text"], "Custom Logo")
        self.assertEqual(context["proj_css"]["primary_a"], "#123456")
        self.assertEqual(context["proj_icons"]["logo"], "/custom/logo.svg")
        self.assertEqual(context["proj_image_select"], "/custom/image.jpg")
        self.assertEqual(context["home_image_attribution"], "Custom Attribution")
        self.assertEqual(context["home_font_color"], "#ABCDEF")
        self.assertEqual(context["homepage_left_background"], "#123123")
        self.assertEqual(context["homepage_right_background"], "#321321")
        self.assertEqual(
            context["map_pin"], "/static/explore/img/icons/explore_map_pin.svg"
        )
        self.assertEqual(
            context["map_pin_selected"],
            "/static/explore/img/icons/explore_map_pin_selected.svg",
        )

    @override_settings(
        PROJ_LOGO_TEXT="",
        PROJ_CSS={},
        PROJ_ICONS={},
        MEDIA_ROOT="/media/",
        MEDIA_URL="/media/",
    )
    def test_explore_context_with_configuration_model(self):
        from configuration.models import Configuration

        Configuration.objects.create(
            preferredInitialism="Config Logo",
            preferredInitialismPlacement="top",
            homepage_image_attribution="Config Attribution",
            homepage_font_color="#FFFFFF",
            homepage_left_background="#000000",
            homepage_right_background="#467011",
        )

        request = self.factory.get("/")
        context = explore_context(request)

        # Assertions for configuration model
        self.assertEqual(context["proj_logo_text"], "Config Logo")
        self.assertEqual(context["proj_text_placement"], "top")
        self.assertEqual(context["home_image_attribution"], "Config Attribution")
        self.assertEqual(context["home_font_color"], "#FFFFFF")
        self.assertEqual(context["homepage_left_background"], "#000000")
        self.assertEqual(context["homepage_right_background"], "#467011")
