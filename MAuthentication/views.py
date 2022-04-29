
import json
import urllib

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template import loader
from django.template.loader import render_to_string
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import View
from Dpfp.base import GOOGLE_RECAPTCHA_SECRET_KEY
from validate_email import validate_email

#Since we define abstract user with same name it's important to get it from the function
User = get_user_model()

from .emailthreading import EmailThread
from .utils import generate_token

'''
SInce overridding don't use authenticate(),set_password().
DOnt make superuser from the termninal.
'''

class RegistrationView(View):
    def get(self, request):
        return render(request, "authentication/register.html")

    def post(self, request):
        context = {"data": request.POST, "has_error": False}

        email = request.POST.get("email")
        name = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(name, email, password1)
        
        #Recaptcha check
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_dict = {
            'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(recaptcha_dict).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        
        if len(password1) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
            context["has_error"] = True
        if password1 != password2:
            messages.error(request, "Passwords don't match with other.")
            context["has_error"] = True

        if not validate_email(email):
            messages.error(request, "Please provide a valid email")
            context["has_error"] = True
        
        #recaptcha api sends json object with one key'sucsess', It's value is boolean
        if not result['success']:
            messages.error(request, "Recaptcha Failed")
            context["has_error"] = True                

        try:
            if User.objects.get(email=email):
                messages.error(request, "Email is already taken!")
                context["has_error"] = True

        except Exception as identifier:
            pass

        try:
            if User.objects.get(username=name):
                messages.error(request, "Username is taken")
                context["has_error"] = True

        except Exception as identifier:
            pass

        if context["has_error"]:
          # messages.error(request,"Unable to register. Client error!")
            return render(request, "authentication/register.html", context, status=400)

        user = User.objects.create(username=name, email=email, password=password1)
        user.set_password(password1)
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        email_subject = "Active your Account"
        
        template = loader.get_template("authentication/activationlink.txt")
        context={
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": generate_token.make_token(user),
        }
        message=template.render(context)        
        
        '''
           #only string not html
            message = render_to_string(
            "authentication/activationlink.html",
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": generate_token.make_token(user),
            },
        )
        '''

        email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
        email_message.content_subtype='html'
        EmailThread(email_message).start()
        messages.success(request, "Your Account was created succesfully.")

        return redirect("Account:login-view")


class LoginView(View):
    def get(self, request):
        return render(request, "authentication/login.html")

    def post(self, request):
        context = {"data": request.POST, "has_error": False}
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username:
            messages.error(request, "Username is required")
            context["has_error"] = True
        if not password:
            messages.error(request, "Password is required")
            context["has_error"] = True
        
        user = User.objects.filter(username=username).first()
        print(user)
        if not user and not context["has_error"]:
            messages.error(request, "Invalid login")
            context["has_error"] = True

        if not user.is_email_verified:
            messages.error(request, "Email Verification failed!")
            context["has_error"] = True

        if context["has_error"]:
            return render(request, "authentication/login.html", status=401, context=context)
        #
        #authenticate.login(request,user)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, "Logged In Successfully!")
        return redirect("home-view")

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            print('id:',uid)
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.is_email_verified = True
            user.save()
            messages.success(request, "Email verified successfully")
            return redirect("Account:login-view")
        return render(request, "authentication/activate_failed.html", status=401)


def logoutview(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect("Account:login-view")


class RequestResetEmailView(View):
    def get(self, request):
        return render(request, "authentication/request-reset-email.html")

    def post(self, request):
        email = request.POST["email"]

        if not validate_email(email):
            messages.error(request, "Please enter a valid email")
            return render(request, "authentication/request-reset-email.html")

        user = User.objects.filter(email=email)

        if user.exists():
            current_site = get_current_site(request)
            email_subject = "Reset your Password"
            
            #Render Simple string this time
            message = render_to_string(
                "authentication/reset-user-password.html",
                {
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user[0].pk)),
                    "token": PasswordResetTokenGenerator().make_token(user[0]),
                },
            )

            email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])

            EmailThread(email_message).start()

        messages.success(request, "We have sent you an email with instructions on how to reset your password")
        return render(request, "authentication/request-reset-email.html")


class SetNewPasswordView(View):
    def get(self, request, uidb64, token):
        context = {"uidb64": uidb64, "token": token}

        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))

            user = User.objects.get(pk=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.error(request, "Password reset link is invalid. Please request a new one!")
                return render(request, "authentication/request-reset-email.html")

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request, "Invalid link!")
            return render(request, "authentication/request-reset-email.html")

        return render(request, "authentication/set-new-password.html", context)

    def post(self, request, uidb64, token):
        context = {"uidb64": uidb64, "token": token, "has_error": False}

        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if len(password) < 6:
            messages.error(request, "Password should be at least 6 characters long")
            context["has_error"] = True
        if password != password2:
            messages.error(request, "Password don`t match")
            context["has_error"] = True

        if context["has_error"] == True:
            return render(request, "authentication/set-new-password.html", context)

        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))

            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()

            messages.success(request, "Password reset success, you can login with new password!")

            return redirect("Account:login-view")

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request, "Something went wrong!")
            return render(request, "authentication/set-new-password.html", context)
