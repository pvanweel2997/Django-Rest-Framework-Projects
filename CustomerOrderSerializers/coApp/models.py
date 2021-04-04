from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)

class Order(models.Model):
    product=models.CharField(max_length=20)
    quantity=models.CharField(max_length=10)
    customer=models.ForeignKey(Customer,related_name='orders',on_delete=models.CASCADE)
