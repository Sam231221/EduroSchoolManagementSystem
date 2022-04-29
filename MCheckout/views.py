import datetime

import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import View
from MBasket.basket import Basket
from MCompany.models import Event, Service
from MOrders.models import Order, OrderEvent, OrderService


class CheckoutView(View):
    def get(self, request):
        user_id = request.user.id
        basket = Basket(request)
        
        order_obj, created  = Order.objects.get_or_create(user_id=user_id, complete=False)
        order_id = order_obj.id
        events = Event.objects.all()
        services = Service.objects.all()
        print('amount:',order_obj.totalamount)
        print('basket:', basket)
        for item in basket:
            if item['type'] == 'event':
                OrderEvent.objects.get_or_create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['sits'])
            if item['type'] == 'service':
                OrderService.objects.get_or_create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['sits'])
        
        return render(request, 'checkout.html',{'order':order_obj, 'services':services, 'events':events})


class KhaltiVerifyView(View):

    def get(self, request, *args, **kwargs):
        print('Initaiting Khalti Verificatiion...')

        transaction_id = datetime.datetime.now().timestamp()
        token = request.GET.get("token")
        amount = request.GET.get("amount")
        o_id = request.GET.get("order_id")
        print(token, amount, o_id)

        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "amount": amount
        }
        headers = {
            "Authorization": "Key test_secret_key_de01b0c1f02b48759df0953a0dcfc8f0"
        }
        order = Order.objects.get(user=request.user, complete=False)
        response = requests.post(url, payload, headers=headers)  # sending data to url
        print('response:', response)
        resp_dict = response.json()
        print('res_dict:', resp_dict)
  
        print('Order Amount:', order.totalamount)
        if resp_dict.get("idx"):
            amount = float(int(amount)/100)
            print('amt:', amount)
            if order.totalamount == amount:
                success = True
                order.complete = True
                order.transaction_id = transaction_id
                order.save()
                return JsonResponse({"success": success})

            else:
                success = False
            return JsonResponse({"success": success})
        else:
            return HttpResponse('false')    

class PaymentSuccessfulView(View):
    def get(self, request):
        print('TRIGGERING PAYMENT')
        basket = Basket(request)
        basket.clear()
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

