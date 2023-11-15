from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(requset):
    return HttpResponse("Вы вошли в аккаунт")


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {"section": 'dashboard'})


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
