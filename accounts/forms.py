from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import models
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(
        max_length=254, 
        required=True, 
        widget=forms.EmailInput(
            attrs={'placeholder': 'Your email adress'}
        )
    )

    password1 = forms.CharField(
        label='Password',
        help_text=None,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Select a password, at least 6 tokens'}
        )
    )

    password2 = forms.CharField(
        label='Confirm password',
        help_text=None,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm password'}
        )
    )

    username = forms.CharField(
        help_text=None,
        widget=forms.TextInput(
            attrs={'placeholder': 'Alphanumerics, dashes and peiods tokens'}
        )
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# attrs={'placeholder': }