from unicodedata import category
from django.shortcuts import render
from django.views.generic import TemplateView, View
from MCompany.models import Category, Company, Location


class HomeView(View):
    def get(self, request):
        print('name:',request.user.username)
        location_obj = Location.objects.filter(name='Kathmandu').first()
        print(location_obj)
        nearbyCompanies = Company.objects.filter(location=location_obj)
        popularCompanies = Company.objects.order_by('-views')
        context={
            'nearbyCompanies':nearbyCompanies,
            'popularCompanies':popularCompanies
        }
        return render(request,'base.html', context)

