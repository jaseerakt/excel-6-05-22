from django.db import models

# Create your models here.
class Customer(models.Model):
    customer =  models.CharField(max_length=200, default="")
