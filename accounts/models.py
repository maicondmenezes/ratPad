from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_photo = models.ImageField(upload_to='fotosUser', blank=True)
    pass
