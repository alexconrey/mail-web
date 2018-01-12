from django.conf.urls import *

from domains import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^list/?$', views.ListDomains, name='list_domains'),
]
