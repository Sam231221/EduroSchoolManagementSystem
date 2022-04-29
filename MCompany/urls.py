from unicodedata import name

from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "Company"

urlpatterns = [
    path("explore/", views.CompanyView.as_view(), name="explore-view"),
    path("companyjsonview/", views.CompanyJsonView.as_view(), name="companyjson-view"),
    path("Pricing/", views.DpfpPricingView.as_view(), name="dpfppricing-view"),
    path('DPfpBusinesForm/', login_required(views.DpfpBusinessFormView.as_view()), name="dpfpbusinessform-view"),
    path("DpfpBusinessCheckout/<int:id>/", views.DpfpBusinessCheckoutView.as_view(), name="dpfpbusinesscheckout-view"),
    path("DpfpBusinessComplete/", views.DpfpBusinessCompleteView.as_view(), name="dpfpbusinesscomplete-view"),
    path('SearchEngineView/', views.SearchEngineView.as_view(), name='searchengine-view'),
    
    path('companydetailview/<int:pk>/', views.CompanyDetailView.as_view(), name="companydetail-view"),
    path('gymmembershipview/',views.GymMembershipView.as_view(), name="gymmembershipform-view"),
    path('gymmembershipsuccess/', views.GymMembershipSuccessView.as_view(), name="gymmembershipsuccess-view"),

    path('bookingcheckout/<int:id>/', views.BookingCheckoutView.as_view(), name="bookingcheckout-view"),
    path('bookingcomplete/', views.BookingCompleteView.as_view(), name="bookingcomplete-view"),
   
   

]
