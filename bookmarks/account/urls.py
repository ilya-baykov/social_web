from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path("login", CustomLoginView.as_view(), name='login'),
    path("logout", auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/',
         TemplateView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path("", dashboard, name='dashboard')
]
