# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Domain, ForwardDomain
# Register your models here.

admin.site.register(Domain)
admin.site.register(ForwardDomain)

