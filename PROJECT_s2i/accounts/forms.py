from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=120, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=120, required=False, help_text='Optional.')
    birthday = forms.DateField(required=False, help_text='Optional. (YYYY-MM-DD)')
    location = forms.CharField(max_length=120, help_text='Required.')
    email = forms.CharField(max_length=120, help_text='Required. Submit a valid email address')
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birthday', 'location', 'password1', 'password2',)
