from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    numero = models.CharField(max_length=50, null=True)
    pays = models.CharField(max_length=101, null=True)

#class Picture(models.Model):
 #   name = models.CharField(max_length=150, null=True)
  #  libelle = models.CharField(max_length=150, null=True)
   # id_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)