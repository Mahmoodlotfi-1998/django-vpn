from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class User(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="phone number must enter in format: '+999999999'. up to 14 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    first_login = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.phone)

class PhoneOTP(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="phone number must enter in format: '+999999999'. up to 14 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    otp = models.CharField(max_length=9,blank=True,null=True)
    count = models.IntegerField(default=0,help_text='number of otp sent')
    validated = models.BooleanField(default=False,help_text="if it is true , that means user have ")

    def __str__(self):
        return str(self.phone) + ' is sent ' + str(self.otp)

class Service(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=15)
    count_day = models.IntegerField(null=True)
    count_internet = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.phone)
