# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-17 02:36
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20180106_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='jsontest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]