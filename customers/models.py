from django.db import models
from django.contrib.auth.models import User
from customers.country import CountryField

class Customer(models.Model):
    user = models.ForeignKey(User)
    address = models.ForeignKey('CustomerAddress')
    phone_number = models.IntegerField(max_length=10)
    
class CustomerAddress(models.Model):
    line_1 = models.CharField(max_length=300)
    line_2 = models.CharField(max_length=300)
    city = models.CharField(max_length=20)
    dpto = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(CountryField, max_length=16)
