from django import forms
from .models import Student, Teacher
import random, string
from django.utils.safestring import mark_safe

def generate_password(length):
    characters = string.ascii_letters + string.digits + "@!._-+&"
    return ''.join(random.choice(char) for char in [characters] * length)

class StudentForm(forms.ModelForm):
    # submit = forms.SubmitField(label='Update Student')
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'roll', 'blood_group',
                  'religion', 'email', 'class_no', 'section', 'admission_id', 'phone', 'photo', 'username', 'parent_name', 
                  'address', 'password', 'bio']

    def __init__(self, *args, **kwargs):
        # Add Bootstrap grid classes to each field
        section_options = kwargs.pop('section_options', None)
        super().__init__(*args, **kwargs)
        if section_options:
            self.fields['section'].choices = section_options

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field.required:
                field.label = mark_safe(field.label +'\t <span class="login-danger">*</span>')
        self.fields['gender'].widget.attrs['class'] += ' select'
        self.fields['religion'].widget.attrs['class'] += ' select'
        self.fields['blood_group'].widget.attrs['class'] += ' select'
        self.fields['class_no'].label = 'Class'
        self.fields['section'].widget.attrs['class'] += ' text-uppercase'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control datetimepicker'
        self.fields['password'].widget.attrs['value'] = generate_password(8)
        self.fields['password'].widget.attrs['value'] = generate_password(8)
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        
        # self.fields['password'].widget.attrs['type'] = 'password'


    def clean(self):
        cleaned_data = super().clean()
        gender = cleaned_data.get('gender')
        photo = cleaned_data.get('photo')
        

        if gender == 'F' and not photo:
            cleaned_data['photo'] = "123123.svg"
        elif not photo:
            cleaned_data['photo'] = "456322.webp"

        return cleaned_data


class TeacherForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput, label='username')
    # password = forms.CharField(widget=forms.TextInput, label='Password')
    # confirm_password = forms.CharField(widget=forms.TextInput, label='Confirm Password')
    class Meta:
        model = Teacher
        # fields = '__all__'

        fields = ['first_name', 'last_name', 'gender', 'photo', 'date_of_birth', 'mobile', 'joining_date',
                  'qualification', 'experience', 'address', 'city', 'state', 'zip_code', 'country',
                  'email', 'username', 'password', 'major_subject', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field.required:
                field.label = mark_safe(field.label +'\t <span class="login-danger">*</span>')

        self.fields['gender'].widget.attrs['class'] += ' select'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control datetimepicker'
        self.fields['joining_date'].widget.attrs['class'] = 'form-control datetimepicker'
        # self.fields['password'].widget.attrs['value'] = generate_password(8)
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['joining_date'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        # self.fields['first_name'].label = mark_safe(self.fields['first_name'].label + '\t <span class="login-danger">*</span>')

    # def clean_confirm_password(self):
    #     password = self.cleaned_data.get('password')
    #     confirm_password = self.cleaned_data.get('confirm_password')
    #     if password and confirm_password and password != confirm_password:
    #         self.add_error('confirm_password', 'Passwords do not match')
    #     return confirm_password
    
    def clean(self):
        cleaned_data = super().clean()
        # self.clean_confirm_password()
        gender = cleaned_data.get('gender')
        photo = cleaned_data.get('photo')
        
        
        if gender == 'F' and not photo:
            cleaned_data['photo'] = "123123.svg"
        elif not photo:
            cleaned_data['photo'] = "456322.webp"
            
        return cleaned_data
