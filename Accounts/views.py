from django.shortcuts import render
from  .models import User , Service
from django.shortcuts import get_list_or_404
from django_apiview.views import apiview
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import PhoneOTP
from django.http import HttpResponseRedirect
import random
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from Accounts import forms

# Create your views here.
def send_to(request):
    return render(request,'login-layout.html')

@csrf_exempt
def VlidatePhoneSendOTP(request):
    phone_number = request.POST.get('phone')
    captcha_token=request.POST.get('g-recaptcha-response')
    cap_url="https://www.google.com/recaptcha/api/siteverify"
    cap_secret="6Lc-kckZAAAAAG6ckDw19Ul9BfiEMmfJFnQA9Q7X"
    cap_data={
        'secret':cap_secret,
        'response':captcha_token
    }
    cap_server_response=requests.post(url=cap_url,data=cap_data)
    cap_json=json.loads(cap_server_response.text)
    if cap_json['success']==False:
        messages.error(request,'Invalid captcha , try again.')
        return HttpResponseRedirect("/login/")
    if(phone_number):
        phone=str(phone_number)
        key = send_otp(phone)
        user=PhoneOTP.objects.filter(phone=phone)
        if user.exists():
            user = PhoneOTP.objects.filter(phone=phone).update(otp=key)
            print(key)
            import ghasedak
            # message = "hellow : " + str(key)
            # sms = ghasedak.Ghasedak("56712dc685079d74f1acd147fb0e516e7a0d5811ea2f1d17c2cc56b4c54ed77b")
            # sms.send({'message': message, 'receptor': '09330105221', 'linenumber': '300002525'})
            return render(request,"login-otp.html",{'phone_send':phone})


        else:
            if key:
                PhoneOTP.objects.create(
                    phone=phone,
                    otp=key,

                )
                import ghasedak
                # message="hellow : "+key
                # sms = ghasedak.Ghasedak("56712dc685079d74f1acd147fb0e516e7a0d5811ea2f1d17c2cc56b4c54ed77b")
                # sms.send({'message': 'hellow', 'receptor': '09330105221', 'linenumber': '300002525'})
                print(key)
                return render(request,"login-otp.html",{'phone_send':phone})
            else:
                return render(request, "errors.html", {'page': 1, 'error': "the key is not correct buid please try again"})
    else:
        return render(request, "errors.html", {'page': 1, 'error': "شماره وارد شده درست نیست"})



def send_otp(phone):
    if phone:
        key = random.randint(999,9999)
        return key
    else:
        return False

@csrf_exempt
def VlidateOTP(request):
    phone_number = request.POST.get('phone')
    otp_send = request.POST.get('otp')


    if phone_number and otp_send:
        old=PhoneOTP.objects.filter(phone=phone_number)
        user=User.objects.filter(phone=phone_number)

        if old.exists():
            old = old.first()
            otp = old.otp
            if str(otp_send) == str(otp):
                if not user.exists():
                    User.objects.create(
                        phone=phone_number,
                    )
                old.validated = True
                old.save()
                form = forms.ServiceForm()
                request.session['subject'] = 'Service'
                return render(request, 'dashbord.html', {'form': form,'phone_number':phone_number})
                # return render(request,"dashbord.html",{})
            else:
                messages.error(request, 'Username or Password Incorrect!')
                return HttpResponseRedirect("/login/")


        else:
            error = 'Username or Password Incorrect!'
            return render(request, "login-otp.html", {'page': 0, 'errors': error})

    else:
        error = 'Username or Password Incorrect!'
        return render(request, "login-otp.html", {'page': 0, 'errors': error})

@csrf_exempt
def VlidateService(request):
    count_day = request.POST.get('count_day')
    count_internet = request.POST.get('count_internet')
    phone = request.POST.get('phone')
    print(count_day)
    print(count_internet)
    print(phone)

    if request.method == 'POST':
        Service.objects.create(phone=phone,count_day=count_day,count_internet=count_internet)
        return HttpResponseRedirect("/login/")
    else:
        form = forms.ServiceForm()
        request.session['subject'] = 'Service'
        return render(request, 'dashbord.html', {'form': form})

def Dashbord(request):
    phone_number = request.POST.get('phone_number')
    return render(request,'dashbord.html',{'phone_number': phone_number})

def list_service(request):
    service = Service.objects.all()
    return render(request, 'list_service.html', {'service': service})
