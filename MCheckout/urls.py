from django.urls import path

from . import views

app_name = "Checkout"

urlpatterns = [
    path("checkout/", views.CheckoutView.as_view(), name="checkout-view"),
    path("khalti-verify/", views.KhaltiVerifyView.as_view(), name="khaltiverify-view"),    
    path("payment_successful/", views.PaymentSuccessfulView.as_view(), name="payment-successful-view"),
]
