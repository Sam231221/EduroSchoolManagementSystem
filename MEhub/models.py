from django.db import models
from MAuthentication.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone
from MAuthentication.models import User

import uuid


# Create your models here.



class StudentsManager(User):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.role = "STUDENT"
        user.save(using=self._db)
        
        return user




class Student(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    ]
    class_year_choice = [(year, year) for year in range(1, 13)]
    BLOOD_CHOICES = [
        ('B+', 'B+'),
        ('A+', 'A+'),
        ('O+', 'O+'),
        ('Others', 'Others')
    ]
    RELIGION_CHOICES = [
        ('Hindu', 'Hindu'),
        ('Christian', 'Christian'),
        ('Others', 'Others')
    ]
    PROFILE_PIC_DIR = 'student_photos/'

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    roll = models.CharField(max_length=20, blank=True, null=True)
    blood_group = models.CharField(max_length=6, choices=BLOOD_CHOICES)
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES)
    section = models.CharField(max_length=5)
    admission_id = models.CharField(max_length=20, blank=True, null=True)
    parent_name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    photo = models.ImageField(upload_to=PROFILE_PIC_DIR, blank=True, null=True)
    class_no = models.IntegerField(default=1, choices=class_year_choice)

    email = models.EmailField(unique=True)

    objects = StudentsManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'gender']
    


    class Meta:
        ordering = ('class_no', 'section')

    groups = models.ManyToManyField(Group, related_name="student_set")
    user_permissions = models.ManyToManyField(Permission, related_name="student_set")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if self.date_of_birth and self.date_of_birth > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Run full validation before saving
        super().save(*args, **kwargs)

    def get_blood_group_display(self):
        return dict(self.BLOOD_CHOICES).get(self.blood_group)

    def get_religion_display(self):
        return dict(self.RELIGION_CHOICES).get(self.religion)

    @property
    def full_name(self):
        return f"{(self.first_name).capitalize()} {self.last_name.capitalize()}"

    def save_photo(self, photo):
        self.photo.save(photo.name, photo) if photo else setattr(
            self, 'photo', None)

    def delete_photo(self):
        if self.photo:
            self.photo.delete()
            setattr(self, 'photo', None)


class EducationalInstitution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    thumbnail = models.CharField(max_length=255, default="")
    description = RichTextUploadingField(
        null=True,
        config_name="default",
    )
    address = models.TextField(default="")
    type = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=255, default="")
    accreditation_status = models.CharField(max_length=255, default="")
    principal_name = models.CharField(max_length=255, default="")
    principal_email = models.EmailField(default="", unique=True)
    principal_phone_number = models.CharField(max_length=20, default="")
    files = models.ImageField(
        upload_to="eis/files/%y",
        help_text="Only .pdf are accepted",
        validators=[FileExtensionValidator(".pdf")],
        blank=True,
        null=True,
    )
