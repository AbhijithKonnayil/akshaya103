from django.shortcuts import render
from staffmanagement.models import staffDetails
from django.http import Http404, HttpResponseRedirect
from .forms import staffDetailsForm, staffRegForm
from django.contrib.auth.models import User

# Create your views here.
def staffManagement(request):
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
				staff = User.objects.create_user(username, email, password)
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
	return render(request,'staffmanagement/staffDetailsEntry.html',{'form':form,})


def dashboard(request):

	return render(request,'staffmanagement/dashboard.html')