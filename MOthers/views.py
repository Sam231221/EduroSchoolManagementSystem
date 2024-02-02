from django.shortcuts import render
from django.views.generic import  View

class HostelView(View):
    def get(self, request):
        context={}
        return render(request,'3.others/hostel/rooms.html', context)

class RoomEditView(View):
    def get(self, request):
        context={}
        return render(request,'3.others/hostel/edit-room.html', context)

class RoomAddView(View):
    def get(self, request):
        context={}
        return render(request,'3.others/hostel/add-room.html', context)

class RoomDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id


class SportListView(View):
    def get(self, request):
        context={}
        return render(request,'3.others/sports/sports.html', context)

class SportEditView(View):
    def get(self, request):
        context={}
        return render(request,'3.others/sports/edit-sports.html', context)
class SportAddView(View):
    def get(self, request):
        context={}
        return render(request,'3.others/sports/add-sports.html', context)

class SportDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id



class TransportListView(View):
    def get(self, request):
        context={}
        return render(request,'3.others/transport/transport.html', context)

class TransportEditView(View):
    def get(self, request):
        context={}
        return render(request,'3.others/transport/edit-transport.html', context)

class TransportAddView(View):
    def get(self, request):
        context={}
        return render(request,'3.others/transport/add-transport.html', context)

class TransportDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id

