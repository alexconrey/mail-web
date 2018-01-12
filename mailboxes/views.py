# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import Mailbox, Alias
from forms import CreateMailboxForm

from domains.models import Domain


# Create your views here.

def ListMailboxesForDomain(request, domain_name):
	domain = Domain.objects.get(name=domain_name)

	mailbox_list = Mailbox.objects.filter(domain_id=domain.id).values()
	alias_list = Alias.objects.filter(domain_id=domain.id).values()

	context = {'title': 'Mailboxes for {0}'.format(domain.name), 'mailbox_list': mailbox_list, 'alias_list': alias_list}

	return render(request, 'mailboxes/table.html', context)


def CreateMailbox(request):
	if request.method == "POST":
		form = CreateMailboxForm(request.POST)
		if form.is_valid():
			form.save()
			dname = Domain.objects.get(pk=request.POST['domain']).name
			return redirect(ListMailboxesForDomain, domain_name=dname)
	else:
		form = CreateMailboxForm()
	
	return render(request, 'mailboxes/create.html', {'form': form, 'title': 'Create Mailbox'})

def CreateAlias(request):
	if request.method == "POST":
		form = CreateAliasForm(request.POST)
		if form.is_valid():
			form.save()
			return ListMailboxesForDomain(request)
	else:
		form = CreateAliasForm()

	return render(request, 'mailboxes/create.html', {'form': form, 'title': 'Create Alias'})

