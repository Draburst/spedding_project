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


@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View):
    form_class = SignupForm
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return JsonResponse({'form': form.as_table()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
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
        for errors in form.errors.values():
            for error in errors:
                messages.warning(self.request, error)

        return super().form_invalid(form)
        
    

from django.shortcuts import render

#@login_required
#def profile(request):
#    return render(request, 'profile.html')


