from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30,default=None)
    email = models.EmailField(max_length=30,default=None)
    mobile = models.BigIntegerField(default=0)
    subject = models.CharField(max_length=30,default=None)
    password = models.CharField(max_length=30,default=None)
