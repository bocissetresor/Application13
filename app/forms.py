from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    numero = forms.CharField(max_length=50)
    pays = forms.CharField(max_length=101)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'numero', 'pays','email', 'password1', 'password2']