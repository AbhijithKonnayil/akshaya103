from django import forms
from accounts.models import  bankAccountDetails, recieptDetail, recieptDetailsOut
import datetime

#set the choices (select options) of the reciept


class accountsInForm(forms.Form):
	reciept=forms.ModelChoiceField(queryset=recieptDetail.objects.all(), widget = forms.Select(attrs = {'class':"form-control",'onchange' : "myFunction();" "findTotal();" "creditField();",}),required=True)
	bank_acc=forms.ModelChoiceField(queryset=bankAccountDetails.objects.all(),widget = forms.Select(attrs = {'class':"form-control",}),required=False)
	payment_fees=forms.FloatField(initial=0,widget = forms.TextInput(attrs = {'class':"form-control",'onblur' : "findTotal();""creditField();",}),required=False)
	service_fees=forms.FloatField(initial=0, widget = forms.TextInput(attrs = {'class':"form-control",'onblur' : "findTotal();""creditField();",}),required=True)
	customer_name=forms.CharField(max_length=50,widget = forms.TextInput(attrs = {'class':"form-control",}),required=False)
	username=forms.CharField(max_length=50,widget = forms.TextInput(attrs = {'class':"form-control",}),required=False)
	password=forms.CharField(max_length=50,widget = forms.TextInput(attrs = {'class':"form-control",}),required=False)
	contact_no=forms.CharField(max_length=10,widget = forms.TextInput(attrs = {'class':"form-control",}),required=False)
	remark=forms.CharField(max_length=200,widget = forms.TextInput(attrs = {'class':"form-control",}),required=False)
	service_on_credit = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs ={'onchange':"creditField();",}))
	rec_amount = forms.FloatField(initial=0,required=False,widget = forms.TextInput(attrs={'class':"form-control",'onblur': "fillDummyValue();" "creditValidation();"}))
	trans_id = forms.CharField(widget=forms.HiddenInput(),required=False,initial=-1)

class accountsOutForm(forms.Form):
	reciept=forms.ModelChoiceField(queryset=recieptDetailsOut.objects.all(), widget = forms.Select(attrs = {'class':"form-control",'onchange' : "assDetails();" "findTotal();",}),required=True)
	bank_acc=forms.ModelChoiceField(queryset=bankAccountDetails.objects.all(),widget = forms.Select(attrs = {'class':"form-control",}),required=False)
	charge=forms.FloatField(initial=0,widget = forms.TextInput(attrs = {'class':"form-control",'onblur' : "findTotal();",}),required=True)
	remark=forms.CharField(max_length=200,widget = forms.TextInput(attrs = {'class':"form-control"}),required=False)

class accountsEditForm(forms.Form):
	rec_amount = forms.FloatField(initial=0,required=False,widget = forms.TextInput(attrs={'onblur':"creditValidation()"}))
	trans_id = forms.CharField(widget=forms.HiddenInput())

class recieptDetailsForm(forms.Form):
	reciept_title=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class':"form-control"}))
	service_fees=forms.FloatField(required=True,widget=forms.TextInput(attrs={'class':"form-control"}))
	fees_associated = forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={'onchange':"printAssBanks()"}))
	ass_bank_acc=forms.ModelChoiceField(queryset=bankAccountDetails.objects.all(), widget = forms.Select(attrs={'class':"form-control"}),required=False)
	ass_fees = forms.FloatField(required=False,widget=forms.TextInput(attrs={'class':"form-control"}))

class recieptDetailsOutForm(forms.Form):
	reciept_title=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class':"form-control"}))
	charge=forms.FloatField(required=True,widget=forms.TextInput(attrs={'class':"form-control"}))
	ass_bank_acc=forms.ModelChoiceField(queryset=bankAccountDetails.objects.all(), widget = forms.Select(attrs={'class':"form-control"}),required=False)

class bankAccountDetailsForm(forms.Form):
	bank_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':"form-control"}),required=True)
	opening_balance = forms.FloatField(widget=forms.TextInput(attrs={'class':"form-control"}),required=True)
	opening_balance_date = forms.DateField(widget=forms.DateInput(attrs={'type':"date"}),initial=datetime.date.today,required=True)
	margin_amount = forms.FloatField(widget=forms.TextInput(attrs={'class':"form-control"}),required=True)
class bankRechargeForm(forms.Form):
	bank=forms.ModelChoiceField(queryset=bankAccountDetails.objects.all(), widget = forms.Select(attrs={'class':"form-control"}),required=True)
	amount=forms.FloatField(widget=forms.TextInput(attrs={'class':"form-control"}),required=True)
				

report_type_options=(('monthwise','Month wise'),('receiptwise','Receipt wise'))
class reportTypeForm(forms.Form):
	report_type=forms.ChoiceField(report_type_options, widget=forms.Select(attrs={'class':"form-control"}))
	db =  forms.CharField(widget=forms.HiddenInput(),required=False,initial='accountsin')
