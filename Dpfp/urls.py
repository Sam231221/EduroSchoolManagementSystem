from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views.generic import TemplateView

admin.site.site_header = "Dpfp Adminsitration"

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path("", include('MAuthentication.urls')),
    path("", include('MEhub.urls', namespace="MEhub")),
    path("", include('MManagement.urls', namespace="MManagement")),
    path("", include('MOthers.urls', namespace="MOthers")),

    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path('socialauth/', include('social_django.urls', namespace='social'))
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
