from django.shortcuts import render
from accounts.models import accountsIn, recieptDetails, bankAccountDetails
from django.http import Http404, HttpResponseRedirect
from .forms import accountsInForm, recieptDetailsForm, bankAccountDetailsForm
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
			return HttpResponseRedirect(date)

	else:
		form = accountsInForm(initial={'reciept':('Others','Others')})
	return render(request, 'accounts/accountsEntry.html',{'form':form, 'allReciept':allReciept, 'recieptDetails' : reciept,'date':date})

def recieptDetailsEntry(request):
	if request.method == 'POST':
		form = recieptDetailsForm(request.POST)
		if form.is_valid():
			data = recieptDetails()
			data.reciept_title = form.cleaned_data['reciept_title']
			data.service_fees = form.cleaned_data['service_fees']
			data.ass_bank_acc = form.cleaned_data['ass_bank_acc']
			data.save()
			return HttpResponseRedirect('entry')
	else:
		form = recieptDetailsForm()
	return render(request,'accounts/recieptDetailsEntry.html',{'form':form,})

def bankAccountDetailsEntry(request):
	if request.method == 'POST':
		form = bankAccountDetailsForm(request.POST)
		if form.is_valid():
			data = bankAccountDetails()
			data.bank_name = form.cleaned_data['bank_name']
			data.bank_branch = form.cleaned_data['bank_branch']
			data.acc_holder = form.cleaned_data['acc_holder']
			data.bank_acc_no = form.cleaned_data['bank_acc_no']
			data.acc_holder_contactno = form.cleaned_data['acc_holder_contactno']
			data.balance = form.cleaned_data['balance']
			data.save()
			return HttpResponseRedirect('add')
	else:
		form = bankAccountDetailsForm()
	return render(request,'accounts/bankAccountDetailsEntry.html',{'form':form,})

def closeAccounts(request,date):
	accounts = accountsIn.objects.all().filter(date=date)
	reciepts = recieptDetails.objects.all()
	individual_sum = 0
	all_staff_sum = 0
	for account in accounts:
		all_staff_sum+=account.total_fees
		if account.staff == request.user.username:

			individual_sum+=account.total_fees

	context={'total_fees':all_staff_sum,'individual_sum': individual_sum,'date': date,}
	return render(request,'accounts/closeaccounts.html',context)	