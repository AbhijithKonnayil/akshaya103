from django.shortcuts import render
from accounts.models import accountsIn, accountsOut, bankAccountDetails, recieptDetail
from django.http import Http404, HttpResponseRedirect
from .forms import accountsInForm,accountsEditForm, accountsOutForm, recieptDetailsForm, bankAccountDetailsForm
from django.db.models import F
import datetime

#from django.conf.urls import media
# Create your views here.

def accountsInEntry(request,date):
	bankAccDetails = bankAccountDetails.objects.all()
	allReciept = accountsIn.objects.all().filter(date=date).order_by('id')
	reciept = recieptDetail.objects.all()
	credit_l = accountsIn.objects.filter(amount_to_pay__gt=0).order_by('-amount_to_pay')
	if request.method =='POST':
		form = accountsInForm(request.POST)
		if form.is_valid():
			trans_id=form.cleaned_data['trans_id']
			if trans_id == -1:
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
				data.amount_to_pay = data.total_fees - form.cleaned_data['rec_amount']
				data.staff = request.user
				data.save()
		else:
			trans_id=int(form.cleaned_data['trans_id'])
			if trans_id>0:
				data = accountsIn.objects.get(id=trans_id)
				data.amount_to_pay = data.amount_to_pay - form.cleaned_data['rec_amount']
				data.save()

			return HttpResponseRedirect('./')

	else:
		form = accountsInForm()
	context ={'form':form, 'recieptDetail' : reciept,'allReciept':allReciept,'date':date,'bankDetails':bankAccDetails, 'credit_list':credit_l,}
	return render(request, 'accounts/accountsEntry.html',context)

def accountsInEdit(request,date,trans_id):
	data = accountsIn.objects.get(id=trans_id)
	credit_l = accountsIn.objects.filter(amount_to_pay__gt=0).order_by('id')
	edit_data = {}
	form = accountsInForm()
	context = {'trans_id':data.id,'reciept':data.reciept,'bank_acc':data.bank_acc,'payment_fees':data.payment_fees,'service_fees':data.service_fees,'customer_name':data.customer_name,'username':data.username,'password':data.password
	,'contact_no':data.contact_no,'remark':data.remark,'total_fees':data.service_fees+data.payment_fees,'rec_amount':data.amount_to_pay,'form':form, 'date':date,'credit_list':credit_l,}
	return render(request, 'accounts/accountsEdit.html',context)


def accountsOutEntry(request,date):
	allReciept = accountsOut.objects.all().filter(date=date).order_by('id')
	reciept = recieptDetail.objects.all()
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
			data = recieptDetail()
			data.reciept_title = form.cleaned_data['reciept_title']
			data.service_fees = form.cleaned_data['service_fees']
			if form.cleaned_data['fees_associated']=='yes':
				data.ass_bank_acc = form.cleaned_data['ass_bank_acc']
				data.ass_fees = form.cleaned_data['ass_fees']
			data.save()
			return HttpResponseRedirect('./')
	else:
		form = recieptDetailsForm()
	return render(request,'accounts/recieptDetailsEntry.html',{'form':form,'date':date,})

def bankAccountDetailsEntry(request,date):
	if request.method == 'POST':
		form = bankAccountDetailsForm(request.POST)
		if form.is_valid():
			data = bankAccountDetails()
			data.bank_name = form.cleaned_data['bank_name']
			data.opening_balance = form.cleaned_data['opening_balance']
			data.opening_balance_date = form.cleaned_data['opening_balance_date']
			data.save()
			return HttpResponseRedirect('./')
	else:
		form = bankAccountDetailsForm()
	return render(request,'accounts/bankAccountDetailsEntry.html',{'form':form,'date':date})

def closeAccounts(request,date):
	print date,"\n\n",datetime.date.today(),"\n"
	accountsin = accountsIn.objects.all().filter(date=date)
	accountsout = accountsOut.objects.all().filter(date=date)
	reciepts = recieptDetail.objects.all()
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
				'openingBalance':openingBalance(date),
				'closingBalance':closingBalance(date)
			}
	return render(request,'accounts/closeaccounts.html',context)	


def closingBalance(date):
	print "\n closing : ", date 
	accountsin = accountsIn.objects.all().filter(date=date)
	accountsout = accountsOut.objects.all().filter(date=date)
	sum_accountsin=0
	sum_accountsout=0
	for account in accountsin:
		sum_accountsin+=account.total_fees
	for account in accountsout:
		sum_accountsout+=account.charge
	net=sum_accountsin-sum_accountsout
	cb=openingBalance(date)-net
	return cb

def openingBalance(date):
	print "\n opening : ", date 
	if date==bankAccountDetails.objects.get(id=1).opening_balance_date:
		return bankAccountDetails.objects.get(id=1).opening_balance
	ob=closingBalance(datetime.date.today()-datetime.timedelta(1))
	return ob
	
