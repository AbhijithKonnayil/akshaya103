from django.shortcuts import render
from accounts.models import accountsIn, accountsOut, bankAccountDetails, recieptDetail
from django.http import Http404, HttpResponseRedirect
from .forms import accountsInForm,accountsEditForm, accountsOutForm, recieptDetailsForm, bankAccountDetailsForm, reportTypeForm
from staffmanagement.forms import dateSelectionForm
from django.db.models import F
from django.contrib.auth.models import User
import datetime
from django.db.models.functions import TruncMonth
#from django.conf.urls import media
# Create your views here.
def userValidation(user):
	if user.is_authenticated:
		return True
	else:
		return False

def accountsInEntry(request,date):
	if userValidation(request.user):
		bankAccDetails = bankAccountDetails.objects.all()
		allReciept = accountsIn.objects.all().filter(date=date).order_by('id')
		reciept = recieptDetail.objects.all()
		credit_l = accountsIn.objects.filter(amount_to_pay__gt=0).order_by('-amount_to_pay')
		if request.method =='POST':
			print("\n post recived \n")
			form = accountsInForm(request.POST)
			if form.is_valid():
				print("\n valid form \n")
				trans_id=int(form.cleaned_data['trans_id'])
				print "\n", trans_id, "\n"
				if trans_id == -1:
					print "\n in if ", trans_id, "\n"
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
					form = accountsInForm()
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
	return HttpResponseRedirect('/')	

def accountsInEdit(request,date,trans_id):
	if userValidation(request.user):
		data = accountsIn.objects.get(id=trans_id)
		credit_l = accountsIn.objects.filter(amount_to_pay__gt=0).order_by('id')
		edit_data = {}
		form = accountsInForm()
		context = {'trans_id':data.id,'reciept':data.reciept,'bank_acc':data.bank_acc,'payment_fees':data.payment_fees,'service_fees':data.service_fees,'customer_name':data.customer_name,'username':data.username,'password':data.password
		,'contact_no':data.contact_no,'remark':data.remark,'total_fees':data.service_fees+data.payment_fees,'amount_to_pay':data.amount_to_pay,'form':form, 'date':date,'credit_list':credit_l,}
		return render(request, 'accounts/accountsEdit.html',context)
	return HttpResponseRedirect('/')

def accountsOutEntry(request,date):
	if userValidation(request.user):
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
	return HttpResponseRedirect('/')	

def accountsView(request,date):
	if userValidation(request.user):
		print "valid useer\n"
		if request.method == 'POST':
			print "post recived\n"
			form_date=dateSelectionForm(request.POST)
			if form_date.is_valid():
				print "valid formr\n"
				req_date = form_date.cleaned_data['date']
				req_db = form_date.cleaned_data['db']
				print req_db , " \n", req_date, "\n"
				if req_db=="accountsin":
					db = accountsIn.objects.all().filter(date=req_date).order_by('id')
				elif req_db == "accountsout":
					db = accountsOut.objects.all().filter(date=req_date).order_by('id')
				form = reportTypeForm()
				context={'form':form,'form_date':form_date,'db':db, 'date':date}		
				return render(request,'accounts/accountsview.html',context)
		
		if request.method=='POST':
			form = reportTypeForm(request.POST)
			months_list=["","January","February","March","April","May","June","July","August","September","October","November","December"]
			service_fees_sum=[-1,0,0,0,0,0,0,0,0,0,0,0,0]
			payment_fees_sum=[-1,0,0,0,0,0,0,0,0,0,0,0,0]
			total_sum=[-1,0,0,0,0,0,0,0,0,0,0,0,0]
			if form.is_valid:
				print form,"\n\n\n"
				report_type=form.cleaned_data['report_type']
				req_db=form.cleaned_data['db']
				if req_db=="accountsin":
					db = accountsIn.objects.all()
					if report_type=="monthwise":
						for each_ob in db:
							ob_date=each_ob.date
							month=ob_date.strftime("%B")
							for each_month in months_list:
								i = months_list.index(each_month)
								if month == each_month:
									service_fees_sum[i]=service_fees_sum[i]+each_ob.service_fees
									payment_fees_sum[i]=payment_fees_sum[i]+each_ob.payment_fees
									total_sum[i]=total_sum[i]+each_ob.total_fees

						form = reportTypeForm(request.POST)
						form_date=dateSelectionForm()
						report_list=zip(months_list,service_fees_sum,payment_fees_sum,total_sum)
						context={'form':form,'form_date':form_date,'date':date,'monthwise':True,'list':report_list}


					elif report_type=="receiptwise":
						reciept=recieptDetail.objects.all()
						reciept_list=[]
						reciept_sum=[]
						reciept_title=[]
						for each_receipt in reciept:
							reciept_list.append(each_receipt.id)
							reciept_title.append(each_receipt.reciept_title)

						print "Reciept List id ",reciept_list,"\n"

						for each_receipt in reciept_list:
							service_fees_sum=[-1,0,0,0,0,0,0,0,0,0,0,0,0]
							print "-------------------------------------------------------"
							print "Reciept id : ", each_receipt 
							db = accountsIn.objects.all().filter(reciept=each_receipt)
							print db
							for each_ob in db:
								ob_date=each_ob.date
								month=ob_date.strftime("%B")
								
								for each_month in months_list:
									i = months_list.index(each_month)
									print"\t",each_month
									if month ==each_month:
										print "\t\tservice fees sum : ",service_fees_sum[i],"\n\t\tservice fees : ",each_ob.service_fees
										service_fees_sum[i]=service_fees_sum[i]+each_ob.service_fees
										print "\t\tservice fees sum : " ,service_fees_sum
										print "\t\treciept_sum : " ,reciept_sum
										break

							reciept_sum.append(service_fees_sum)
							print "reciept sum:",reciept_sum
									
						print"-----------------------------------"
						print "arary:\n",reciept_sum," ||||||||||||||"
						print "lenth ",len(reciept_sum)," ||||||||||"
						print"-----------------------------------"
						print months_list
						form = reportTypeForm(request.POST)
						form_date=dateSelectionForm()
						report_list=zip(reciept_title,reciept_sum)
						print range(13)
						context={'form':form,'form_date':form_date,'date':date,'receiptwise':True,'months_list':zip(months_list,range(13)),'report_list':report_list}
					
					return render(request,'accounts/accountsview.html',context)



					print "\n"
				elif req_db == "accountsout":
					db = accountsOut.objects.all()



		else:
			form = reportTypeForm()
			form_date=dateSelectionForm()
			context={'form':form,'form_date':form_date,'date':date}
			print "post not\n"
			return render(request,'accounts/accountsview.html',context)
	return HttpResponseRedirect('/')


def recieptDetailsEntry(request,date):
	if userValidation(request.user):
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
	return HttpResponseRedirect('/')	

def bankAccountDetailsEntry(request,date):
	if userValidation(request.user):
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
	return HttpResponseRedirect('/')	

def closeAccounts(request,date):
	if userValidation(request.user):
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
				}
					
		return render(request,'accounts/closeaccounts.html',context)	
	return HttpResponseRedirect('/')	

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
	if date==bankAccountDetails.objects.get(id=9).opening_balance_date:
		return bankAccountDetails.objects.get(id=9).opening_balance
	ob=closingBalance(datetime.date.today()-datetime.timedelta(1))
	return ob
	
