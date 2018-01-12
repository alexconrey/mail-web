from django import forms

from django.forms import ModelForm

from models import Domain, ForwardDomain

class CreateDomainForm(ModelForm):
	class Meta:
		model = Domain
		fields = ['name']

class CreateForwardDomainForm(ModelForm):
	class Meta:
		model = ForwardDomain
		fields = ['name', 'to_domain']

