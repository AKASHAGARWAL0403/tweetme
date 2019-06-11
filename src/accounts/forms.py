from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(forms.Form):
    username  = forms.CharField(max_length=150)
    email     = forms.EmailField()
    password  = forms.CharField(max_length = 100 , widget=forms.PasswordInput)
    password2 = forms.CharField(max_length = 100 , label='Confirm Password' , widget = forms.PasswordInput)

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Password must be same')
        return password

    def clean_username(self):
        username  = self.cleaned_data.get('username') 
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError("Username not available")
        return username
    
    def clean_email(self):
        email  = self.cleaned_data.get('email') 
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("Email not available")
        return email
