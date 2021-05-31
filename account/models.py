from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    birth_day = models.DateField('Data de Nascimento', blank=True, null=True)


