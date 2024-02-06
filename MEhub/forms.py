from django import forms
from .models import Student
import random, string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "@!._-+&"
    return ''.join(random.choice(char) for char in [characters] * length)

class StudentForm(forms.ModelForm):
    # submit = forms.SubmitField(label='Update Student')
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'roll', 'blood_group',
                  'religion', 'email', 'class_no', 'section', 'admission_id', 'phone', 'photo', 'username', 'parent_name', 'address', 'password']

    def __init__(self, *args, **kwargs):
        # Add Bootstrap grid classes to each field
        section_options = kwargs.pop('section_options', None)
        super().__init__(*args, **kwargs)
        if section_options:
            self.fields['section'].choices = section_options

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
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
