# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-16 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_accountsout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccountdetails',
            name='bank_branch',
        ),
    ]
