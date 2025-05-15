from django.urls import path

from . import views

urlpatterns = [
	path('create', views.create, name='create'),
	path('forgot', views.forgot, name='forgot'),
    path('', views.index, name='index'),
]
	#url(r'^logout$', views.logout, name='logout'),
