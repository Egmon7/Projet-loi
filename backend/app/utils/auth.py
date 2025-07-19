import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app.models import Depute
from django.http import JsonResponse

class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None
        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = Depute.objects.get(id=payload['id'])
            return (user, None)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expiré')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Token invalide')
        except Depute.DoesNotExist:
            raise AuthenticationFailed('Utilisateur non trouvé')

def token_required(view_func):
    # Garde ton décorateur pour les vues non-DRF si besoin
    from functools import wraps
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'detail': 'Token manquant ou invalide'}, status=401)
        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = Depute.objects.get(id=payload['id'])
            request.user = user
        except jwt.ExpiredSignatureError:
            return JsonResponse({'detail': 'Token expiré'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'detail': 'Token invalide'}, status=401)
        except Depute.DoesNotExist:
            return JsonResponse({'detail': 'Utilisateur non trouvé'}, status=401)
        return view_func(request, *args, **kwargs)
    return wrapped_view