# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='forwarddomain',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
