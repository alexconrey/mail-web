from django.conf.urls import *

from domains import views

urlpatterns = [
	url(r'^$', views.ListAllDomains, name='index'),
	url(r'^create/?$', views.CreateLocalDomain, name='create_domain'),
	url(r'^create/local/?$', views.CreateLocalDomain, name='create_local_domain'),
	url(r'^create/forward/?$', views.CreateForwardDomain, name='create_forward_domain'),
	url(r'^list/?$', views.ListAllDomains, name='list_domains'),
	url(r'^list/all/?$', views.ListAllDomains, name='list_all_domains'),
	url(r'^list/local/?$', views.ListLocalDomains, name='list_local_domains'),
	url(r'^list/forward/?$', views.ListForwardDomains, name='list_forward_domains'),
]
