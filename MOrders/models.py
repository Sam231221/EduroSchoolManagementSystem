from decimal import Decimal

from django.conf import settings
from django.db import models
from MAuthentication.models import User
from MCompany.models import Event, Service


class Order(models.Model):
    user = models.ForeignKey(User, related_name='userorders', on_delete=models.SET_NULL, null=True)
    email = models.EmailField(null=True,max_length=254, blank=True)
    address1 = models.CharField(null=True,max_length=250)
    address2 = models.CharField(null=True,max_length=250)
    city = models.CharField(null=True, max_length=100)
    phone = models.CharField(null=True, max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(null=True,max_digits=5, decimal_places=2)
    payment_option = models.CharField(null=True,max_length=200, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return f"Order by {self.user} at {self.date_created}"

    @property
    def totalamount(self):
        return sum([item.totalprice for item in self.orderservice_set.all()] + [item.totalprice for item in self.orderevent_set.all()])

class OrderService(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Service, related_name="orderservices", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Order id {self.id}:{self.order}'

    @property
    def totalprice(self):
        return self.price*self.quantity 

class OrderEvent(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Event, related_name="orderevents", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Order id {self.id}:{self.order}'

    @property
    def totalprice(self):
        return self.price*self.quantity 
