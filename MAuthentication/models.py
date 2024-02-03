from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator,MinValueValidator,MaxValueValidator
Role=(
    ('USER', 'USER'),
    ('AGENT', 'AGENT'),
    ('STAFF', 'STAFF'),
    ('ADMIN', 'ADMIN'),
    ('MENTOR', 'MENTOR'),
    ('TEACHER', 'TEACHER'),
    ('STUDENT', 'STUDENT'),
)


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    is_activated = models.BooleanField(default=False)
    profilePicture = models.ImageField(upload_to="eis/files/%y"
                              ,help_text="Only .png and .jpg are accepted"
                              ,validators=[FileExtensionValidator(".png,.jpg")]
                              ,blank=True,null=True)

    role = models.CharField(max_length=10, choices=Role, null=True)
    bio = models.TextField(default="", blank=True)
    address = models.TextField(default="", blank=True)
    stripeCustomerId = models.CharField(max_length=255, unique=True, null=True,blank=True)
    stripeSubscriptionId = models.CharField(max_length=255, unique=True,  null=True,blank=True)
    stripePriceId = models.CharField(max_length=100,null=True,blank=True)
    stripeCurrentPeriodEnd = models.DateTimeField( max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return self.email


