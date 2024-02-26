from django.shortcuts import render
from django.views.generic import  View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Teacher
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import StudentForm, TeacherForm
from django.http import HttpResponseRedirect


class HomeView(View):
    def get(self, request):
        context={"request":request, "user":self.request.user}
        print(context["user"])
        print(request)
        return render(request,'dashboard.html', context)


class StudentListView(ListView):
    model = Student
    template_name = '1.main/student/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = '1.main/student/student_details.html'


class StudentCreateView(CreateView, LoginRequiredMixin):
    model = Student
    form_class = StudentForm
    template_name = '1.main/student/add_student.html'
    # success_url = reverse_lazy('MEhub:student-list-view')
    
    def form_valid(self, form):
        self.object = form.save()
        success_url = reverse_lazy('MEhub:student-detail-view', args=[self.object.pk])
        return HttpResponseRedirect(success_url)


class StudentUpdateView(UpdateView, LoginRequiredMixin):
    model = Student
    form_class = StudentForm
    template_name = '1.main/student/edit_student.html'
    context_object_name = 'student'
    # success_url = reverse_lazy('MEhub:student-list-view')
    
    def form_valid(self, form):
        self.object = form.save()
        success_url = reverse_lazy('MEhub:student-detail-view', args=[self.object.pk])
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the available section options from wherever they are defined
        # For example, if you have them in a list or queryset, you can do:
        # print(self.model.objects)
        context['section_options'] = [('B', 'B'), ('A', 'A'), ('C', 'C')]
        return context



class StudentDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Student
    template_name = '1.main/student/student_confirm_delete.html'
    success_url = reverse_lazy('MEhub:student-list-view')
    
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_superuser or self.request.user.role == "TEACHER")
    
    
    


class TeacherListView(ListView):
    model = Teacher
    template_name = "1.main/teacher/teacher_list.html"
    context_object_name = 'teachers'


class TeacherEditView(UpdateView, LoginRequiredMixin):
    model = Teacher
    form_class = TeacherForm
    template_name = '1.main/teacher/edit_teacher.html'
    
    def form_valid(self, form):
        self.object = form.save()
        success_url = reverse_lazy('MEhub:teacher-detail-view', args=[self.object.pk])
        return HttpResponseRedirect(success_url)
    

class TeacherAddView(CreateView, LoginRequiredMixin):
    model = Teacher
    form_class = TeacherForm
    template_name = '1.main/teacher/add_teacher.html'
    success_url = reverse_lazy('MEhub:teacher-list-view')
    
    def form_valid(self, form):
        self.object = form.save()
        success_url = reverse_lazy('MEhub:teacher-detail-view', args=[self.object.pk])
        return HttpResponseRedirect(success_url)
    

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = '1.main/teacher/teacher_details.html'
    context_object_name = 'teacher'


class TeacherDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Teacher
    template_name = '1.main/teacher/teacher_confirm_delete.html'
    success_url = reverse_lazy('MEhub:teacher-list-view')
    
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_superuser or self.request.user.role == "TEACHER")



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




