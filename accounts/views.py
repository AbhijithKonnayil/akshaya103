from django.shortcuts import render
from accounts.models import accountsin
from django.http import Http404
# Create your views here.
def index(request):
	html = ''
	allReciept=accountsin.objects.all()
	context = {		'allReciept': allReciept,		}
	
	return render(request, 'accounts/index.html',context)

def detail(request, reciept_id):
	try:
		reciept = accountsin.objects.get(id=reciept_id)
	except accountsin.DoesNotExist:
		raise Http404("Reciept does not exist")
	return render(request, 'music/index.html',{'accountsin':accountsin})