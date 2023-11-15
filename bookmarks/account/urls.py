from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path("login", CustomLoginView.as_view(), name='login'),
    path("logout", auth_views.LogoutView.as_view(), name='logout'),
    path("", dashboard, name='dashboard')
]
