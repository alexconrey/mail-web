# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create your models here.
class Mailbox(models.Model):
        name = models.CharField(max_length=32)
        password = models.CharField(max_length=256)
        domain = models.ForeignKey('domains.Domain', on_delete=models.CASCADE)
        quota = models.IntegerField(default=0)
        is_active = models.BooleanField(default=True)
        is_readonly = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True, blank=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True)

        def __unicode__(self):
                return self.name + '@' + self.domain.name
	class Meta:
		verbose_name = 'Mailbox'
		verbose_name_plural = 'Mailboxes'


class Alias(models.Model):
        name = models.CharField(max_length=255)
        domain = models.ForeignKey('domains.Domain', on_delete=models.CASCADE)
        to_mailbox = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

        def __unicode__(self):
                return self.name + '@' + self.domain.name
	
	class Meta:
		verbose_name = 'Alias'
		verbose_name_plural = 'Aliases'

