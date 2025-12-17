from django.urls import include, path, re_path
from rest_framework import routers
from .API import views as api_views

from . import views

router = routers.DefaultRouter()
router.register(r"pagecontent", api_views.PageContentViewSet)

explore_patterns = [
    path("", views.explore),
    re_path(r"^(?P<model_type>\w+)/$", views.get_by_model_type),
    re_path(r"^(?P<model_type>\w+)/(?P<id>\w+)/$", views.get_by_model_id),
    re_path(r"^(?P<model_type>\w+)/(?P<id>\w+)/download$", views.download_media_file),
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
    # API endpoints (DRF)
    path("api/pagecontent/", include(router.urls)),
    re_path(r"^api/page/(?P<name>\w+)/$", api_views.PageContentSingle.as_view()),
    path("api/search/", api_views.ExploreSearch.as_view()),
    re_path(r"^api/record/(?P<model_type>\w+)/(?P<id>\w+)/$", api_views.RecordDetail.as_view()),
    re_path(r"^api/export/(?P<model_type>\w+)/(?P<id>\w+)/(?P<format>\w+)/$", api_views.ExportRecord.as_view()),
    re_path(r"^api/media/(?P<model_type>\w+)/(?P<id>\w+)/download$", api_views.DownloadMediaFile.as_view()),
    path("", views.home),
]
# url(r'^logout$', views.logout, name='logout'),
