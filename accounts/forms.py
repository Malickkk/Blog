from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        ]

        username = forms.Field(widget=forms.TextInput(attrs={
            'class': 'form-control, form-control-user',
            'placeholder': 'Username',
        }))
        first_name = forms.Field(widget=forms.TextInput(attrs={
            'class': 'form-control, form-control-user',
            'placeholder': 'First name',
        }))
        last_name = forms.Field(widget=forms.TextInput(attrs={
            'class': 'form-control, form-control-user',
            'placeholder': 'Last name',
        }))
        email = forms.Field(widget=forms.EmailInput(attrs={
            'class': 'form-control, form-control-user',
            'placeholder': 'Email',
        }))
        password1 = forms.Field(widget=forms.PasswordInput(attrs={
            'class': 'form-control, form-control-user',
            'placeholder': 'Password',
        }), label='Password')
        password2 = forms.Field(widget=forms.PasswordInput(attrs={
            'class': 'form-control, form-control-user',
            'placeholder': 'Confirm Password',
        }), label='Password')


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
