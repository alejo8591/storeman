from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    customer = models.ForeignKey(User, blank=True, null=True)
    status_code = models.ForeignKey('StatusCode')
    date_placed = models.DateTimeField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    comments = models.TextField(blank=True)
    products = models.ManyToManyField(Product, through='ProductInOrder')
    
class ProductInOrder(models.Model):
    order = models.ForeignKey('Order')
    product = models.ForeignKey(Product)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField()
    comments = models.TextField()
    
class StatusCode(models.Model):
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=300)
    description = models.TextField()