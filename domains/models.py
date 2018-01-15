# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.now()

class Domain(models.Model):
	name = models.CharField(max_length=255)
	owner = models.ForeignKey(User, default=1, related_name='domains_domain')
	date_created = models.DateTimeField(default=datetime.now())
        date_modified = AutoDateTimeField(default=datetime.now())
	
	def __unicode__(self):
		return self.name

class ForwardDomain(models.Model):
	name = models.CharField(max_length=255)
	owner = models.ForeignKey(User, default=1, related_name='domains_forwardeddomain')
	date_created = models.DateTimeField(default=datetime.now())
        date_modified = AutoDateTimeField(default=datetime.now())
	to_domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='domains_forwardeddomain')

	def __unicode__(self):
		return self.name
