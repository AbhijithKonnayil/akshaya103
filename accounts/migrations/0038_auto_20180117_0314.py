# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-17 03:14
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_jsontest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsontest',
            name='field',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
