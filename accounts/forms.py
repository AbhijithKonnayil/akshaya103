from django import forms
from accounts.models import  bankAccountDetails, recieptDetail
import datetime

#set the choices (select options) of the reciept


class accountsInForm(forms.Form):
	reciept=forms.ModelChoiceField(queryset=recieptDetail.objects.all(), widget = forms.Select(attrs = {'onchange' : "myFunction();" "findTotal();",}),required=True)
	bank_acc=forms.ModelChoiceField(queryset=bankAccountDetails.objects.all(),required=False)
	payment_fees=forms.FloatField(initial=0,widget = forms.TextInput(attrs = {'onblur' : "findTotal();",}),required=False)
	service_fees=forms.FloatField(initial=0, widget = forms.TextInput(attrs = {'onblur' : "findTotal();",}),required=True)
	customer_name=forms.CharField(max_length=50,required=False)
	username=forms.CharField(max_length=50,required=False)
	password=forms.CharField(max_length=50,required=False)
	contact_no=forms.CharField(max_length=10,required=False)
	remark=forms.CharField(max_length=200,required=False)

class recieptDetailsForm(forms.Form):
	reciept_title=forms.CharField(max_length=50,required=True)
	service_fees=forms.FloatField(required=True)
	fees_associated = forms.ChoiceField(required=True, initial='yes' ,choices=[('yes','Yes'),('no','No')], widget=forms.RadioSelect(attrs ={'onchange':"printAssBanks();",}))
	ass_bank_acc=forms.ModelChoiceField(queryset=bankAccountDetails.objects.all(), widget = forms.Select(attrs={}),required=False)
	ass_fees = forms.FloatField(required=False)

class bankAccountDetailsForm(forms.Form):
	bank_name = forms.CharField(max_length=50,required=True)
	opening_balance = forms.FloatField(required=True)
	opening_balance_date = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.date.today,required=True)

class accountsOutForm(forms.Form):
	reciept=forms.CharField(max_length=50,required=True)
	bank_acc=forms.ModelChoiceField(queryset=bankAccountDetails.objects.all(),required=False)
	charge=forms.FloatField(initial=0,widget = forms.TextInput(attrs = {'onblur' : "findTotal();",}),required=True)
	remark=forms.CharField(max_length=200,required=False)	
