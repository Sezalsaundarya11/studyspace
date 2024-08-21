from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(null=False, unique=True)

    def __str__(self):
        return self.user.username

