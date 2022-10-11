import email
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Contacts(models.Model):
    Name = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    Address = models.CharField(max_length=122)
    Phone = models.CharField(max_length=122)
    Desc = models.CharField(max_length=1022)
    def __str__(self) -> str:
        return self.Name +(" ")+ self.Email

class Signup(models.Model):
    Fname = models.CharField(max_length=122 )
    Lname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122 )
    phone = models.CharField(max_length=122 )
    occupation = models.CharField(max_length=122 )
    city = models.CharField(max_length=122 )
    state = models.CharField(max_length=122 )
    gender = models.CharField(max_length=122 )
    agree =  models.CharField(max_length=122 )        
    def __str__(self) -> str:
        return self.Fname +(" ")+ self.Lname 