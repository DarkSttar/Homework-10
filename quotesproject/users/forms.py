from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=60,
                               required=True,
                               widget=forms.TextInput(attrs={"class":"custom-textinput"}))
    password1 = forms.CharField(
        min_length=5,
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={"class":"custom-textinput"})
    )
    password2 = forms.CharField(
        min_length=5,
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={"class":"custom-textinput"})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
        
    class Meta:
        model = User
        fields = ['username', 'password']
