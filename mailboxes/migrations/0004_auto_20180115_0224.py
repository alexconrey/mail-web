# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-15 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailboxes', '0003_auto_20180112_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alias',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailboxes_alias', to='domains.Domain'),
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailboxes_mailbox', to='domains.Domain'),
        ),
    ]
