from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Order
from django.forms import ModelForm



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'comment'] 
		
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


