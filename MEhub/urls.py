
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "MEhub"

urlpatterns = [
    path("", login_required(views.HomeView.as_view()), name="home-view"),  
    
    path("students/", views.StudentListView.as_view(), name="student-list-view"),
    path("students/add", views.StudentCreateView.as_view(), name="student-add-view"),
    path("students/<int:pk>", views.StudentDetailView.as_view(), name="student-detail-view"),
    path("students/<int:pk>/edit", views.StudentUpdateView.as_view(), name="student-edit-view"),
    path("students/<int:pk>/delete",views.StudentDeleteView.as_view() , name="student-delete-view"),  

    path("teachers", views.TeacherListView.as_view(), name="teacher-list-view"),  
    path("teachers/1", views.TeacherEditView.as_view(), name="teacher-edit-view"),  
    path("teachers/add",views.TeacherAddView.as_view() , name="teacher-add-view"),  
    path("teachers/1",views.TeacherDeleteView.as_view() , name="teacher-delete-view"),  
   
    path("subjects", views.SubjectListView.as_view(), name="subject-list-view"),  
    path("subjects/1", views.SubjectEditView.as_view(), name="subject-edit-view"),  
    path("subjects/add",views.SubjectAddView.as_view() , name="subject-add-view"),  
    path("subjects/1",views.SubjectDeleteView.as_view() , name="subject-delete-view"),  
   
    path("invoices/", views.InvoiceListView.as_view(), name="invoice-list-view"),  
    path("invoices/2", views.InvoiceEditView.as_view(), name="invoice-edit-view"),  
    path("invoices/add",views.InvoiceAddView.as_view() , name="invoice-add-view"),  
    path("invoices/2",views.InvoiceDeleteView.as_view() , name="invoice-delete-view"),  
   

]
