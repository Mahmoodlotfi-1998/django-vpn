from django.forms import ModelForm
from django import forms
from .models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['phone', 'count_day', 'count_internet', ]

    phone = forms.IntegerField()
    count_day = forms.IntegerField()
    count_internet = forms.IntegerField()
