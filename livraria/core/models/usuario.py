from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nome = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)