from django.urls import path
from .views import (
    ExpenseListView,
    ExpenseEditView,
    ExpenseAddView,
    ExpenseDeleteView,
    SalaryListView,
    SalaryEditView,
    SalaryAddView,
    SalaryDeleteView,
    EventsListView,
    EventsEditView,
    EventsAddView,
    EventsDeleteView,
    ExamListView,
    ExamEditView,
    ExamAddView,
    ExamDeleteView,
    FeesListView,
    FeesEditView,
    FeesAddView,
    FeesDeleteView,
    HolidayListView,
    HolidayEditView,
    HolidayAddView,
    HolidayDeleteView,
    TimetableListView,
    TimetableEditView,
    TimetableAddView,
    TimetableDeleteView,
)

app_name = 'MManagement'  

urlpatterns = [
    # Expense URLs
    path('expenses/', ExpenseListView.as_view(), name='expense-list-view'),
    path('expense/edit/', ExpenseEditView.as_view(), name='expense-edit-view'),
    path('expense/add/', ExpenseAddView.as_view(), name='expense-add-view'),
    path('expense/delete/', ExpenseDeleteView.as_view(), name='expense-delete-view'),

    # Salary URLs
    path('salaries/', SalaryListView.as_view(), name='salary-list-view'),
    path('salary/edit/', SalaryEditView.as_view(), name='salary-edit-view'),
    path('salary/add/', SalaryAddView.as_view(), name='salary-add-view'),
    path('salary/delete/', SalaryDeleteView.as_view(), name='salary-delete-view'),

    # Events URLs
    path('events', EventsListView.as_view(), name='events-list-view'),
    path('events/edit/', EventsEditView.as_view(), name='events-edit-view'),
    path('events/add/', EventsAddView.as_view(), name='events-add-view'),
    path('events/delete/', EventsDeleteView.as_view(), name='events-delete-view'),

    # Exam URLs
    path('exams/', ExamListView.as_view(), name='exam-list-view'),
    path('exam/edit/', ExamEditView.as_view(), name='exam-edit-view'),
    path('exam/add/', ExamAddView.as_view(), name='exam-add-view'),
    path('exam/delete/', ExamDeleteView.as_view(), name='exam-delete-view'),

    # Fees URLs
    path('fees/', FeesListView.as_view(), name='fees-list-view'),
    path('fees/edit/', FeesEditView.as_view(), name='fees-edit-view'),
    path('fees/add/', FeesAddView.as_view(), name='fees-add-view'),
    path('fees/delete/', FeesDeleteView.as_view(), name='fees-delete-view'),

    # Holiday URLs
    path('holidays/', HolidayListView.as_view(), name='holiday-list-view'),
    path('holiday/edit/', HolidayEditView.as_view(), name='holiday-edit-view'),
    path('holiday/add/', HolidayAddView.as_view(), name='holiday-add-view'),
    path('holiday/delete/', HolidayDeleteView.as_view(), name='holiday-delete-view'),

    # Timetable URLs
    path('timetables/', TimetableListView.as_view(), name='timetable-list-view'),
    path('timetable/edit/', TimetableEditView.as_view(), name='timetable-edit-view'),
    path('timetable/add/', TimetableAddView.as_view(), name='timetable-add-view'),
    path('timetable/delete/', TimetableDeleteView.as_view(), name='timetable-delete-view'),
]
