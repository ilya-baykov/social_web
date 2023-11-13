from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # path('authentication/', authentication, name='authentication'),
    path('authentication/', auth_views.LoginView.as_view(), name='authentication'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),
]
