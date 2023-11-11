from django.urls import path
from .views import MainView, HistoryViev


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('/h/', HistoryViev.as_view(), name='history'),
    path('h/', HistoryViev.as_view(), name='history'),
]