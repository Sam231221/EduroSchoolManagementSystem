from django.shortcuts import render
from django.views.generic import  View


class ExpenseListView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/accounts/expenses/expenses.html', context)

class ExpenseEditView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/accounts/expenses/edit-expenses.html', context)

class ExpenseAddView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/accounts/expenses/add-expenses.html', context)

class ExpenseDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id


class SalaryListView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/accounts/salary/salary.html', context)

class SalaryEditView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/accounts/salary/edit-salary.html', context)
class SalaryAddView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/accounts/salary/add-salary.html', context)

class SalaryDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id

class EventsListView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/events/event.html', context)


class EventsEditView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/events/edit-invoice.html', context)


class EventsAddView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/events/add-events.html', context)


class EventsDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id



class ExamListView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/exams/exam.html', context)

class ExamEditView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/exams/edit-exam.html', context)

class ExamAddView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/exams/add-exam.html', context)

class ExamDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id


class FeesListView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/fees/fees.html', context)

class FeesEditView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/fees/edit-fees.html', context)

class FeesAddView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/fees/add-fees.html', context)

class FeesDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id
    

class HolidayListView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/holiday/holiday.html', context)

class HolidayEditView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/holiday/edit-holiday.html', context)

class HolidayAddView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/holiday/add-holiday.html', context)

class HolidayDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id    
    


class TimetableListView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/timetable/time-table.html', context)

class TimetableEditView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/timetable/edit-time-table.html', context)

class TimetableAddView(View):
    def get(self, request):
        context={}
        return render(request,'2.management/timetable/add-time-table.html', context)

class TimetableDeleteView(View):
    def post(self, request):
       
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
      
        return product_id    