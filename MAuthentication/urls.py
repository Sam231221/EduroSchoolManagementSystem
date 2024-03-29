from django.urls import path, re_path

from . import views

app_name = 'Account'

urlpatterns = [
    path('api/create-user/', views.CreateUserView.as_view(), name='create-user-api-view'),
    re_path(r"^accounts/register/$", views.RegistrationView.as_view(), name="register-view"),
    re_path(r"^accounts/login/$", views.LoginView.as_view(), name="login-view"),
    re_path(r"^accounts/logout/$", views.logoutview, name="logout-view"),
    path("accounts/activate/<uidb64>/<token>/", views.ActivateAccountView.as_view(), name="account-activation-view"),
    path("accounts/set-new-password/<uidb64>/<token>/", views.SetNewPasswordView.as_view(), name="set-new-password-view"),
    re_path(r"^accounts/request-reset-email/$", views.RequestResetEmailView.as_view(), name="request-reset-email-view"),
]
