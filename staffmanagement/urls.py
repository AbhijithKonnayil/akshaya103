from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	#/staff/add
	url(r'^staffs/add/(?P<date>\d{4}-\d{2}-\d{2})$', views.staffManagement, name='staffManagement'),
	#/login
	url(r'^login/$',login, {'template_name':'staffmanagement/login.html'}),
	#/logout
	url(r'^logout/$',logout, {'template_name':'staffmanagement/logout.html'}),
	#/staffs
	 url(r'^staffs/(?P<date>\d{4}-\d{2}-\d{2})/$', views.dashboard, name='dashboard'),
	#/date
	url(r'^date/$', views.selectDate, name='date'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)