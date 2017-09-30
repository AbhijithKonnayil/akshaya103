from django.conf.urls import url
from . import views

urlpatterns = [
	#/accounts/
	url(r'^$', views.index, name='index'),

	#/accounts/1
	url(r'^(?P<reciept_id>[0-9]+)/$', views.detail, name='detail'),

	#accounts/close
	url(r'^close/(?P<date>[\w.]+[\W]{1}\d{2}[\w,]{1}[\W]{1}\d{4})/$', views.closeAccounts, name='closeAccounts'),

	#accounts/entry
	url(r'^entry/(?P<date>[\w.]+[\W]{1}\d{2}[\w,]{1}[\W]{1}\d{4})/$', views.accountsInEntry, name='accountsInEntry'),

	#accounts/entry
	url(r'^outentry/(?P<date>[\w.]+[\W]{1}\d{2}[\w,]{1}[\W]{1}\d{4})/$', views.accountsOutEntry, name='accountsOutEntry'),

	#accounts/recieptDetails/entry
	url(r'^recieptDetails/add$', views.recieptDetailsEntry, name='recieptDetailsEntry'),

	#accounts/bankDetails/add
	url(r'^bankDetails/add$', views.bankAccountDetailsEntry, name='bankAccountDetailsEntry'),
]