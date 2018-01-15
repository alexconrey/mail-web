# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.now()


# Create your models here.
class Mailbox(models.Model):
        name = models.CharField(max_length=32)
        password = models.CharField(max_length=256)
        domain = models.ForeignKey('domains.Domain', on_delete=models.CASCADE, related_name='mailboxes_mailbox')
        quota = models.IntegerField(default=0)
        is_active = models.BooleanField(default=True)
        is_readonly = models.BooleanField(default=False)
      	date_created = models.DateTimeField(default=datetime.now())
        date_modified = AutoDateTimeField(default=datetime.now())

	class Meta:
		verbose_name = 'Mailbox'
		verbose_name_plural = 'Mailboxes'

        def __unicode__(self):
                return self.name + '@' + self.domain.name


class Alias(models.Model):
        name = models.CharField(max_length=255)
        domain = models.ForeignKey('domains.Domain', on_delete=models.CASCADE, related_name='mailboxes_alias')
        to_mailbox = models.CharField(max_length=255)
       	date_created = models.DateTimeField(default=datetime.now())
        date_modified = AutoDateTimeField(default=datetime.now())

	
	class Meta:
		verbose_name = 'Alias'
		verbose_name_plural = 'Aliases'

        def __unicode__(self):
                return self.name + '@' + self.domain.name

