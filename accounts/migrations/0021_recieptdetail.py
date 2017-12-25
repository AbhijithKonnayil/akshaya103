# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20171223_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='recieptDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ass_fees', models.FloatField(blank=True, default=0, max_length=10)),
                ('reciept_title', models.CharField(max_length=50)),
                ('service_fees', models.FloatField(blank=True, default=0, max_length=10)),
                ('ass_bank_acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bankAccountDetails')),
            ],
        ),
    ]
