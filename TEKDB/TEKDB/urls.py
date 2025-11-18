"""TEKDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin

# urlpatterns = [
#    url(r'^admin/', admin.site.urls),
# url (r'^$', views.index, name='index'),
# ]

from django.conf.urls.static import static
from django.conf import settings

from django.urls import include, path, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from login import views as login_views

from . import views
from .custom_filebrowser import site as custom_filebrowser


urlpatterns = [
    # url(r'^login/', include('login.urls')),
    path("admin/filebrowser/", custom_filebrowser.urls),
    path("login/", login_views.login, name="login"),
    path("login_async/", login_views.login_async, name="login_async"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("tinymce/", include("tinymce.urls")),
    path("accounts/", include("django_registration.backends.one_step.urls")),
    re_path(r"^admin/", admin.site.urls),
    path("nested_admin/", include("nested_admin.urls")),
    re_path(r"^tekdb/(?P<model_name>\w+)/(?P<id>\w+)/get_related$", views.get_related),
    path(
        "citation_autocomplete/",
        views.CitationAutocompleteView.as_view(),
        name="select2_fk_citation",
    ),
    path("export_database/", views.ExportDatabase, name="export_database"),
    path("import_database/", views.ImportDatabase, name="import_database"),
    path(
        "medium_autocomplete/",
        views.MediaAutocompleteView.as_view(),
        name="select2_fk_media",
    ),
    path(
        "place_autocomplete/",
        views.PlaceAutocompleteView.as_view(),
        name="select2_fk_place",
    ),
    path(
        "place_resource_autocomplete/",
        views.PlaceResourceAutocompleteView.as_view(),
        name="select2_fk_placeresource",
    ),
    path(
        "resource_autocomplete/",
        views.ResourceAutocompleteView.as_view(),
        name="select2_fk_resource",
    ),
    path(
        "resource_activity_autocomplete/",
        views.ResourceActivityAutocompleteView.as_view(),
        name="select2_fk_resourceactivity",
    ),
    path("", include("explore.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
