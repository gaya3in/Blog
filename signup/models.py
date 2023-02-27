from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


USERTYPE_CHOICES = (
    ("-----", "-----"),
    ("Patient", "Patient"),
    ("Doctor", "Doctor")
)


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='static/images/')
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True,blank=False)
    address_line1 = models.CharField(max_length=500,blank=True)
    address_city = models.CharField(max_length=50, blank=True)
    address_state = models.CharField(max_length=50, blank=True)
    address_pincode = models.IntegerField(null=True)
    user_type= models.CharField(max_length=50,choices=USERTYPE_CHOICES,default='-----')





