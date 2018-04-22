from django import forms
import datetime
#from staffmanagement.models import staffDetails
designation_choice = (('admin','Admin'),('operator','Operator'))
db_choice = (('accountsin','Reciepts'),('accountsout','Expenditure'),('both','Both'))
class staffRegForm(forms.Form):
	first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':"form-control"}))
	last_name = forms.CharField(max_length=50,widget = forms.TextInput(attrs = {'class':"form-control"}))
	username = forms.CharField(max_length=50,widget = forms.TextInput(attrs = {'class':"form-control"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'onchange':"confirmPassword()",'class':"form-control"}))
	confirm_password =  forms.CharField(widget=forms.PasswordInput(attrs={'onchange':"confirmPassword()",'onblur':"confirmPassword2()",'class':"form-control"}),required=False)
	designation = forms.ChoiceField(designation_choice,widget = forms.Select(attrs = {'class':"form-control"}))
	email = forms.CharField(max_length=50,widget = forms.TextInput(attrs = {'class':"form-control"}))
	mob = forms.CharField(max_length=10,widget = forms.TextInput(attrs = {'class':"form-control"}))
	address = forms.CharField(max_length=100,widget = forms.TextInput(attrs = {'class':"form-control"}))
	#profile_photo = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':"form-control"}))
	user_id = forms.IntegerField(widget=forms.HiddenInput(),required=False,initial=-1)

class dateSelectionForm(forms.Form):
	date = forms.DateField(widget=forms.DateInput(attrs={'type':"date",'class':"form-control",'data-date-format':"DD MMMM YYYY"}),initial=datetime.date.today,)
	db =  forms.CharField(widget=forms.HiddenInput(),required=False,initial='accountsin')


	
