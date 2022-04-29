from django.shortcuts import render
from django.views.generic import TemplateView, View
from MCompany.models import Company


class HomeView(View):
    def get(self, request):
        print('name:',request.user.username)
        nearbyCompanies = Company.objects.filter(location='Pokhara')
        popularCompanies = Company.objects.order_by('-views')
        context={
            'nearbyCompanies':nearbyCompanies,
            'popularCompanies':popularCompanies
        }
        return render(request,'base.html', context)

