from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserSignUp(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='first name', widget=forms.TextInput(attrs={'class': 'input--style-5', 'name':'first_name'}))
    last_name = forms.CharField(max_length=100, label='last name', widget=forms.TextInput(attrs={'class': 'input--style-5', 'name':'last_name'}))
    username = forms.CharField(max_length=100, label='last name', widget=forms.TextInput(attrs={'class': 'input--style-5', 'name':'username'}))
    password1 = forms.CharField(max_length=100, label='Password', widget=forms.TextInput(attrs={'class': 'input--style-5', 'name':'password1', 'type':'password'}))
    password2 = forms.CharField(max_length=100, label='Confirm password', widget=forms.TextInput(attrs={'class': 'input--style-5', 'name':'password2', 'type':'password'}))
    email = forms.EmailField(required=True, label='email', widget=forms.TextInput(attrs={'class': 'input--style-5', 'name':'email'}))
    telephone = forms.CharField(max_length=11, label='telephone', widget=forms.TextInput(attrs={'class': 'input--style-5', 'name':'phone'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'telephone', 'password1', 'password2')