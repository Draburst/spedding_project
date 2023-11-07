from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, EmailInput
import sys

# Add the directory containing module1.py to sys.path
sys.path.append('C:/Users/User/spedding_project/spending/spending/main/')
sys.path.append('C:/Users/lapch/goiteens/spedding_project/main/')
from main.models import User


class SignupForm(UserCreationForm):
    email = EmailField(widget=EmailInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
