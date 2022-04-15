from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    user_id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    PhoneNumber =models.CharField(max_length=50, unique=True)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, unique=True)
    parmacy = models.CharField(max_length=50)
    date_joined = models.DateTimeField()
    relation = models.CharField(max_length=50)

