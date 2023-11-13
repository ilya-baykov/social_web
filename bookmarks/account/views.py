from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


# def authentication(request):
#     if request.POST:
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             user = authenticate(request, username=cleaned_data['login'], password=cleaned_data['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Вход выполнен успешно')
#                 else:
#                     return HttpResponse("Что то не так с аккаунтом")
#             else:
#                 return HttpResponse("Неправильный логин")
#     else:
#         form = LoginForm()
#     return render(request, template_name='account/authentication_form.html', context={'form': form})
