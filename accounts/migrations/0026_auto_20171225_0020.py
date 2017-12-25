# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-25 00:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20171223_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsin',
            name='contact_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='accountsin',
            name='customer_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='accountsin',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='accountsin',
            name='payment_fees',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accountsin',
            name='service_fees',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accountsin',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountsin',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='accountsout',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
