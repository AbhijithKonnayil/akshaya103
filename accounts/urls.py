from django.conf.urls import url
from . import views

urlpatterns = [
	#/accounts/
	url(r'^$', views.index, name='index'),

	#/accounts/1
	url(r'^(?P<reciept_id>[0-9]+)/$', views.detail, name='detail'),

	#accounts/close
	url(r'^close/(?P<date>\d{4}-\d{2}-\d{2})/$', views.closeAccounts, name='closeAccounts'),

	#accounts/entry
	url(r'^entry/(?P<date>\d{4}-\d{2}-\d{2})/$', views.accountsInEntry, name='accountsInEntry'),

	#accounts/entry
	url(r'^outentry/(?P<date>\d{4}-\d{2}-\d{2})/$', views.accountsOutEntry, name='accountsOutEntry'),

	#accounts/recieptDetails/entry
	url(r'^recieptDetails/add/(?P<date>\d{4}-\d{2}-\d{2})/$', views.recieptDetailsEntry, name='recieptDetailsEntry'),

	#accounts/bankDetails/add
	url(r'^bankDetails/add/(?P<date>\d{4}-\d{2}-\d{2})/$', views.bankAccountDetailsEntry, name='bankAccountDetailsEntry'),
]