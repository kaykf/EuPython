from django.contrib.auth.models import User # type: ignore
from django import forms # type: ignore

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username': 'Login', 'password':'Senha'}