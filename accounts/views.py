from django.shortcuts import render
from accounts.models import accountsIn
from django.http import Http404, HttpResponse
from .forms import accountsInForm
# Create your views here.

def index(request):
	html = ''
	allReciept=accountsIn.objects.all()
	context = {		'allReciept': allReciept,		}
	
	return render(request, 'accounts/index.html',context)

def detail(request, reciept_id):
	try:
		reciept = accountsIn.objects.get(id=reciept_id)
	except accountsIn.DoesNotExist:
		raise Http404("Reciept does not exist")
	return render(request, 'accounts/details.html',{'accountsIn':reciept.id})

def accountsEntry(request):
	if request.method =='POST':
		form = accountsInForm(request.POST)
		if form.is_valid():
			data = accountsIn()
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
			data.save()
			return HttpResponse('thanks')

	else:
		form = accountsInForm()
		return render(request, 'accounts/accountsEntry.html', {'form':form})

