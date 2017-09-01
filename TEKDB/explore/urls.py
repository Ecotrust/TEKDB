from django.conf.urls import url, include

from . import views

explore_patterns = [
    url(r'^$', views.explore),
    url(r'^(?P<model_type>\w+)/$', views.get_by_model_type),
    url(r'^(?P<model_type>\w+)/(?P<id>\w+)/$', views.get_by_model_id),
]

urlpatterns = [
	url(r'^about/', views.about),
    url(r'^help/', views.help),
    url(r'^search/', views.search),
    url(r'^query/$', views.query),
    url(r'^explore$', views.explore),
    url(r'^explore/', include(explore_patterns)),
    url(r'^export/$', views.download),
    url(r'^$', views.home),
]
	#url(r'^logout$', views.logout, name='logout'),
