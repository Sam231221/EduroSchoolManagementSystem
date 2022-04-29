from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

app_name='Dashboard'

urlpatterns = [
 
    #re_path(r"^$", login_required(TemplateView.as_view(template_name='base.html')), name="home-view"),
  path("", login_required(TemplateView.as_view(template_name='dashboard/dashbase.html')), name="dashboard-view"),
  path("charts/", TemplateView.as_view(template_name='dashboard/charts/chartjs.html'), name="standardcharts-view"),
  path("apexcharts/", TemplateView.as_view(template_name='dashboard/charts/apexcharts.html'), name="apexcharts-view"),
  path("echarts/", TemplateView.as_view(template_name='dashboard/charts/echarts.html'), name="echarts-view"),
  
  path("userprofile/", TemplateView.as_view(template_name='dashboard/personal/userprofile.html'), name="userprofile-view"),
  path("contact/", TemplateView.as_view(template_name='dashboard/personal/contact.html'), name="contact-view"),

]
