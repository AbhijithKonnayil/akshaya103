# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-17 03:51
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_auto_20180117_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsontest',
            name='hsfield',
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True),
        ),
    ]
