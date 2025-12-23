from django.urls import include, path, re_path
from .API import views as api_views

from . import views

explore_patterns = [
    path("", views.explore),
    re_path(r"^(?P<model_type>\w+)/$", views.get_by_model_type),
    re_path(r"^(?P<model_type>\w+)/(?P<id>\w+)/$", views.get_by_model_id),
    re_path(r"^(?P<model_type>\w+)/(?P<id>\w+)/download$", views.download_media_file),
]

api_explore_patterns = [
    path("<str:model_type>/", api_views.ExploreByType.as_view()),
    path("<str:model_type>/<int:id>/", api_views.ExploreById.as_view()),
    path("<str:model_type>/<int:id>/download", api_views.DownloadMediaFile.as_view()),
]

export_patterns = [
    path("", views.download),
    re_path(
        r"^(?P<model_type>\w+)/(?P<id>\w+)/(?P<format>\w+)/$", views.export_by_model_id
    ),
]

urlpatterns = [
    re_path(r"^about/", views.about),
    re_path(r"^help/", views.help),
    re_path(r"^search/", views.search, name="search"),
    path("explore", views.explore),
    path("explore/", include(explore_patterns)),
    path("export", views.download),
    path("export/", include(export_patterns)),
    path("", views.home),
    # API endpoints (DRF)
    path("api/explore/", include(api_explore_patterns)),
    path("api/page/<str:name>/", api_views.PageContentSingle.as_view()),
    path("api/search/", api_views.ExploreSearch.as_view()),
    path("api/export/", api_views.Download.as_view()),
    path(
        "api/export/<str:model_type>/<int:id>/<str:format>/",
        api_views.ExportRecord.as_view(),
    ),
    path(
        "api/site-info/", api_views.SiteConfigurationAPIView.as_view(), name="site-info"
    ),
    path("api/csrf/", api_views.CsrfTokenAPIView.as_view(), name="csrf-token"),
]
# url(r'^logout$', views.logout, name='logout'),
