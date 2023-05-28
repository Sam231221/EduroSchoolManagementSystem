from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'Basket'

urlpatterns = [
    path('your-basket/',login_required(views.UserCartView.as_view()),name="basket-view"),
    path('add/', views.BasketAddView.as_view(), name='basket-add-view'),
    path('update/', views.BasketUpdateView.as_view(), name='basket-update-view'),
    path('delete/', views.BasketDeleteView.as_view(), name='basket-delete-view'),
    
]
