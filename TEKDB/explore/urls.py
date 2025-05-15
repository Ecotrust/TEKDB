from django.urls import include, path, re_path

from . import views

explore_patterns = [
    path('', views.explore),
    re_path(r'^(?P<model_type>\w+)/$', views.get_by_model_type),
    re_path(r'^(?P<model_type>\w+)/(?P<id>\w+)/$', views.get_by_model_id),
    re_path(r'^(?P<model_type>\w+)/(?P<id>\w+)/download$', views.download_media_file),
]

export_patterns = [
    path('', views.download),
    re_path(r'^(?P<model_type>\w+)/(?P<id>\w+)/(?P<format>\w+)/$', views.export_by_model_id),
]

urlpatterns = [
	re_path(r'^about/', views.about),
    re_path(r'^help/', views.help),
    re_path(r'^search/', views.search, name='search'),
    path('explore', views.explore),
    path('explore/', include(explore_patterns)),
    path('export', views.download),
    path('export/', include(export_patterns)),
    path('', views.home),
]
	#url(r'^logout$', views.logout, name='logout'),
