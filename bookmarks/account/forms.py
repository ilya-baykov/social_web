from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=35, label="Логин:", widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(max_length=25, label="Пароль:", widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': (
            "Неправильное имя пользователя или пароль :c"
        ),
        'inactive': ("Этот аккаунт больше не активен "),
    }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

