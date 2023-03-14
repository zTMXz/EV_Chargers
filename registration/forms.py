from django import forms
from .models import Registration
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", 'autofocus': True, 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", 'type':"password", 'placeholder':"Password"}))


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['login', 'password']