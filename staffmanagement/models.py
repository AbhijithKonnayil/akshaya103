# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

designation_choice = (('admin','Admmin'),('operator','Operator'))
# Create your models here.
class staffDetails(models.Model):
	name = models.CharField(max_length=50)
	designation = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	mob = models.CharField(max_length=10)
	address = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class staffDetailsForm(ModelForm):
	Model = staffDetails
	fields = ('name','designation','email','mob','address')