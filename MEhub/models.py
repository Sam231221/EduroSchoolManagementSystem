from django.db import models
from MAuthentication.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator,MinValueValidator,MaxValueValidator
import uuid
# Create your models here.
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
    files = models.ImageField(upload_to="eis/files/%y"
                              ,help_text="Only .pdf are accepted"
                              ,validators=[FileExtensionValidator(".pdf")]
                              ,blank=True,null=True)

