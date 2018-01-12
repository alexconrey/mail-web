from django import forms

from django.forms import ModelForm

from models import Mailbox, Alias

class CreateMailboxForm(ModelForm):
	class Meta:
		model = Mailbox
		fields = ['name', 'password', 'quota', 'is_active', 'is_readonly', 'domain']

class CreateAliasForm(ModelForm):
	class Meta:
		model = Alias
		fields = ['name', 'domain', 'to_mailbox']
