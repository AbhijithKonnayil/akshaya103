# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-04 02:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20171103_2202'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bankAccountDetails',
        ),
    ]