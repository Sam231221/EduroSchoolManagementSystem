from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    is_activated = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.username)
