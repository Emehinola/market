from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# overriding django default User model
class User(AbstractUser):
    telephone = models.CharField(unique=True, max_length=11)