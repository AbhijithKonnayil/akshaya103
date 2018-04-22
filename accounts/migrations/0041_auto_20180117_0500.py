# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-17 05:00
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_remove_jsontest_hsfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jsontest',
            name='field',
        ),
        migrations.AddField(
            model_name='jsontest',
            name='hsfield',
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
    ]
