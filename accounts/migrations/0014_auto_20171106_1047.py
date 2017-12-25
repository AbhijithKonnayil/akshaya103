# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-06 10:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20171106_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccountdetails',
            name='opening_balance',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='bankaccountdetails',
            name='opening_balance_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]