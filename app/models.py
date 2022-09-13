from operator import mod
from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_created = models.DateTimeField(auto_now=True)
    is_updated = models.DateTimeField(auto_now=True)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    available = models.CharField(max_length=100)
    is_add_date = models.DateField(auto_now=True)
    is_add_time = models.TimeField(auto_now=True)
    