from django.db import models
from django.forms import ModelForm
import datetime
from django.utils.timezone import now


class accountsIn(models.Model):
	date=models.DateField(default=datetime.date.today)
	time=models.DateTimeField(auto_now_add=True)
	reciept=models.CharField(max_length=100)
	bank_acc=models.CharField(max_length=50,blank=True)
	payment_fees=models.FloatField(blank=False)
	service_fees=models.FloatField(blank=False)
	customer_name=models.CharField(max_length=50, blank=False, null=False)
	username=models.CharField(max_length=50, blank=True)
	password=models.CharField(max_length=50, blank=True)
	contact_no=models.CharField(max_length=10, blank=False, null=True)
	total_fees=models.FloatField()
	remark=models.CharField(max_length=200,blank=True)
	staff=models.CharField(max_length=50)
	def __str__(self):
		return self.reciept +  ' ' + str(self.service_fees)

class accountsOut(models.Model):
	date=models.DateField(default=datetime.date.today)
	time=models.DateTimeField(auto_now_add=True)
	reciept=models.CharField(max_length=100)
	bank_acc=models.CharField(max_length=50,blank=True)
	charge=models.FloatField(blank=False)
	remark=models.CharField(max_length=200,blank=True)
	staff=models.CharField(max_length=50)
	def __str__(self):
		return self.reciept +  ' ' + str(self.charge)	

class recieptDetails(models.Model):
	reciept_title = models.CharField(max_length=50,)
	ass_bank_acc = models.CharField(max_length=50,)
	ass_bank_acc = models.CharField(max_length=50, null=True,blank=True)
	service_fees = models.FloatField(max_length=10, null=True,blank=True)
	def __str__(self):
		return self.reciept_title 

class bankAccountDetails(models.Model):
	bank_name = models.CharField(max_length=50,)
	bank_branch = models.CharField(max_length=50,)
	bank_acc_no = models.CharField(max_length=15,)
	acc_holder = models.CharField(max_length=50,)
	acc_holder_contactno = models.CharField(max_length=10,)
	balance = models.FloatField()
	def __str__(self):
		return self.bank_name

## << MODEL FORMS >>##

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
		model = recieptDetails
		fields = ('reciept_title','ass_bank_acc','service_fees')

class bankAccountDetailsForm(ModelForm):
	class Meta:
		model = bankAccountDetails
		fields = ('bank_name','bank_branch','bank_acc_no','acc_holder','acc_holder_contactno','balance')