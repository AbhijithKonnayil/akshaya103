from django.shortcuts import render
from staffmanagement.models import staffDetails
from django.http import Http404, HttpResponseRedirect
from .forms import staffDetailsForm

# Create your views here.
def staffManagement(request):
	if request.method == 'POST':
		form = staffDetailsForm(request.POST)
		if form.is_valid():
			staff = staffDetails()
			staff.name = form.cleaned_data['name']
			staff.mob = form.cleaned_data['mob']
			staff.address = form.cleaned_data['address']
			staff.email = form.cleaned_data['email']
			staff.save()
			return HttpResponseRedirect('add')
	else:
		form = staffDetailsForm()
	return render(request,'staffmanagement/staffDetailsEntry.html',{'form':form,})
