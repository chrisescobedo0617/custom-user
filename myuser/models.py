from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(max_length=240)
    age = models.IntegerField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)