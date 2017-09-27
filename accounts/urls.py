from django.conf.urls import url
from . import views

urlpatterns = [
	#/accounts/
	url(r'^$', views.index, name='index'),
	#/accounts/1
	url(r'^(?P<reciept_id>[0-9]+)/$', views.detail, name='detail'),
	#accounts/entry
	url(r'^entry$', views.accountsInEntry, name='accountsInEntry'),
	#accounts/entry
	url(r'^entry/(?P<date>\d{4}-\d{2}-\d{2})$', views.accountsInEntry, name='accountsInEntry'),
	#accounts/recieptDetails/entry
	url(r'^recieptDetails/add$', views.recieptDetailsEntry, name='recieptDetailsEntry'),
	#accounts/bankDetails/add
	url(r'^bankDetails/add$', views.bankAccountDetailsEntry, name='bankAccountDetailsEntry'),
]