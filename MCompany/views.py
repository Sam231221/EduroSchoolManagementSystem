import time

from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView, View
from MUtilities.models import Membership

from MCompany.models import Booking,Location ,Category, Company, Event, GymPlan, Service, User

from .forms import CompanyForm


def convert(time_string):
    date_var = time.strptime(time_string, '%I:%M')

    return date_var

class CompanyView(View):
    def get(self, request):
        categories = Category.objects.all()
        locations = Location.objects.all()
        context={
            'categories':categories,
            'locations':locations,
            'gymcount':Company.objects.filter(category__name__icontains='Gym').count(),
            'futsalcount':Company.objects.filter(category__name__icontains='Futsal').count(),
            'companies': Company.objects.order_by('?'),

        }
        return render(request,'company/explore.html',context)

class CompanyJsonView(View):
    def get(self, request):
        categories = request.GET.getlist('category[]')
        print(categories)
        company_queryset ={}
        if len(categories) > 0:
            company_queryset = Company.objects.filter(category__id__in=categories).distinct()
            print(company_queryset)

        html = render_to_string('utilities/companiesbyfilter.html',{'companies':company_queryset})    
        return JsonResponse({'companies':html}, safe=False)

class CompanyDetailView(View):
    def get(self, request, pk):
        company_obj = Company.objects.filter(id=pk).first()
        events = company_obj.event_set.all()
        services = company_obj.service_set.all()
        bookings = Booking.objects.filter(provider=company_obj).order_by('starting_time')
        context={'company':company_obj,'bookings':bookings, 'events':events,'services':services}       
        return render(request,'company/companydetailview.html',context)    
        
class GymMembershipView(View):
    def get(self, request):
        memberships= GymPlan.objects.all()
        context={'memberships':memberships}
        return render(request, 'company/gymmembershipform.html', context)
    
class GymMembershipSuccessView(View):    
    def get(self, request):
        print('\n hello')
        return JsonResponse({'success':True}, safe=False)

class BookingCheckoutView(View):
    def get(self, request,id):
        booking_obj = Booking.objects.get(id=id)
        context={'booking_obj':booking_obj}       
        return render(request,'booking/bookingcheckoutview.html',context)    

class BookingCompleteView(View):
    def get(self, request):
        getid = request.GET.get("id")
        print(getid, type(getid))
        getcustomer = request.GET.get('customer')
        print('-----------------------')
        print(getcustomer , type(getcustomer))
        booking_obj = Booking.objects.get(id=int(getid))
        print('bk:', booking_obj)
        customer_obj = User.objects.filter(username__icontains = getcustomer).first()
        print(customer_obj)
        booking_obj.customer = customer_obj
        booking_obj.availability = 'Booked'
        booking_obj.save()
        print('Bk:',booking_obj.customer, booking_obj.availability)
        return JsonResponse({'success':True},safe=False)    
       
class SearchEngineView(View):
    def get(self, request):
        print('asd:',request.GET)
        companies = Company.products.filter(name=companyname, location=location)
        if len(companyname) > 0 and len(location) > 0:
            product_list = [] #inititae an empty list
            
            #Append all customer obj into the list using loop.
            for obj in companies:
                item= {
                    'pk': obj.id,
                    'url': obj.get_absolute_url(),
                    'title': obj.title 
                }
                product_list.append(item)
            
            #now attach customer_list  to the response
            response = product_list    
        else:
            response = "Sorry, We don't currently have "+str(companyname)    
            print(response)        
        
        return JsonResponse({'queryset':response}, safe=False)
               
class DpfpPricingView(View):
    def get(self,request):
        memberships= Membership.objects.all()
        
        return render(request, 'dpfppricing.html', {'memberships':memberships})

class DpfpBusinessFormView(View):
    def get(self,request):
        print('user:',request.user.username)
        
        companyform = CompanyForm()
        memberships= Membership.objects.all()
        return render(request, 'dpfpbusinessform.html', {'companyform':companyform, 'memberships':memberships})

    def post(self,request):
        membership_obj= Membership.objects.filter(price =request.POST['membership']).first()
        company_obj =  Company.objects.filter(user=request.user).first()
        if company_obj is None:
            print('type:', request.POST['membership'])
            category_obj = Category.objects.filter(name=request.POST['category']).first()
            print(category_obj)
            Company.objects.create(user=request.user, category=category_obj ,name=request.POST['companyname'], office_number=request.POST['contactnumber'], opening_time=request.POST['openingtime'], closing_time=request.POST['closingtime'], membership=membership_obj, is_active = False)
            messages.success(request, 'Company is succesfullyfor this profile')
            return HttpResponseRedirect(reverse('Company:dpfpbusinesscheckout-view', args=(membership_obj.id,)))
        else:
            messages.error(request, 'Company is already registered for this profile')
            return HttpResponseRedirect(request.META["HTTP_REFERER"])
class DpfpBusinessCheckoutView(View):
    def get(self,request, id):
        company_obj = Company.objects.filter(user=request.user).first()
        membership= Membership.objects.get(pk=id)
        memberships= Membership.objects.all()
        return render(request, 'dpfpbusinesscheckout.html', {'company_obj':company_obj,'membership':membership, 'memberships':memberships})

class DpfpBusinessCompleteView(View):
    def get(self, request):
            token = request.GET.get("token")
            amount = request.GET.get("amount")
            c_id = int(request.GET.get("company_id"))
            print('-----------------------------')
            print('\nId:',c_id)
            url = "https://khalti.com/api/v2/payment/verify/"
            payload = {
                "token": token,
                "amount": amount
            }
            headers = {
                "Authorization": "Key test_secret_key_de01b0c1f02b48759df0953a0dcfc8f0"
            }            
            company_obj = Company.objects.filter(id=c_id ,user=request.user).first()
            print(company_obj)
            company_obj.is_active = True 
            company_obj.save()
            return JsonResponse({'success':True}, safe=False)
  
