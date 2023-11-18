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
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = '/login'

    def form_valid(self, form):
        super().form_valid(form)
        return JsonResponse({'message': 'User created Successfully'}, status=201)

    def form_invalid(self, form):
        print(form.as_ul())
        print(form.errors)
        for errors in form.errors.values():
            for error in errors:
                messages.warning(self.request, error)


        if 'birth_date' in form.errors:
            return JsonResponse({'message': 'Помилка в даті'}, status=422)
        else:
            return JsonResponse({'message': 'Помилка валідації форми'}, status=400)
        return JsonResponse({'message': 'Помилка валідації форми'}, status=400)

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


