from django.http import JsonResponse
from django.views import View
import json

import jwt
from main.db_communicate import get_transactions_by_day, get_user_transactions

from spending.settings import SECRET_KEY
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import *
from django.core.serializers import serialize

@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
        
    def post(self, request):
        print('Hello')
        
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        token = data['token']
        print(token)
        jwt_data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        print(jwt_data)
        user = User.objects.get(pk=jwt_data['user_id'])
        transaction_data = get_user_transactions(jwt_data['user_id'])

        data = {
            'message': 'User has found successfully',
            'balance': user.balance,
            'transactions': transaction_data
        }
        print(data)
        
        return JsonResponse(data, status=200)
        

@method_decorator(csrf_exempt, name='dispatch')
class HistoryViev(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            token = data['token']
            jwt_data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = jwt_data['user_id']   
            transactions = get_transactions_by_day(user_id=user_id)
            print(transactions)
        
            data = {
                'message': 'Transactions retrieved successfully',
                'transactions': transactions
            }

            return JsonResponse(data, status=200)
            
        
        except Exception as error:
            data = {
                'message': f'{error}'
            }
            return JsonResponse(data, status=200)

            
@method_decorator(csrf_exempt, name='dispatch')
class CreateTransactionView(View):
    
    
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        token = data['token']
        jwt_data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = jwt_data['user_id']   
        if data['category'] != 7:
            data['amount'] = -data['amount']
        form = TransactionForm({'amount': data['amount'], 'date': data['date'], 'category': data['category'], 'user': user_id})
        if form.is_valid():
            transaction = form.save()
            return JsonResponse({'message': 'Success creating', 'transaction_id': transaction.id}, status=201)
        else:
            return JsonResponse({'message': f'{form.errors}'}, status=400)