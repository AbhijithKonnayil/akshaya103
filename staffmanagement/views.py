from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from staffmanagement.models import staffDetails
from django.http import Http404, HttpResponseRedirect
from .forms import staffRegForm, dateSelectionForm
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
		print "\n post recived \n"
		form = staffRegForm(request.POST,request.FILES)
		if form.is_valid():
			print "\n valid form  \n"
			user_id = form.cleaned_data['user_id']
			print user_id
			if user_id == -1:
				print "\n id  \n", user_id
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
			elif user_id>0:
				print user_id,"  id \n\n"
				staff=User.objects.get(id=user_id)
				staffD = staffDetails.objects.get(user=staff.username)
				print staffD
				staff.first_name = form.cleaned_data['first_name']
				staff.last_name = form.cleaned_data['last_name']
				staff.username = form.cleaned_data['username']
				staff.set_password(form.cleaned_data['password'])
				staff.email = form.cleaned_data['email']
				staffD.mob = form.cleaned_data['mob']
				staffD.address = form.cleaned_data['address']
				staffD.user = staff.username


				if form.cleaned_data['designation'] == 'admin':
					staff.is_superuser = True
				else:
					staff.is_superuser = False
					staff.is_staff = True

				staffD.save()
				staff.save()
			form=staffRegForm()
        	context={'form':form,'userlist':userlist,'allUsers':allUsers,'date':date,'root':settings.BASE_DIR}
		return render(request,'staffmanagement/staffDetailsEntry.html',context)
	else:
		form = staffRegForm()
	return render(request,'staffmanagement/staffDetailsEntry.html',{'userlist':userlist,'form':form,'allUsers':allUsers,'date':date,'root':settings.BASE_DIR})

def staffManagementEdit(request,date,user_id):
	allUsers = User.objects.all()
	allUserDetails = staffDetails.objects.all()
	userlist=zip(allUsers,allUserDetails)
	usr = User.objects.get(id=user_id)
	username = usr.username
	usr_details = staffDetails.objects.get(user=username)
	print user_id, "\n\n"
	if usr.is_superuser:
		designation = 'admin'
	elif usr.is_staff:
		designation = 'operator'
	user_data={'first_name':usr.first_name,
				'last_name':usr.last_name,
				'username':usr.username,
				'password':usr.password,
				'mob':usr_details.mob,
				'designation': designation,
				'address': usr_details.address,
				'email': usr.email,
				'profile_photo':usr_details.profile_photo,
				'user_id':usr.id,
				}
	form = staffRegForm(user_data)
	return render (request,'staffmanagement/staffDetailsEntry.html',{'userlist':userlist,'form':form,'allUsers':allUsers,'user_id':user_id,'password':usr.password})




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

