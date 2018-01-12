# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mailbox(models.Model):
        name = models.CharField(max_length=32)
        password = models.CharField(max_length=256)
        domain = models.ForeignKey('domains.Domain', on_delete=models.CASCADE)
        quota = models.IntegerField(default=0)
        is_active = models.BooleanField(default=True)
        is_readonly = models.BooleanField(default=False)

        def __unicode__(self):
                return self.name + '@' + self.domain.name


class Alias(models.Model):
        name = models.CharField(max_length=255)
        domain = models.ForeignKey('domains.Domain', on_delete=models.CASCADE)
        to_mailbox = models.CharField(max_length=255)

        def __unicode__(self):
                return self.name + '@' + self.domain.name

