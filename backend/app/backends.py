from django.contrib.auth.backends import ModelBackend
from .models import Depute

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Depute.objects.get(email=username)
            if user.check_password(password):
                return user
        except Depute.DoesNotExist:
            return None
