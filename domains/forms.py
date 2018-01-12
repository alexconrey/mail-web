from django import forms

from django.forms import ModelForm

from models import Domain

class CreateDomainForm(ModelForm):
	class Meta:
		model = Domain
		fields = ['name']

