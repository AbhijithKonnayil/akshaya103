from django import forms
from staffmanagement.models import staffDetails
designation_choice = (('admin','Admin'),('operator','Operator'))

class staffDetailsForm(forms.Form):
	name = forms.CharField(max_length=50)
	designation = forms.ChoiceField(designation_choice)
	email = forms.CharField(max_length=20)
	mob = forms.CharField(max_length=10)
	address = forms.CharField(max_length=100)

	def __str__(self):
		return self.name