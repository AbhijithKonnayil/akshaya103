# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 02:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffmanagement', '0005_auto_20171223_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
