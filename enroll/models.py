from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
