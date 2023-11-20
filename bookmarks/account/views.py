from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(requset):
    return HttpResponse("Вы вошли в аккаунт")


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, template_name='account/user_profile.html',
                          context={"user_form": user_form, "profile_form": profile_form, "status": True})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, template_name='account/user_profile.html',
                  context={"user_form": user_form, "profile_form": profile_form, "status": False})


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
            Profile.objects.create(user=new_user)
            template_name = 'account/register_done.html'
            form = new_user
    else:
        form = UserRegistrationForm()
    return render(request, template_name=template_name, context={'form': form})
