# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-15 02:24
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import domains.models


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0004_auto_20180113_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='domains_domain', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='forwarddomain',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 15, 2, 24, 33, 803674)),
        ),
        migrations.AlterField(
            model_name='forwarddomain',
            name='date_modified',
            field=domains.models.AutoDateTimeField(default=datetime.datetime(2018, 1, 15, 2, 24, 33, 803711)),
        ),
        migrations.AlterField(
            model_name='forwarddomain',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='domains_forwardeddomain', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='forwarddomain',
            name='to_domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains_forwardeddomain', to='domains.Domain'),
        ),
    ]