from django.shortcuts import render
from accounts.models import accountsIn, accountsOut, recieptDetails, bankAccountDetails
from django.http import Http404, HttpResponseRedirect
from .forms import accountsInForm, accountsOutForm, recieptDetailsForm, bankAccountDetailsForm
# Create your views here.

def index(request):
	html = ''
	allReciept=accountsIn.objects.all()
	context = {'allReciept': allReciept,}
	
	return render(request, 'accounts/index.html',context)

def detail(request, reciept_id):
	try:
		reciept = accountsIn.objects.get(id=reciept_id)
	except accountsIn.DoesNotExist:
		raise Http404("Reciept does not exist")
	return render(request, 'accounts/details.html',{'accountsIn':reciept.id})

def accountsInEntry(request,date):
	allReciept = accountsIn.objects.all().filter(date=date).order_by('id')
	reciept = recieptDetails.objects.all()
	if request.method =='POST':
		form = accountsInForm(request.POST)
		if form.is_valid():
			data = accountsIn()
			data.date = date
			data.reciept = form.cleaned_data['reciept']
			data.bank_acc = form.cleaned_data['bank_acc']
			data.payment_fees = form.cleaned_data['payment_fees']
			data.service_fees = form.cleaned_data['service_fees']
			data.customer_name = form.cleaned_data['customer_name']
			data.username = form.cleaned_data['username']
			data.password = form.cleaned_data['password']
			data.contact_no = form.cleaned_data['contact_no']
			data.total_fees = data.payment_fees+data.service_fees
			data.remark = form.cleaned_data['remark']
			data.staff = request.user
			data.save()
			return HttpResponseRedirect('./')

	else:
		form = accountsInForm(initial={'reciept':('Others','Others')})
	return render(request, 'accounts/accountsEntry.html',{'form':form, 'allReciept':allReciept, 'recieptDetails' : reciept,'date':date})

def accountsOutEntry(request,date):
	allReciept = accountsOut.objects.all().filter(date=date).order_by('id')
	#reciept = recieptDetails.objects.all()
	if request.method =='POST':
		form = accountsOutForm(request.POST)
		if form.is_valid():
			data = accountsOut()
			data.date = date
			data.reciept = form.cleaned_data['reciept']
			data.bank_acc = form.cleaned_data['bank_acc']
			data.charge = form.cleaned_data['charge']
			data.remark = form.cleaned_data['remark']
			data.staff = request.user
			data.save()
			return HttpResponseRedirect('./')

	else:
		form = accountsOutForm()
	return render(request, 'accounts/accountsoutEntry.html',{'form':form, 'allReciept':allReciept, 'date':date})

def recieptDetailsEntry(request,date):
	if request.method == 'POST':
		form = recieptDetailsForm(request.POST)
		if form.is_valid():
			data = recieptDetails()
			data.reciept_title = form.cleaned_data['reciept_title']
			data.service_fees = form.cleaned_data['service_fees']
			data.ass_bank_acc = form.cleaned_data['ass_bank_acc']
			data.save()
			return HttpResponseRedirect('./')
	else:
		form = recieptDetailsForm()
	return render(request,'accounts/recieptDetailsEntry.html',{'form':form,'date':date})

def bankAccountDetailsEntry(request,date):
	if request.method == 'POST':
		form = bankAccountDetailsForm(request.POST)
		if form.is_valid():
			data = bankAccountDetails()
			data.bank_name = form.cleaned_data['bank_name']

			data.save()
			return HttpResponseRedirect('./')
	else:
		form = bankAccountDetailsForm()
	return render(request,'accounts/bankAccountDetailsEntry.html',{'form':form,'date':date})

def closeAccounts(request,date):
	accountsin = accountsIn.objects.all().filter(date=date)
	accountsout = accountsOut.objects.all().filter(date=date)
	reciepts = recieptDetails.objects.all()
	individual_accountsin_sum = 0
	individual_accountsout_sum = 0
	all_staff_sum_accountsin = 0
	all_staff_sum_accountsout = 0
	for account in accountsin:
		all_staff_sum_accountsin+=account.total_fees
		if account.staff == request.user.username:

			individual_accountsin_sum+=account.total_fees
	for account in accountsout:
		all_staff_sum_accountsout+=account.charge
		if account.staff == request.user.username:
			individual_accountsout_sum+=account.charge

	context={	'all_staff_accountsin_sum': all_staff_sum_accountsin,
				'individual_accountsin_sum': individual_accountsin_sum,
				'all_staff_accountsout_sum': all_staff_sum_accountsout,
				'individual_accountsout_sum': individual_accountsout_sum,
				'date': date,
			}
	return render(request,'accounts/closeaccounts.html',context)	