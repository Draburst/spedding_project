from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('history/', HistoryViev.as_view(), name='history'),
    path('create_transaction/', CreateTransactionView.as_view()),
    path('search/', SearchTransactionsView.as_view()),
    path('delete_transaction/', DeleteTransactionView.as_view()),
    path('get_profile_info/', UserProfileView.as_view()),
]

