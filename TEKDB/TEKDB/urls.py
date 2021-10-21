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
#from django.conf.urls import url
#from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#	url (r'^$', views.index, name='index'),
#]

from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from login import views as login_views
from dal import autocomplete

from . import views
from . import models

urlpatterns = [
    # url(r'^login/', include('login.urls')),
    url(r'^login/$', login_views.login, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^tekdb/(?P<model_name>\w+)/(?P<id>\w+)/get_related$', views.get_related),
    url('citation_autocomplete/$', views.CitationAutocompleteView.as_view(), name='select2_fk_citation',),
    url('media_autocomplete/$', views.MediaAutocompleteView.as_view(), name='select2_fk_media',),
    url('place_autocomplete/$', views.PlaceAutocompleteView.as_view(), name='select2_fk_place',),
    url('place_resource_autocomplete/$', views.PlaceResourceAutocompleteView.as_view(), name='select2_fk_placeresource',),
    url('resource_autocomplete/$', views.ResourceAutocompleteView.as_view(), name='select2_fk_resource',),
    url('resource_activity_autocomplete/$', views.ResourceActivityAutocompleteView.as_view(), name='select2_fk_resourceactivity',),
    url(r'', include('explore.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
