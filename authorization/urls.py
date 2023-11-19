from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignupView, CustomLoginView


urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('signup', SignupView.as_view()),
    path('logout', LogoutView.as_view()),
]