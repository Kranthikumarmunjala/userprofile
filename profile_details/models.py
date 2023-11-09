from django.db import models


# Create your models here.
class UserProfile(models.Model):
    name=models.CharField(max_length=255, null=True, blank=True)
    email=models.EmailField()
    mobile_number=models.BigIntegerField()
    dob=models.DateField()
    location=models.CharField(max_length=255, null=True, blank=True)