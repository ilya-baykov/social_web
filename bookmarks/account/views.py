from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(requset):
    return HttpResponse("Вы вошли в аккаунт")


def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, template_name='account/user_profile.html', context={"form": form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


def register(request):
    logout(request)
    template_name = 'account/register.html'
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            template_name = 'account/register_done.html'
            form = new_user
    else:
        form = UserRegistrationForm()
    return render(request, template_name=template_name, context={'form': form})
