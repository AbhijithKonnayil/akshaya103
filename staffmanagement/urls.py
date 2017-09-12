from django.conf.urls import url
from . import views

urlpatterns = [
	#/staff/add
	url(r'^staffs/add$', views.staffManagement, name='staffManagement'),
	#/accounts/1
]