from decimal import Decimal
from statistics import mode
from tkinter.tix import Tree
from unicodedata import category

from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from MAuthentication.models import User
from MUtilities.models import Membership
from pyexpat import model

SOCIAL_CHOICES=(
    ('Google','Google'),
    ('Facebook', 'Facebook'),
    ('Instagram', 'Instagram'),
    ('Twitter','Twitter'),
)


class Category(models.Model):
    name=models.CharField(null=True, max_length=50)

    def __str__(self) -> str:
        return str(self.name)    

class GymPlan(models.Model):
    name=models.CharField(null=True, max_length=50)
    price = models.DecimalField(max_digits=6,max_length=4,null=True
                                        ,decimal_places=2)
    def __str__(self) -> str:
        return str(self.name)    

class Visitior(models.Model):
    ipaddress = models.CharField(null=True, max_length=100)

    def __str__(self) -> str:
        return str(self.ipaddress)
class Company(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True,help_text=_("Owner of Company:"))
    name =models.CharField(max_length=50, null=True, verbose_name=_("Name of the Company:"))
    thumbnail = models.ImageField(null=True,help_text=_("Provide the image of your Company"))
    email = models.EmailField(null=True,verbose_name=_("Business Email"))
    description = RichTextUploadingField(
        null=True,
        config_name="default",
    ) 
    bookingprice = models.IntegerField(null=True)
    location = models.CharField(null=True, max_length=100)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True)
    followers = models.IntegerField(null=True)
    likes = models.IntegerField(null=True)
    office_number = models.CharField(null=True, max_length=10)
    opening_time = models.TimeField(null=True, help_text=_("At what time your company starts?. Expected in AM"))
    closing_time = models.TimeField(null=True, help_text=_("At what time your company ends?. Expected in PM"))
    date_joined = models.DateTimeField(auto_now_add=True)
    views = models.ManyToManyField(Visitior, blank=True)
    total_views = models.IntegerField(default=0)
    membership = models.ForeignKey(Membership,on_delete=models.SET_NULL ,null=True)
    
    is_active = models.BooleanField(default=False)
   
    def __str__(self):
        return f"{self.name}"

    @property
    def totalviews(self):
        return self.views.count()

    def get_absolute_url(self):
        return reverse("Company:companydetail-view", kwargs={"pk": self.id})

    class Meta:
        verbose_name_plural = _("Companies")
  
class GymMembership(models.Model):
    customer = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True,help_text=_("Owner of Company:"))
    paying_plan =models.ForeignKey(GymPlan, on_delete=models.CASCADE, null=True)
    provider = models.OneToOneField(Company, on_delete=models.CASCADE ,null=True)
    coming_time = models.TimeField(null=True)
    joining_time = models.DateTimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"enrolled by {self.customer}"

AVAILABILITY_CHOICES = (
    ('Booked','Booked'),
    ('Book Now', 'Book Now'),
)
class Booking(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,blank=True,help_text=_("Owner of Company:"))
   #paying_plan =models.ForeignKey(BookingPlan,on_delete=models.SET_NULL, null=True)
    starting_time = models.TimeField(null=True)
    ending_time = models.TimeField(null=True)    
    price = models.DecimalField(max_digits=6,max_length=4, default=100
                                    ,decimal_places=2)
    provider = models.ForeignKey(Company, on_delete=models.CASCADE ,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    availability = models.CharField(default='Book Now', choices=AVAILABILITY_CHOICES, max_length=100, blank=True)

    def __str__(self):
        return f"enrolled by {self.starting_time}"

    class Meta:
        ordering = ('starting_time',)    



# Product Review
RATING=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)
class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    product=models.ForeignKey(Company,on_delete=models.CASCADE, null=True)
    review_text=models.TextField(null=True, editable=False)
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Reviews'


    def __str__(self):
        return f"Reviewed By {self.user}"        
    
    def get_review_rating(self):
        return self.review_rating

class Event(models.Model):
    name = models.CharField(max_length=50, null= True)
    thumbnail = models.ImageField(null=True)
    description = RichTextUploadingField(
        null=True,
        config_name="default",
    )   
    ordered_by = models.ForeignKey(User,related_name='usereventorders' , on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=6,max_length=4, null=True
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)
    
    starting_time = models.DateTimeField(null=True, help_text=_("At what time the event starts?."))
    ending_time = models.DateTimeField(null=True, help_text=_("At what time the event ends?."))
    date_created = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    going = models.PositiveIntegerField(null=True,blank=True)
    total_sits = models.PositiveIntegerField(null=True,validators=[MinValueValidator(1)], help_text=_("Total no of people that can participate in this event."))    
    sits=models.PositiveIntegerField(validators=[MinValueValidator(1)])
    bookmarks = models.ManyToManyField(User, default=None, blank=True)

    def __str__(self):
        return f"{self.name}"

class Service(models.Model):
    name = models.CharField(max_length=50, null= True)
    thumbnail = models.ImageField(null=True)
    description = RichTextUploadingField(
        null=True,
        config_name="default",
    )   
    ordered_by = models.ForeignKey(User,related_name='userserviceorders' , on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    working_hour = models.IntegerField(null=True, help_text=_("Mention in hour."))
    price = models.DecimalField(max_digits=6,max_length=4, null=True
                                ,validators=[MinValueValidator(Decimal('0'))]
                                ,decimal_places=2)    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sits=models.PositiveIntegerField(null=True,validators=[MinValueValidator(1)], help_text=_("No of people enrolling for this service."))
    bookmarks = models.ManyToManyField(User, default=None, blank=True)

    def __str__(self):
        return f"{self.name}"

class ImageAlbum(models.Model):
    image = models.URLField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True,verbose_name="Images")    
    def __str__(self):
        return f"{self.image}"


class SocialLink(models.Model):
    socialtype =models.CharField(null=True, max_length=50, choices=SOCIAL_CHOICES)
    url=models.URLField(null=True, help_text=_("Provide the link of your any social link"))
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.socialtype} of {self.company}"
