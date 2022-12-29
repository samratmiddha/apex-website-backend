from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    is_head = models.BooleanField()
    email = models.EmailField(max_length=254, null=True, blank=True)
    mobile_number = models.CharField(max_length=15)
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.username}"