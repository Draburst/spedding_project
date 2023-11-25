from django.http import JsonResponse
from main.forms import TransactionForm
from .forms import SignupForm
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import jwt
from django.conf import settings
from .login_service import authenticate_user


@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View):
    form_class = SignupForm
    
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Invalid request method'})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        form = self.form_class(data)
        if form.is_valid():
            form.save()
            user = authenticate_user(data['username'], data['password1'])
            payload = {
                'user_id': user.id,
                'username': user.username,
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            return JsonResponse({'message': 'User created Successfully', 'token': token}, status=201)
        else:
            errors = {}
            for field, field_errors in form.errors.items():
                errors[field] = [error for error in field_errors]
            
            if 'birth_date' in errors:
                return JsonResponse({'message': f'{errors}'}, status=422)
            else:
                print(errors)
                return JsonResponse({'message': 'Bad Form request', 'errors': errors}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class CustomLoginView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')
            user = authenticate_user(username, password)
        except:
            return JsonResponse({'message': 'Your password or name is incorrect'}, status=200)

        if user:
            payload = {
                'user_id': user.id,
                'username': user.username,
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            return JsonResponse({'message': 'Login successful', 'token': token}, status=200)
        else:
            return JsonResponse({'message': 'Invalid login credentials'})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Invalid request method'})

        
@method_decorator(csrf_exempt, name='dispatch')
class CreateTransactionView(View):
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            return JsonResponse({'status': 'success', 'transaction_id': transaction.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
        
    
    

