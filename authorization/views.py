from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SignupForm
from django.views.generic import TemplateView
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View):
    form_class = SignupForm
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return JsonResponse({'form': form.as_table()})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        form = self.form_class(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User created Successfully'}, status=201)
        else:
            errors = {}
            for field, field_errors in form.errors.items():
                errors[field] = [error for error in field_errors]
            
            if 'birth_date' in errors:
                return JsonResponse({'message': 'Помилка в даті'}, status=422)
            else:
                print(errors)
                return JsonResponse({'message': 'Помилка валідації форми', 'errors': errors}, status=400)


class CustomLoginView(LoginView):
    def form_invalid(self, form):
        response_data = {
            'success': False,
            'errors': {}
        }

        for field, errors in form.errors.items():
            response_data['errors'][field] = [str(error) for error in errors]

        return JsonResponse(response_data, status=400)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            request._body = json.dumps(data).encode('utf-8')
        except json.JSONDecodeError:
            response_data = {
                'success': False,
                'errors': {'__all__': ['Invalid JSON format.']}
            }
            return JsonResponse(response_data, status=400)

        return super().post(request, *args, **kwargs)

        
    

