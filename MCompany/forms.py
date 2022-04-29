from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['user', 'name','opening_time', 'closing_time', 'office_number' , 'thumbnail', 'membership', ]

#ust render datetimefield
