from django import forms
import datetime
#from staffmanagement.models import staffDetails
designation_choice = (('admin','Admin'),('operator','Operator'))

class staffDetailsForm(forms.Form):
	name = forms.CharField(max_length=50)
	designation = forms.ChoiceField(designation_choice)
	email = forms.CharField(max_length=20)
	mob = forms.CharField(max_length=10)
	address = forms.CharField(max_length=100)
	
class staffRegForm(forms.Form):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50)
	designation = forms.ChoiceField(designation_choice)
	email = forms.CharField(max_length=50)
	mob = forms.CharField(max_length=10)
	address = forms.CharField(max_length=100)

class dateSelectionForm(forms.Form):
	date = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.date.today)
	
