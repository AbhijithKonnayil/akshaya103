from django.conf.urls import url
from . import views

urlpatterns = [
	#/accounts/
	url(r'^$', views.index, name='index'),
	#/accounts/1
	url(r'^(?P<reciept_id>[0-9]+)/$', views.detail, name='detail'),

	#accounts/entry
	url(r'^entry$', views.accountsEntry, name='accountsEntry'),
]