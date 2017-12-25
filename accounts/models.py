from django.db import models
from django.forms import ModelForm
import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User

class bankAccountDetails(models.Model):
	bank_name = models.CharField(max_length=50,null=False)
	opening_balance = models.FloatField(max_length=10, blank=False,null=False, default=0)
	opening_balance_date = models.DateField(default=datetime.date.today,null=False, blank=False)
	
	def __str__(self):
		return self.bank_name

class recieptDetail(models.Model):
	ass_fees = models.FloatField(max_length=10,default=0,blank=True)
	reciept_title = models.CharField(max_length=50,blank=False)
	ass_bank_acc = models.ForeignKey(bankAccountDetails,blank=True,null=True)
	service_fees = models.FloatField(max_length=10, default=0, blank=True)
	
	def __str__(self):
		return self.reciept_title

class accountsIn(models.Model):
	date=models.DateField(default=datetime.date.today)
	time=models.DateTimeField(auto_now_add=True)
	reciept=models.ForeignKey(recieptDetail,blank=False,null=False)
	bank_acc=models.ForeignKey(bankAccountDetails,blank=True,null=True)
	payment_fees=models.FloatField(blank=False,default=0,)
	service_fees=models.FloatField(blank=False,default=0,)
	customer_name=models.CharField(max_length=50, blank=True, null=True)
	username=models.CharField(max_length=50, blank=True, null=True)
	password=models.CharField(max_length=50, blank=True, null=True)
	contact_no=models.CharField(max_length=10, blank=True, null=True)
	total_fees=models.FloatField()
	remark=models.CharField(max_length=200,blank=True)
	staff=models.CharField(max_length=50)
	def __str__(self):
		return "Transation ID : " + str(self.id)

class accountsOut(models.Model):
	date=models.DateField(default=datetime.date.today)
	time=models.DateTimeField(auto_now_add=True)
	reciept=models.CharField(max_length=50,)
	bank_acc=models.ForeignKey(bankAccountDetails,null=True,blank=True)
	charge=models.FloatField(blank=False)
	remark=models.CharField(max_length=200,blank=True)
	staff=models.CharField(max_length=50)
	def __str__(self):
		return "Transation ID : "+ str(self.id) +" -> "+ self.reciept


## << MODEL FORMS >>##
"""
class accountsInForm(ModelForm):
	class Meta:
		model = accountsIn
		fields = ('reciept','bank_acc','payment_fees','service_fees','customer_name','username','password','contact_no','total_fees','remark')

class accountsOutForm(ModelForm):
	class Meta:
		model = accountsOut
		fields = ('reciept','bank_acc','charge','remark')

class recieptDetailsForm(ModelForm):
	class Meta:
		model = recieptDetail
		fields = ('reciept_title','ass_bank_acc','service_fees','ass_fees')

class bankAccountDetailsForm(ModelForm):
	class Meta:
		model = bankAccountDetails
		fields = ('bank_name','opening_balance','opening_balance_date')
	"""	