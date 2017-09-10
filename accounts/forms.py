from django import forms
from accounts.models import recieptDetails

#set the choices (select options) of the reciept
reciept_types=()
choice = recieptDetails.objects.all()
for a in choice:
	d=(str(a.reciept_title),str(a.reciept_title))
	reciept_types=reciept_types+(d,)

class accountsInForm(forms.Form):
	reciept=forms.ChoiceField(reciept_types, widget = forms.Select(attrs = {'onchange' : "myFunction();",}))
	bank_acc=forms.CharField(max_length=50)
	payment_fees=forms.FloatField()
	service_fees=forms.FloatField()
	customer_name=forms.CharField(max_length=50)
	username=forms.CharField(max_length=50)
	password=forms.CharField(max_length=50)
	contact_no=forms.CharField(max_length=10)
	remark=forms.CharField(max_length=200)
