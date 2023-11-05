from werkzeug.security import check_password_hash
from main.models import User


def authenticate_user(username, password):
    try:
        user = User.objects.get(username=username)

        if check_password_hash(user.password, password):
            return user
        else:
            return False
    except User.DoesNotExist:
        return False
