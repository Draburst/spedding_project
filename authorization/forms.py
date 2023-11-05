from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, EmailInput
import sys

sys.path.append('C:/Users/lapch/goiteens/spedding_project/main/')
from main.models import User


class SignupForm(UserCreationForm):
    email = EmailField(widget=EmailInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

