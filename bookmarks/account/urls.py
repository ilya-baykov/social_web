from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path("login", CustomLoginView.as_view(), name='login'),
    path("logout", auth_views.LogoutView.as_view(), name='logout'),
    path("password_change", auth_views.PasswordChangeView.as_view(), name='password_change'),
    path("password_change_done", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path("", dashboard, name='dashboard')
]
