# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-24 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_auto_20180423_1444'),
    ]

    operations = [
        migrations.DeleteModel(
            name='json',
        ),
    ]
