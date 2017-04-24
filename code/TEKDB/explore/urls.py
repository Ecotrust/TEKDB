from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^about/', views.about),
    url(r'^help/', views.help),
    url(r'^$', views.home),
]
	#url(r'^logout$', views.logout, name='logout'),
