from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegister(UserCreationForm):
    username = forms.CharField(max_length=255, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(max_length=255, label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(max_length=255, label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AuthUser(AuthenticationForm):
    username = forms.CharField(max_length=255, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))

    password = forms.CharField(max_length=255, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))