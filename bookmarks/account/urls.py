from django.urls import path
from .views import *

urlpatterns = [
    path('authentication/', authentication, name='authentication'),
]
