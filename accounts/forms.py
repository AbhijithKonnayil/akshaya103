from django import forms
from accounts.models import recieptDetails, bankAccountDetails
import datetime
#set the choices (select options) of the reciept
reciept_types=()
reciept_choice = recieptDetails.objects.all()
for a in reciept_choice:
	d=(str(a.reciept_title),str(a.reciept_title))
	reciept_types=reciept_types+(d,)

banks = ()
bank_choice = bankAccountDetails.objects.all()
for a in bank_choice:
	d=(str(a.bank_name),str(a.bank_name))
	banks=banks+(d,)


class accountsInForm(forms.Form):
	reciept=forms.ChoiceField(reciept_types, widget = forms.Select(attrs = {'onchange' : "myFunction();" "findTotal();",}))
	bank_acc=forms.ChoiceField(banks,)
	payment_fees=forms.FloatField(initial=0,widget = forms.TextInput(attrs = {'onblur' : "findTotal();",}))
	service_fees=forms.FloatField(initial=0, widget = forms.TextInput(attrs = {'onblur' : "findTotal();",}))
	customer_name=forms.CharField(max_length=50)
	username=forms.CharField(max_length=50)
	password=forms.CharField(max_length=50)
	contact_no=forms.CharField(max_length=10)
	remark=forms.CharField(max_length=200)

class recieptDetailsForm(forms.Form):
	reciept_title=forms.CharField(max_length=50)
	service_fees=forms.FloatField()
	fees_associated = forms.ChoiceField(required=True, initial='no' ,choices=[('yes','Yes'),('no','No')], widget=forms.RadioSelect(attrs ={'onchange':"printAssBanks();"}))
	ass_bank_acc=forms.ChoiceField(banks, widget = forms.Select(attrs={'class':"display-none"}))

class bankAccountDetailsForm(forms.Form):
	bank_name = forms.CharField(max_length=50,)
	opening_balance = forms.FloatField()
	opening_balance_date = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.date.today,)

class accountsOutForm(forms.Form):
	reciept=forms.CharField(max_length=50)
	bank_acc=forms.ChoiceField(banks,)
	charge=forms.FloatField(initial=0,widget = forms.TextInput(attrs = {'onblur' : "findTotal();",}))
	remark=forms.CharField(max_length=200)	
