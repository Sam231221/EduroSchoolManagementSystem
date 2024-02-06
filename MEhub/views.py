from django.shortcuts import render
from django.views.generic import  View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from django.urls import reverse_lazy
from .forms import StudentForm



class HomeView(View):
    def get(self, request):
        context={}
        return render(request,'dashboard.html', context)


class StudentListView(ListView):
    model = Student
    template_name = '1.main/student/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = '1.main/student/student_details.html'
    print("IN")


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = '1.main/student/student_form.html'
    success_url = reverse_lazy('MEhub:student-list-view')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = '1.main/student/student_form.html'
    success_url = reverse_lazy('MEhub:student-list-view')
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the available section options from wherever they are defined
        # For example, if you have them in a list or queryset, you can do:

        context['section_options'] = [('B', 'B'), ('A', 'A'), ('C', 'C')]
        return context

    def form_valid(self, form):
        # Save the form and redirect
        # self.object = form.save(commit=True)
        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')





class TeacherListView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/teacher/teachers.html', context)

class TeacherEditView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/teacher/edit-teacher.html', context)
class TeacherAddView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/teacher/add-teacher.html', context)

class TeacherDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id



class SubjectListView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/subject/subjects.html', context)

class SubjectEditView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/subject/edit-subject.html', context)

class SubjectAddView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/subject/add-subject.html', context)

class SubjectDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id



class InvoiceListView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/invoice/invoices.html', context)


class InvoiceEditView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/invoice/edit-invoice.html', context)


class InvoiceAddView(View):
    def get(self, request):
        context={}
        return render(request,'1.main/invoice/add-invoice.html', context)


class InvoiceDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id




