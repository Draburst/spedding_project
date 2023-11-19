from django.http import JsonResponse
from django.views import View
import json
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import *
from django.shortcuts import render

from django.core.serializers import serialize

@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
    def get(self, request):
        try:
            user = User.objects.get(pk=request.user.id)

            user_dict = {
                'id': user.id,
                'username': user.username,
            }

            data = {
                'message': 'User has found successfully',
                'user': user_dict,
            }
            
            return JsonResponse(data, status=200)
        
        except Exception as error:
            print(str(error))
            data = {
                'message': str(error),
            }

            return JsonResponse(data, status=500)

        
    def post(self, request):
        
        form = TransactionForm(request.POST)
        
        if form.is_valid:
            transaction = form.save()
            data = {
                'message': 'Transaction created successfully.',
                'transaction_id': transaction.id,
                'transaction_amount': transaction.amount
            }
            return JsonResponse(data, status=201)
        else:
            data = {
                'message': 'Transaction created failed.',
                'transaction_id': transaction.id,
                'transaction_amount': transaction.amount
            }
            return JsonResponse(data, status=400)
        

@method_decorator(csrf_exempt, name='dispatch')
class HistoryViev(View):

    def get(self, request):
        try:
            transactions = Transaction.objects.filter(user=request.user.id)
            transactions_data = serialize('json', transactions)
        
            data = {
                'message': 'Transactions retrieved successfully',
                'transactions': transactions_data
            }

            return JsonResponse(data, status=200)
            
        
        except Exception as error:
            data = {
                'message': f'{error}'
            }

            
            return JsonResponse(data, status=200)

            
