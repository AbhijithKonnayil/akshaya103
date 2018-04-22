# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-21 11:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffmanagement', '0009_remove_staffdetails_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
