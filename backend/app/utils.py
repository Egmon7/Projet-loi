# app/utils.py
from app.models import Depute
from django.contrib.auth.hashers import check_password

def authenticate_depute(email, password):
    try:
        user = Depute.objects.get(email=email)
    except Depute.DoesNotExist:
        return None

    if check_password(password, user.password):
        return user
    return None
