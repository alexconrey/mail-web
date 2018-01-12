# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, RedirectView

from models import Domain, ForwardDomain

def index(request):
	return render(request, 'domains/index.html', {})

def ListDomains(request):
	domain_list = Domain.objects.all().values()
	
	context = {'domain_list': domain_list}
	
	
	return render(request, 'domains/list_domains.html', context)
