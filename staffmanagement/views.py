from django.shortcuts import render
from staffmanagement.models import staffDetails
from django.http import Http404, HttpResponseRedirect
from .forms import staffDetailsForm, staffRegForm, dateSelectionForm
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils import formats
from django.utils.timezone import now

# Create your views here.
def staffManagement(request):
	allUsers = User.objects.all()
	if request.method == 'POST':
		form = staffRegForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			mob = form.cleaned_data['mob']
			address = form.cleaned_data['address']
			email = form.cleaned_data['email']
			staffD = staffDetails()
			if form.cleaned_data['designation'] == 'admin':
				staff = User.objects.create_superuser(username, email, password)
			else:
				staff = User.objects.create_user(username, email, password,is_staff=True)
			staff.first_name = first_name
			staff.last_name = last_name
			staff.save()
			staffD.user = username
			staffD.address = address
			staffD.mob = mob
			#staffD.save()
		return HttpResponseRedirect('add')
	else:
		form = staffRegForm()
	return render(request,'staffmanagement/staffDetailsEntry.html',{'form':form,'allUsers':allUsers})


def dashboard(request,date):

	return render(request,'staffmanagement/dashboard.html',{'date':date})

def selectDate(request):
	if request.method == 'POST':
		form = dateSelectionForm(request.POST)
		if form.is_valid():
			d=form.cleaned_data['date']
			return render(request,'staffmanagement/dashboard.html',{'form':form,'date':d})
	#else:
	form = dateSelectionForm()
	return render(request,'staffmanagement/dateselect.html',{'form':form,})

