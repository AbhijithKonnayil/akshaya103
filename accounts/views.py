from django.shortcuts import render
from accounts.models import accountsIn, accountsOut, bankAccountDetails, recieptDetail, recieptDetailsOut, bankBalanceDetails, bankRechargeDetails
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from .forms import accountsInForm,accountsEditForm, accountsOutForm, recieptDetailsForm, recieptDetailsOutForm, bankAccountDetailsForm, reportTypeForm, bankRechargeForm
from staffmanagement.forms import dateSelectionForm
from django.db.models import F
from django.contrib.auth.models import User

from django.db.models import Sum
import datetime
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
			
			form = accountsInForm(request.POST)
			if form.is_valid():
				
				trans_id=int(form.cleaned_data['trans_id'])
				
				if trans_id == -1:
					
					data = accountsIn()
					data.date = date
					data.reciept = form.cleaned_data['reciept']
					
					data.bank_acc = form.cleaned_data['bank_acc']
					
					data.payment_fees = form.cleaned_data['payment_fees']
					if data.bank_acc:
						bank_acc = bankAccountDetails.objects.all().get(id=data.bank_acc.id)
						bank_acc.current_balance = bank_acc.current_balance - data.payment_fees
					
						if bank_acc.current_balance<0:
							form = accountsInForm()
							negative_balance = bank_acc.bank_name
							context ={'form':form, 'recieptDetail' : reciept,'allReciept':allReciept,
							'date':date,'bankDetails':bankAccDetails, 'credit_list':credit_l,
							'negative_balance':negative_balance}
							
							return render(request, 'accounts/accountsEntry.html',context)

						if bank_acc.current_balance < bank_acc.margin_amount:
							below_margin_amount = bank_acc.bank_name
						else:
							below_margin_amount = False
						bank_acc.save()
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
					below_margin_amount = False
					form = accountsInForm()
			else:
				trans_id=int(form.cleaned_data['trans_id'])
				if trans_id>0:
					data = accountsIn.objects.get(id=trans_id)
					data.amount_to_pay = data.amount_to_pay - form.cleaned_data['rec_amount']
					data.save()
					below_margin_amount =False

				return HttpResponseRedirect('./')

		else:
			form = accountsInForm()
			below_margin_amount =False
		context ={'form':form, 'recieptDetail' : reciept,'allReciept':allReciept,
					'date':date,'bankDetails':bankAccDetails, 'credit_list':credit_l,
					'below_margin_amount':below_margin_amount}
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
	bankAccDetails = bankAccountDetails.objects.all()
	if userValidation(request.user):
		allReciept = accountsOut.objects.all().filter(date=date).order_by('id')
		reciept = recieptDetailsOut.objects.all()
		if request.method =='POST':
			form = accountsOutForm(request.POST)
			if form.is_valid():
				data = accountsOut()
				data.date = date
				data.reciept = form.cleaned_data['reciept']
				data.bank_acc = form.cleaned_data['bank_acc']
				data.charge = form.cleaned_data['charge']
				bank_acc = bankAccountDetails.objects.get(id=data.bank_acc.id)
				bank_acc.current_balance = bank_acc.current_balance - data.charge
				bank_acc.save()
				if bank_acc.current_balance<0:
					form = accountsOutForm()
					negative_balance = bank_acc.bank_name
					
					context={'form':form, 'allReciept':allReciept,'bankDetails':bankAccDetails,'recieptout':reciept,
							 'date':date,'negative_balance':negative_balance}
					return render(request, 'accounts/accountsoutEntry.html',context)


				if bank_acc.current_balance < bank_acc.margin_amount:
					
					below_margin_amount = bank_acc.bank_name
					
				else:
					below_margin_amount = False
				
				data.remark = form.cleaned_data['remark']
				data.staff = request.user
				data.save()
				

		else:
			below_margin_amount = False
		form = accountsOutForm()
		
		return render(request, 'accounts/accountsoutEntry.html',{'form':form, 'allReciept':allReciept,'bankDetails':bankAccDetails,'recieptout':reciept, 'date':date,'below_margin_amount':below_margin_amount})
	return HttpResponseRedirect('/')	

def accountsView(request,date):
	if userValidation(request.user):
		
		if request.method == 'POST':
			
			form_date=dateSelectionForm(request.POST)
			if form_date.is_valid():
				
				req_date = form_date.cleaned_data['date']
				req_db = form_date.cleaned_data['db']
				
				form = reportTypeForm()
				if req_db=="accountsin":
					db = accountsIn.objects.all().filter(date=req_date).order_by('id')
					context={'form':form,'form_date':form_date,'dbin':db, 'date':date,'reciepts':True}
				elif req_db == "accountsout":
					db = accountsOut.objects.all().filter(date=req_date).order_by('id')
					
					context={'form':form,'form_date':form_date,'dbout':db, 'date':date,'payments':True}
				elif req_db == "bankbalance":
					db = bankBalanceDetails.objects.all().filter(date=req_date).order_by('id')
					context={'form':form,'form_date':form_date,'dbbank':db, 'date':date,'bankbalance':True}
					
				

				return render(request,'accounts/accountsview.html',context)
		
		if request.method=='POST':
			form = reportTypeForm(request.POST)
			months_list=["January","February","March","April","May","June","July","August","September","October","November","December"]
			service_fees_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
			payment_fees_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
			total_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
			if form.is_valid():
				
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
						context={'form':form,'form_date':form_date,'date':date,'monthwise':True,'list':report_list,'reciepts':True}


					elif report_type=="receiptwise":
						reciept=recieptDetail.objects.all()
						reciept_list=[]
						reciept_sum=[]
						reciept_title=[]
						for each_receipt in reciept:
							reciept_list.append(each_receipt.id)
							reciept_title.append(each_receipt.reciept_title)

						
						import sys
						#sys.exit(1)
						
						for each_receipt in reciept_list:
							service_fees_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
							
							
							db = accountsIn.objects.all().filter(reciept=each_receipt)
							
							for each_ob in db:
								ob_date=each_ob.date
								month=ob_date.strftime("%B")
								
								for each_month in months_list:
									i = months_list.index(each_month)
									
									if month ==each_month:
										
										service_fees_sum[i]=service_fees_sum[i]+each_ob.service_fees
										
										
										break
							


							reciept_sum.append(service_fees_sum)
							

						form = reportTypeForm(request.POST)
						form_date=dateSelectionForm()
						report_list=zip(reciept_title,reciept_sum)
						context={'form':form,'form_date':form_date,'date':date,
									'receiptwise':True,
									'report_list':report_list,
									'month_list':months_list,
									'reciepts':True,
									'reciept_list_count':len(reciept_list)+1,}
					
					return render(request,'accounts/accountsview.html',context)



					

				elif req_db == "accountsout":
					
					charge_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
					db = accountsOut.objects.all()
					if report_type=="monthwise":
						
						for each_ob in db:
							ob_date=each_ob.date
							month=ob_date.strftime("%B")
							for each_month in months_list:
								i = months_list.index(each_month)
								if month == each_month:
									charge_sum[i]=charge_sum[i]+each_ob.charge
									total_sum[i]=charge_sum[i]

						form = reportTypeForm(request.POST)
						form_date=dateSelectionForm()
						report_list=zip(months_list,total_sum)
						context={'form':form,'form_date':form_date,'date':date,'monthwise':True,'list':report_list,'payments':True}



					elif report_type=="receiptwise":
						
						reciept=recieptDetailsOut.objects.all()
						reciept_list=[]
						reciept_sum=[]
						reciept_title=[]
						for each_receipt in reciept:
							reciept_list.append(each_receipt.id)
							reciept_title.append(each_receipt.reciept_title)

						

						for each_receipt in reciept_list:
							charge_sum=[0,0,0,0,0,0,0,0,0,0,0,0]
							
							
							db = accountsOut.objects.all().filter(reciept=each_receipt)
							
							for each_ob in db:
								ob_date=each_ob.date
								month=ob_date.strftime("%B")
								
								for each_month in months_list:
									i = months_list.index(each_month)
									
									if month ==each_month:
										
										charge_sum[i]=charge_sum[i]+each_ob.charge
										
										break
							


							reciept_sum.append(charge_sum)
							
							
						form = reportTypeForm(request.POST)
						form_date=dateSelectionForm()
						report_list=zip(reciept_title,reciept_sum)
						context={'form':form,'form_date':form_date,'date':date,'receiptwise':True,'report_list':report_list,'month_list':months_list,'payments':True,
									'reciept_list_count':len(reciept_list)+1,}
						
					return render(request,'accounts/accountsview.html',context)

		else:
			form = reportTypeForm()
			form_date=dateSelectionForm()
			context={'form':form,'form_date':form_date,'date':date,'reciepts':True}
			
			return render(request,'accounts/accountsview.html',context)
	return HttpResponseRedirect('/')


def recieptDetailsEntry(request,date):
	if userValidation(request.user):
		try:
			receiptin=recieptDetail.objects.all().get(reciept_title="Suspense Amount")
		except recieptDetail.DoesNotExist:	
			try:
				receiptin=recieptDetail.objects.all().get(id=1)
				receiptin.reciept_title="Suspense Amount"
				receiptin.service_fees=0
				receiptin.ass_fees=0
				receiptin.save()
				print "problem"
			except recieptDetail.DoesNotExist:
				receiptin=recieptDetail()
				receiptin.id=1
				receiptin.reciept_title="Suspense Amount"
				receiptin.service_fees=0
				receiptin.ass_fees=0
				receiptin.save()
		try:
			receiptout=recieptDetailsOut.objects.all().get(reciept_title="Suspense Amount")
		except recieptDetailsOut.DoesNotExist:	
			try:
				receiptout=recieptDetailsOut.objects.all().get(id=1)
				receiptout.reciept_title="Suspense Amount"
				receiptout.service_fees=0
				receiptout.ass_fees=0
				receiptout.save()
			except recieptDetailsOut.DoesNotExist:
				receiptout=recieptDetailsOut()
				receiptout.id=1
				receiptout.reciept_title="Suspense Amount"
				receiptout.service_fees=0
				receiptout.ass_fees=0
				receiptout.save()

		if request.method == 'POST':
			formin = recieptDetailsForm(request.POST)
			formout = recieptDetailsOutForm(request.POST)
			if formin.is_valid():
				data = recieptDetail()
				data.reciept_title = formin.cleaned_data['reciept_title']
				data.service_fees = formin.cleaned_data['service_fees']
				
				
				if formin.cleaned_data['fees_associated']==True:
					data.ass_bank_acc = formin.cleaned_data['ass_bank_acc']
					data.ass_fees = formin.cleaned_data['ass_fees']
				data.save()
				return HttpResponseRedirect('./')

			elif formout.is_valid():
				data = recieptDetailsOut()
				data.reciept_title = formout.cleaned_data['reciept_title']
				data.charge = formout.cleaned_data['charge']
				data.ass_bank_acc = formin.cleaned_data['ass_bank_acc']
				data.save()
				return HttpResponseRedirect('./')
		else:
			formin= recieptDetailsForm()
			formout = recieptDetailsOutForm()
		receiptin = recieptDetail.objects.all()
		receiptout = recieptDetailsOut.objects.all()
		return render(request,'accounts/recieptDetailsEntry.html',{'formin':formin,'formout':formout,'date':date,'receiptin':receiptin,'receiptout':receiptout})
	return HttpResponseRedirect('/')	

def bankAccountDetailsEntry(request,date):
	if userValidation(request.user):
		if request.method == 'POST':
			form = bankAccountDetailsForm(request.POST)
			form_recharge = bankRechargeForm(request.POST)
			
			if form.is_valid():
				
				bank = bankBalanceDetails()
				data = bankAccountDetails()
				data.bank_name = form.cleaned_data['bank_name']
				data.opening_balance = form.cleaned_data['opening_balance']
				data.opening_balance_date = form.cleaned_data['opening_balance_date']
				data.margin_amount = form.cleaned_data['margin_amount']
				data.current_balance = data.opening_balance 
				data.save()
				bank_pointer=bankAccountDetails.objects.all().last()
				bank.bank=bank_pointer
				bank.date=date
				
				bank.opening_balance=data.opening_balance
				bank.closing_balance=bank.opening_balance
				bank.save()

				return HttpResponseRedirect('./')
			if form_recharge.is_valid():
				
				data = bankRechargeDetails()
				data.bank = form_recharge.cleaned_data['bank']
				
				data.amount=form_recharge.cleaned_data['amount']
				data.save()
				bank = bankAccountDetails.objects.get(id=data.bank.id)
				bank.current_balance=bank.current_balance+data.amount
				bank.save()

				
			
				try:
					bank_ob_data = bankBalanceDetails.objects.get(date=date,bank=data.bank)
					bank_ob_data.closing_balance = bank_ob_data.closing_balance + data.amount
					bank_ob_data.date=date
					bank_ob_data.save()
					

				except bankBalanceDetails.DoesNotExist:
					bank_ob_data = bankBalanceDetails.objects.filter(bank=data.bank).last()

					if bank_ob_data:
						bank = bankBalanceDetails()
						bank.bank= data.bank
						
						bank.date=date
						
						bank.opening_balance = bank_ob_data.closing_balance
						
						bank.closing_balance = bank.opening_balance + data.amount
						bank.save()
					else:
						
						bank = bankBalanceDetails()
						bank.bank= data.bank
						bank.date=date
						bank_ob_data=bankAccountDetails.objects.get(data.bank)
						bank.opening_balance = bank_ob_data.opening_balance
						
						bank.closing_balance = bank.opening_balance + data.amount
						bank.save()
				"""		
					except bankBalanceDetails.DoesNotExist:
						bank_ob_data=bankAccountDetails.objects.get(id=bank.bank)
						
				"""
				
				
				return HttpResponseRedirect('./')
		else:
			form = bankAccountDetailsForm()
			form_recharge=bankRechargeForm()
		context = {'form':form,'form_recharge':form_recharge,'date':date}
		return render(request,'accounts/bankAccountDetailsEntry.html',context)
	return HttpResponseRedirect('/')	


def closeAccounts(request,date):
	if userValidation(request.user):
		
		recieptin=recieptDetail.objects.values('id','reciept_title')
		accountsin=accountsIn.objects.values('reciept').annotate(sum_payment_fees=Sum('payment_fees'),sum_service_fees=Sum('service_fees')).filter(date=date)
		accountsin_sum = accountsIn.objects.all().filter(date=date).aggregate(Sum('payment_fees'),Sum('service_fees'),Sum('total_fees'))
		recieptout=recieptDetailsOut.objects.values('id','reciept_title')
		accountsout=accountsOut.objects.values('reciept').annotate(sum_charge=Sum('charge')).filter(date=date)
		accountsout_sum = accountsOut.objects.all().filter(date=date).aggregate(Sum('charge'))

		accountsin_bank = accountsIn.objects.values('bank_acc').annotate(sum_payment_fees=Sum('payment_fees')).filter(date=date)
		

		
		for each in accountsin_bank:
			
			if each['bank_acc']> 0:
				
				try:
					bankRecharge = bankRechargeDetails.objects.values('bank').annotate(sum_amount=Sum('amount')).filter(date=date,bank=each['bank_acc'])
					#bankRecharge_sum = bankRechargeDetails.objects.values('bank').annotate(sum_amount=Sum('amount')).filter(date=date,bank=each['bank_acc'])
					
					if bankRecharge:
						bankRecharge_sum=bankRecharge[0]
						bankRechargeAmount_sum=bankRecharge_sum['sum_amount']
					else:
						bankRechargeAmount_sum=0
				except bankRechargeDetails.DoesNotExist:
					bankRechargeAmount_sum=0


				
				try:
					
					bank=bankBalanceDetails.objects.get(date=date,bank=each['bank_acc'])
					bank.closing_balance=bank.opening_balance-each['sum_payment_fees'] + bankRechargeAmount_sum
					bank.save()
					
				except bankBalanceDetails.DoesNotExist:
					
					data = bankBalanceDetails()
					try:
						bank = bankBalanceDetails.objects.filter(bank=each['bank_acc']).last()
						data.bank = bank.bank
						data.date=date
						data.opening_balance = bank.closing_balance
						data.closing_balance = data.opening_balance - each['sum_payment_fees'] + bankRechargeAmount_sum
						data.save()
					except:
						init_bank_data=bankAccountDetails.objects.get(id=each['bank_acc'])
						data.bank=init_bank_data
						data.date=date
						data.opening_balance=init_bank_data.opening_balance
						data.closing_balance=  data.opening_balance - each['sum_payment_fees'] + bankRechargeAmount_sum
						data.save()

		

		if accountsout_sum['charge__sum']:
			pass;
		else:
			accountsout_sum['charge__sum']=0.0

		if accountsin_sum['total_fees__sum']:
			pass;
		else:
			accountsin_sum['total_fees__sum']=0.0


		if request.method =='POST':
			
			formout=accountsOutForm(request.POST)
			form = accountsInForm(request.POST)
			

			if formout.is_valid():
				data = accountsOut()
				data.date = date
				data.reciept = formout.cleaned_data['reciept']
				data.bank_acc = formout.cleaned_data['bank_acc']
				data.charge = formout.cleaned_data['charge']
				data.remark = "Suspense Amount"
				data.staff = request.user
				data.save()
				return HttpResponseRedirect('./')

			else:
				formout=accountsOutForm()

			if form.is_valid():
				
				data = accountsIn()
				data.date = date
				data.reciept = form.cleaned_data['reciept']
				data.bank_acc = form.cleaned_data['bank_acc']
				data.payment_fees = form.cleaned_data['payment_fees']
				data.service_fees = form.cleaned_data['service_fees']
				data.customer_name = "Suspence amount"
				data.username = "Suspense amount"
				data.password = "Suspense amount"
				data.contact_no = "Suspense"
				data.total_fees = data.payment_fees+data.service_fees
				data.remark = "Suspence amount"
				data.amount_to_pay = 0
				data.staff = request.user
				data.save()
				form = accountsInForm()
				return HttpResponseRedirect('./')

			else:

				
				form = accountsInForm()

		form = accountsInForm()
		formout=accountsOutForm()
		context={	'accountsin':accountsin,'recieptin':recieptin,
					'accountsin_sum':[accountsin_sum['payment_fees__sum'],accountsin_sum['service_fees__sum'],accountsin_sum['total_fees__sum']],
					'accountsout':accountsout,'recieptout':recieptout,
					'accountsout_sum':accountsout_sum['charge__sum'],
					'netTotal':accountsin_sum['total_fees__sum']-accountsout_sum['charge__sum'],
					'form':form,'formout':formout,
					'date': date,
					'gen':True,
				}
					
		return render(request,'accounts/closeaccounts.html',context)	
	return HttpResponseRedirect('/')	
