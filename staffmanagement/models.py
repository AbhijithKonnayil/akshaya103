# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

designation_choice = (('admin','Admmin'),('operator','Operator'))
# Create your models here.

class staffDetails(models.Model):
	user = models.CharField(max_length=50,null=True)
	mob = models.CharField(max_length=10,)
	address = models.CharField(max_length=100)
	profile_photo = models.ImageField(upload_to='',)

	def __str__(self):
		return self.user
"""
class staffDetailsForm(ModelForm):
	class Meta:
		model = staffDetails
		fields = ('user','mob','address','profile_photo')

"""