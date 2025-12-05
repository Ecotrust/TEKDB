from django.test import TestCase, RequestFactory, override_settings
from TEKDB.context_processors import search_settings


class TestSearchSettingsContextProcessor(TestCase):
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
            context = search_settings(request)

        self.assertIn("MIN_SEARCH_RANK", context)
        self.assertIn("MIN_SEARCH_SIMILARITY", context)
        self.assertEqual(context["MIN_SEARCH_RANK"], 0.01)
        self.assertEqual(context["MIN_SEARCH_SIMILARITY"], 0.1)

    @override_settings()
    def test_search_settings_missing_in_settings(self):
        from django.conf import settings

        del settings.MIN_SEARCH_RANK
        del settings.MIN_SEARCH_SIMILARITY
        request = self.factory.get("/")
        context = search_settings(request)
        self.assertIn("MIN_SEARCH_RANK", context)
        self.assertIn("MIN_SEARCH_SIMILARITY", context)
        self.assertEqual(context["MIN_SEARCH_RANK"], 0.01)  # Default
        self.assertEqual(context["MIN_SEARCH_SIMILARITY"], 0.1)  # Default

    @override_settings(MIN_SEARCH_RANK=0.05, MIN_SEARCH_SIMILARITY=0.2)
    def test_search_settings_from_settings(self):
        request = self.factory.get("/")
        context = search_settings(request)
        self.assertIn("MIN_SEARCH_RANK", context)
        self.assertIn("MIN_SEARCH_SIMILARITY", context)
        self.assertEqual(context["MIN_SEARCH_RANK"], 0.05)
        self.assertEqual(context["MIN_SEARCH_SIMILARITY"], 0.2)

    def test_search_settings_configs_overrides_settings(self):
        from configuration.models import Configuration

        Configuration.objects.create(min_search_rank=0.03, min_search_similarity=0.15)

        request = self.factory.get("/")
        context = search_settings(request)
        self.assertIn("MIN_SEARCH_RANK", context)
        self.assertIn("MIN_SEARCH_SIMILARITY", context)
        self.assertEqual(context["MIN_SEARCH_RANK"], 0.03)
        self.assertEqual(context["MIN_SEARCH_SIMILARITY"], 0.15)

    @override_settings(
        MIN_SEARCH_RANK=0.05,
    )
    def test_search_settings_configs_missing_search_rank(self):
        from configuration.models import Configuration

        Configuration.objects.create(min_search_rank=None, min_search_similarity=0.2)

        request = self.factory.get("/")
        context = search_settings(request)
        self.assertIn("MIN_SEARCH_RANK", context)
        self.assertIn("MIN_SEARCH_SIMILARITY", context)
        self.assertEqual(context["MIN_SEARCH_RANK"], 0.05)  # From settings
        self.assertEqual(context["MIN_SEARCH_SIMILARITY"], 0.2)  # From config


class TestAddMapDefaultContextProcessor(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @override_settings(
        DATABASE_GEOGRAPHY={
            "default_lon": 13839794,
            "default_lat": 5171449,
            "default_zoom": 5,
        }
    )
    def test_add_map_default_context(self):
        from TEKDB.context_processors import add_map_default_context

        request = self.factory.get("/")
        context = add_map_default_context(request)
        self.assertIn("default_lon", context)
        self.assertIn("default_lat", context)
        self.assertIn("default_zoom", context)
        self.assertEqual(context["default_lat"], 5171449)
        self.assertEqual(context["default_lon"], 13839794)
        self.assertEqual(context["default_zoom"], 5)

    def test_add_map_default_context_override_settings_with_configs(self):
        from configuration.models import Configuration
        from django.contrib.gis.geos import Polygon
        from TEKDB.context_processors import add_map_default_context

        Configuration.objects.create(
            geometry=Polygon.from_bbox([2000000, 1000000, 3000000, 2000000])
        )

        request = self.factory.get("/")
        context = add_map_default_context(request)
        self.assertIn("map_extent", context)
        self.assertEqual(context["map_extent"], [2000000, 1000000, 3000000, 2000000])
