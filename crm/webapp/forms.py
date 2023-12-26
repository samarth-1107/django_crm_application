from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Record

# REGISTER/CREATE USER

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2']

# LOGIN USER
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# CREATE RECORD 

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country']

# UPDATE RECORD 

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country']