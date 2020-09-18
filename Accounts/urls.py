from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from Accounts.views import VlidatePhoneSendOTP,VlidateOTP,VlidateService,Dashbord,list_service
app_name='accounts'

admin.autodiscover()
urlpatterns = [
    url(r'^validate_phone/$', VlidatePhoneSendOTP, name='valid_phone'),
    url(r'^validate_otp/$', VlidateOTP, name='valid_otp'),
    url(r'^service/$', VlidateService, name='service'),
    url(r'^dashbord/$', VlidateService, name='dashbord'),
    url(r'^list_service/$', list_service, name='list'),

]
