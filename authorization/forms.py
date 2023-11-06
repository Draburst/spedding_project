from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, EmailInput
import sys

<<<<<<< HEAD
# Add the directory containing module1.py to sys.path
sys.path.append('C:/Users/User/spedding_project/spending/spending/main/')
=======
>>>>>>> 49b2d5abfb32e2cbc97dc268c66129195453b95b
sys.path.append('C:/Users/lapch/goiteens/spedding_project/main/')
from main.models import User


class SignupForm(UserCreationForm):
    email = EmailField(widget=EmailInput)

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ['username', 'password', 'email']
        fields = ['username', 'password1', 'password2', 'email']
=======
        fields = ['username', 'password1', 'password2', 'email']

>>>>>>> 49b2d5abfb32e2cbc97dc268c66129195453b95b
