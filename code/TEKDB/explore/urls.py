from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^about/', views.about),
    url(r'^help/', views.help),
    url(r'^search/', views.search),
    url(r'^query/$', views.query),
    url(r'^explore/', views.explore),
    url(r'^$', views.home),
]
	#url(r'^logout$', views.logout, name='logout'),
