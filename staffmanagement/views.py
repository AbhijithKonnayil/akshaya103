from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from staffmanagement.models import staffDetails
from django.http import Http404, HttpResponseRedirect
from .forms import staffDetailsForm, staffRegForm, dateSelectionForm
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils import formats
from django.utils.timezone import now
from django.conf import settings

# Create your views here.
def staffManagement(request,date):
	allUsers = User.objects.all()
	allUserDetails = staffDetails.objects.all()
	userlist=zip(allUsers,allUserDetails)
	if request.method == 'POST':
		form = staffRegForm(request.POST,request.FILES)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			mob = form.cleaned_data['mob']
			address = form.cleaned_data['address']
			email = form.cleaned_data['email']
			profile_photo = form.cleaned_data['profile_photo']
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
			staffD.profile_photo = profile_photo
			staffD.save()       	
        	context={'form':form,'userlist':userlist,'date':date,'root':settings.BASE_DIR}
		return render(request,'staffmanagement/staffDetailsEntry.html',context)
	else:
		form = staffRegForm()
	return render(request,'staffmanagement/staffDetailsEntry.html',{'userlist':userlist,'form':form,'allUsers':allUsers,'date':date,'root':settings.BASE_DIR})


def dashboard(request,date):

	return render(request,'staffmanagement/dashboard.html',{'date':date})

def selectDate(request):
	if request.method == 'POST':
		form = dateSelectionForm(request.POST)
		if form.is_valid():
			d=form.cleaned_data['date']
			da = d.strftime("%Y-%m-%d")
			return render(request,'staffmanagement/dashboard.html',{'form':form,'date':da})
	else:
		form = dateSelectionForm()
		return render(request,'staffmanagement/dateselect.html',{'form':form,})

