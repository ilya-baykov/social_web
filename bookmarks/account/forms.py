from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=35, label="Логин:", widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(max_length=25, label="Пароль:", widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': (
            "Неправильное имя пользователя или пароль :c"
        ),
        'inactive': ("Этот аккаунт больше не активен "),
    }


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        labels = {
            'username': 'Никнейм',
            'first_name': 'Имя:',
            'email': 'Электронная почта',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают")
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Эта почта уже занята :c')
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Электронная почта',
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Эта почта занята другой учётной записью')
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
        labels = {
            'date_of_birth': 'Дата Рождения',
            'photo': 'Фото'
        }
