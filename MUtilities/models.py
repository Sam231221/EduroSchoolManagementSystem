from django.db import models
from django.utils.translation import gettext_lazy as _
from MAuthentication.models import User

PAYING_PLAN_CHOICES = (
    ('None', 'None'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),
    ('Yearly', 'Yearly'),
)

class Membership(models.Model):
    name= models.CharField(null=True, max_length=20)
    price = models.DecimalField(max_digits=6,max_length=4, null=True
                                ,decimal_places=2)
    paying_plan = models.CharField(null=True,max_length=50, choices=PAYING_PLAN_CHOICES)                            
    start_countdown =models.DateTimeField(auto_now_add=True)
    end_countdown = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class MemebershipPlan(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE, null=True)
    plan = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.plan)


'''
when start_countdown is equal to endcountdown, deactivate the company or user.
he should not be allowed to take free tier again.For this
we deactivate the company. WHen the user with the same company tries for the free tier again then
check if there already exists membership for this company with type "FREE"
'''


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)  #default is false which means unchecked box
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "Ordered by "+str(self.user)
