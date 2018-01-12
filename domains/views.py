# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, RedirectView

from models import Domain, ForwardDomain
from forms import CreateDomainForm, CreateForwardDomainForm

def ListAllDomains(request):
	local_domain_list = Domain.objects.all().values()
	forward_domain_list = ForwardDomain.objects.all().values()

	all_domain_list = [] 

	for domain in local_domain_list:
		all_domain_list.append(domain)
	
	for domain in forward_domain_list:
		all_domain_list.append(domain)

	context = {'title': 'All domains', 'domain_list': all_domain_list}

	return render(request, 'domains/table.html', context)

def ListLocalDomains(request):
	domain_list = Domain.objects.all().values()
	
	context = {'title': 'Local domains', 'domain_list': domain_list}
	
	return render(request, 'domains/table.html', context)

def ListForwardDomains(request):
	domain_list = ForwardDomain.objects.all().values()

	context = {'title': 'Forwarded Domains', 'domain_list': domain_list}

	return render(request, 'domains/table.html', context)

def CreateLocalDomain(request):
	if request.method == "POST":
		form = CreateDomainForm(request.POST)
		if form.is_valid():
			form.save()
			return ListAllDomains(request)
	else:
		form = CreateDomainForm()

	return render(request, 'domains/create_domain.html', {'form': form})

def CreateForwardDomain(request):
	if request.method == "POST":
		form = CreateForwardDomainForm(request.POST)
		if form.is_valid():
			form.save()
			return ListAllDomains(request)
	else:
		form = CreateForwardDomainForm()

	return render(request, 'domains/create_domain.html', {'form': form})
