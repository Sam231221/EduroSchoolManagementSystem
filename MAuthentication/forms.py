from django import forms

from .models import User


class SignUpForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'pass', 'type':'password', 'align':'center', 'placeholder':'Enter a password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'pass', 'type':'password', 'align':'center', 'placeholder':'Reenter  the password'}),
    )   
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
   
        widgets = {
            'username': forms.TextInput(attrs={ 'placeholder':'Enter a Username'}),
            'email': forms.EmailInput(attrs={'placeholder':'Provide your Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder':'Enter a Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder':'ReType the Password'}),
                
        }
        
    def clean_username(self):
        name = self.cleaned_data.get('username')
        if len(name)<=3:
            raise forms.ValidationError('Name is too Short')  
        return name 
       

class LogInForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','password']
   
        widgets = {
            'username': forms.TextInput(attrs={ 'placeholder':'Enter you Username'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Enter your Password'}),
        }
        
