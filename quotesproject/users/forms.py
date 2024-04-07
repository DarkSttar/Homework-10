from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=60,
                               required=True,
                               widget=forms.TextInput())
    password1 = forms.CharField(
        min_length=5,
        max_length=50,
        required=True,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        min_length=5,
        max_length=50,
        required=True,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']