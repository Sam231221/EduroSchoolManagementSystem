import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from MCompany.models import Event, Service

from .basket import Basket


class UserCartView(View):
    def get(self, request):
        basket = Basket(request)
        return render(request, 'basketsummary.html', {'basket': basket})

class BasketAddView(View):
    def post(self, request):
        basket = Basket(request)
        data = json.loads(request.body)
       
        if data['type'] =="service":
            serviceId= data['serviceId']
            serviceName = data['serviceName']
            serviceSits = int(data['qty'])
            print('type:', type(serviceSits))
            service_obj = Service.objects.get(id=serviceId,name=serviceName)#type class
            print('event:', service_obj)
            basket.add(product=service_obj,product_type=data['type'],ordered_by=str(request.user), sits=serviceSits)
            return JsonResponse({
                'id':service_obj.id,
                'name':service_obj.name,
                'price':service_obj.price
            },safe=False)

        if data['type'] =="event":
            eventId= data['eventId']
            eventName = data['eventName']
            eventSits = int(data['qty'])
            event_obj = Event.objects.get(id=eventId,name=eventName)#type class
            print('event:', event_obj)
            basket.add(product=event_obj,product_type=data['type'], ordered_by=str(request.user), sits=eventSits)

            return JsonResponse({
                'id':event_obj.id,
                'name':event_obj.name,
                'price':event_obj.price
            }  ,safe=False)                  
                                    

#Shopping Cart
class BasketDeleteView(View):
    def post(self, request):
        print("enetered")
        basket = Basket(request)
        prod_id=int(request.POST['prod_id'])
        basket.delete(product_id=prod_id)
        
        basketqty = basket.__len__()
        print("Updated Basket:", basket.session['skey'])           
        response = JsonResponse({
                'action':'delete',
                'delete_id':prod_id,
                'basketqty':basketqty,
                'basket_subtotal_price': basket.get_subtotal_price()
            }, safe=False)
        return response


class BasketUpdateView(View):
    def post(self, request):
        basket = Basket(request)
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
