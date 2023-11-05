from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import General_stor


urlpatterns = [
    path('', General_stor.as_view(), name='main'),
]
