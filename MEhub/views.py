from unicodedata import category
from django.shortcuts import render
from django.views.generic import  View

class HomeView(View):
    def get(self, request):
        context={}
        return render(request,'base.html', context)


class StudentListView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/student/students.html', context)

class StudentEditView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/student/edit-student.html', context)

class StudentAddView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/student/add-student.html', context)

class StudentDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id


class TeacherListView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/add-teacher.html', context)

class TeacherEditView(View):
    def get(self, request):
        context={}
        return render(request,'base.html', context)

class TeacherAddView(View):
    def get(self, request):
        context={}
        return render(request,'base.html', context)

class TeacherDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id



class SubjectListView(View):
    def get(self, request):
        context={}
        return render(request,'base.html', context)

class SubjectEditView(View):
    def get(self, request):
        context={}
        return render(request,'base.html', context)

class SubjectAddView(View):
    def get(self, request):
        context={}
        return render(request,'base.html', context)

class SubjectDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id



class InvoiceListView(View):
    def get(self, request):
        context={}
        return render(request,'base.html', context)

class InvoiceEditView(View):
    def get(self, request):
        context={}
        return render(request,'base.html', context)

class InvoiceAddView(View):
    def get(self, request):
        context={}
        return render(request,'base.html', context)

class InvoiceDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id




