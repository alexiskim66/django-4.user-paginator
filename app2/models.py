from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    ages = models.CharField(max_length=10)