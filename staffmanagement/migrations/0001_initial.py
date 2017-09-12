# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staffDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=20, verbose_name=(('admin', 'Admmin'), ('operator', 'Operator')))),
                ('email', models.CharField(max_length=20)),
                ('mob', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
