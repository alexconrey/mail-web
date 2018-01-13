from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

from user_management import 
urlpatterns = [
	url(r'^$', views.ListAllDomains, name='index'),
	url(r'^create/?$', views.CreateLocalDomain, name='create_domain'),
	url(r'^create/local/?$', views.CreateLocalDomain, name='create_local_domain'),
	url(r'^create/forward/?$', views.CreateForwardDomain, name='create_forward_domain'),
	url(r'^list/?$', views.ListAllDomains, name='list_domains'),
	url(r'^list/all/?$', views.ListAllDomains, name='list_all_domains'),
	url(r'^list/local/?$', views.ListLocalDomains, name='list_local_domains'),
	url(r'^list/forward/?$', views.ListForwardDomains, name='list_forward_domains'),
]o


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
