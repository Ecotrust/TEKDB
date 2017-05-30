from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^create$', views.create, name='create'),
	url(r'^forgot$', views.forgot, name='forgot'),
    url(r'^$', views.index, name='index'),
]
	#url(r'^logout$', views.logout, name='logout'),
