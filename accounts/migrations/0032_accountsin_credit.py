# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_accountsin_amount_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountsin',
            name='credit',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
