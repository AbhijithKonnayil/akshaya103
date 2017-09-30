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
	#url(r'^staffs/(?P<date>\d{4}-\d{2}-\d{2})$', views.dashboard, name='dashboard'),
	url(r'^staffs/(?P<date>[\w.]+[\W]{1}\d{2}[\w,]{1}[\W]{1}\d{4})/$', views.dashboard, name='dashboard'),
	#/date
	url(r'^date/$', views.selectDate, name='date'),
]