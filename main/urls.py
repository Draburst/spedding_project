from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path('', MainViev.as_view(), name='main'),
    
]
