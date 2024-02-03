from django.db import models
from MAuthentication.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import (
    FileExtensionValidator,
    MinValueValidator,
    MaxValueValidator,
)
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
    files = models.ImageField(
        upload_to="eis/files/%y",
        help_text="Only .pdf are accepted",
        validators=[FileExtensionValidator(".pdf")],
        blank=True,
        null=True,
    )


# class Education(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     start_date = models.DateField()
#     end_date = models.DateField()


# class Section(models.Model):
#     name = models.CharField(max_length=100, null=True)


# class Subject(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     class_name = models.CharField(max_length=100, null=True)


# class Class(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     section = models.ForeignKey(Section, on_delete=models.CASCADE)


# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     roll_number = models.CharField(max_length=20)
#     blood_group = models.CharField(max_length=5)
#     profile_pic = models.ImageField(
#         upload_to="student_profile_pics/", blank=True, null=True
#     )
#     class_info = models.ForeignKey(Class, on_delete=models.CASCADE)
#     admission_id = models.CharField(max_length=20)
#     section = models.ForeignKey(Section, on_delete=models.CASCADE)
#     about = models.TextField()
#     mobile = models.CharField(max_length=15)
#     email = models.EmailField()
#     gender = models.CharField(max_length=10)
#     date_of_birth = models.DateField()
#     permanent_address = models.TextField()
#     temporary_address = models.TextField()


# class Employee(models.Model):
#     type = models.CharField(max_length=20)
#     name = models.CharField(max_length=100, null=True)
#     profile_pic = models.ImageField(
#         upload_to="employee_profile_pics/", blank=True, null=True
#     )
#     email = models.EmailField()
#     gender = models.CharField(max_length=10)
#     date_of_birth = models.DateField()
#     joining_date = models.DateField()
#     leave_date = models.DateField(null=True, blank=True)
#     address = models.TextField()
#     phone_number = models.CharField(max_length=15)
#     experience = models.TextField()


# # Similarly, continue modeling other entities in your system...


# class Hostel(models.Model):
#     block = models.CharField(max_length=100, null=True)
#     room_number = models.CharField(max_length=20)
#     room_type = models.CharField(
#         max_length=20,
#         choices=[("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")],
#     )
#     number_of_beds = models.IntegerField()
#     availability = models.BooleanField(default=True)


# class Sports(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     coach_name = models.CharField(max_length=100, null=True)
#     start_year = models.IntegerField()


# class Payment(models.Model):
#     bank_details = models.OneToOneField(BankDetails, on_delete=models.CASCADE)
#     terms_and_conditions = models.TextField()
#     notes = models.TextField()


# class BankDetails(models.Model):
#     account_holder = models.CharField(max_length=100, null=True)
#     bank_name = models.CharField(max_length=100, null=True)
#     ifsc_code = models.CharField(max_length=20)
#     account_number = models.CharField(max_length=20)


# class Invoice(models.Model):
#     invoice_no = models.CharField(max_length=20)
#     issued_date = models.DateField()
#     due_date = models.DateField()
#     name = models.CharField(max_length=100, null=True)
#     tax = models.CharField(
#         max_length=20, choices=[("GST", "GST"), ("VAT", "VAT"), ("None", "None")]
#     )
#     recurring_invoice = models.BooleanField()
#     sign = models.CharField(max_length=100, null=True)


# class Charges(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     type = models.CharField(max_length=100, null=True)


# class Discount(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)


# class InvoiceItem(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     category = models.CharField(max_length=100, null=True)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     discount = models.ForeignKey(Discount, on_delete=models.CASCADE)


# class Fees(models.Model):
#     student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
#     student_name = models.CharField(max_length=100, null=True)
#     gender = models.CharField(max_length=10)
#     fees_type = models.CharField(max_length=100, null=True)
#     fees_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     paid_date = models.DateField()


# class Expenses(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     item_quantity = models.IntegerField()
#     expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     source_of_purchase = models.CharField(max_length=100, null=True)


# class Holiday(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     type = models.CharField(max_length=100, null=True)
#     start_date = models.DateField()
#     end_date = models.DateField()


# class Exam(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     class_name = models.CharField(max_length=100, null=True)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     fees = models.DecimalField(max_digits=10, decimal_places=2)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     event_date = models.DateField()


# class Salary(models.Model):
#     staff_category = models.CharField(max_length=100, null=True)
#     name = models.CharField(max_length=100, null=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)


# class TimeTable(models.Model):
#     teacher_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100, null=True)
#     class_name = models.CharField(max_length=100, null=True)
#     section = models.ForeignKey(Section, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
