# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-25 01:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20171225_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsout',
            name='bank_acc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.bankAccountDetails'),
        ),
    ]