from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	#/staff/add
	url(r'^staffs/add$', views.staffManagement, name='staffManagement'),
	#/login
	url(r'^login/$',login, {'template_name':'staffmanagement/login.html'}),
	#/logout
	url(r'^logout/$',logout, {'template_name':'staffmanagement/logout.html'}),
	#/staffs
	url(r'^staffs/$', views.dashboard, name='dashboard'),
	#/date
	url(r'^date/$', views.selectDate, name='date'),
]