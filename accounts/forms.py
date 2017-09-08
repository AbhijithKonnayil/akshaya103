from django import forms

reciept_types = (
	('aadhar','Aadhar'),
	('egrats','E Grants')
	)

class accountsInForm(forms.Form):
	reciept=forms.CharField(max_length=100, widget=forms.Select(choices=reciept_types))
	bank_acc=forms.CharField(max_length=50)
	payment_fees=forms.FloatField()
	service_fees=forms.FloatField()
	customer_name=forms.CharField(max_length=50)
	username=forms.CharField(max_length=50)
	password=forms.CharField(max_length=50)
	contact_no=forms.CharField(max_length=10)
	remark=forms.CharField(max_length=200)
	