from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from MEhub.views import HomeView

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^$", HomeView.as_view(), name="home-view"),  
    path("about/", TemplateView.as_view(template_name='about.html'), name="about-view"),
    path("support/", TemplateView.as_view(template_name='support.html'), name="support-view"),
    path("contact/", TemplateView.as_view(template_name='contact.html'), name="contact-view"),

    path("", include('MAuthentication.urls')),
    path("basket/", include('MBasket.urls')),
    path("", include('MCompany.urls')),
    path("", include('MCheckout.urls')),
    path("dashboard/", include('MDashboard.urls', namespace='Dashboard')),

    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path('socialauth/', include('social_django.urls', namespace='social'))
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
