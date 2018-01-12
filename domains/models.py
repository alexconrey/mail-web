# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Domain(models.Model):
	name = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.name

class ForwardDomain(models.Model):
	name = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	to_domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.name
