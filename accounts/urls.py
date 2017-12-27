from django.conf.urls import url
from . import views

urlpatterns = [
	#accounts/close
	url(r'^close/(?P<date>\d{4}-\d{2}-\d{2})/$', views.closeAccounts, name='closeAccounts'),

	#accounts/entry
	url(r'^entry/(?P<date>\d{4}-\d{2}-\d{2})/$', views.accountsInEntry, name='accountsInEntry'),

	#accounts/entry/2015-12-2/5
	url(r'^entry/(?P<date>\d{4}-\d{2}-\d{2})/(?P<trans_id>(\d+))/$', views.accountsInEdit, name='accountsInEdit'),

	#accounts/entry
	url(r'^outentry/(?P<date>\d{4}-\d{2}-\d{2})/$', views.accountsOutEntry, name='accountsOutEntry'),

	#accounts/recieptDetails/entry
	url(r'^recieptDetails/add/(?P<date>\d{4}-\d{2}-\d{2})/$', views.recieptDetailsEntry, name='recieptDetailsEntry'),

	#accounts/bankDetails/add
	url(r'^bankDetails/add/(?P<date>\d{4}-\d{2}-\d{2})/$', views.bankAccountDetailsEntry, name='bankAccountDetailsEntry'),
]