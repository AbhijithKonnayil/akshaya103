# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffmanagement', '0004_auto_20171107_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetails',
            name='profile_photo',
            field=models.ImageField(upload_to=''),
        ),
    ]