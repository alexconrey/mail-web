# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import views as auth_views

# Create your views here.
def Welcome(request):
	return render(request, 'user_management/welcome.html', {})
