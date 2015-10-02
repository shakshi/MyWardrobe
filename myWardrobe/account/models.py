from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
  GENDER_CHOICES=[('M','Male'),('F','Female')]
  gender=models.CharField(max_length=1,choices=GENDER_CHOICES,default='F')
  
  def __str__(self):
    return self.username;

