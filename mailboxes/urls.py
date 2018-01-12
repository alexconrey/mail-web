from django.conf.urls import *

from mailboxes import views

urlpatterns = [
	url(r'^list/(?P<domain_name>(.*))/?$', views.ListMailboxesForDomain, name='list_mailboxes_for_domain'),
	url(r'^create/?$', views.CreateMailbox, name='create_mailbox'),
	url(r'^create/alias/?$', views.CreateAlias, name='create_alias'),
]
