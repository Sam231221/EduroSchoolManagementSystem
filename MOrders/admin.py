from django.contrib import admin

from MOrders.models import Order, OrderEvent, OrderService

admin.site.register(Order)
admin.site.register(OrderService)
admin.site.register(OrderEvent)
