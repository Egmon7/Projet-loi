from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from .models import Loi, ConferencePresident, ConferenceLois, Pleniere, Vote, Notification, Depute
from .permissions import IsPresidentOrReadOnly, IsDeputeOrReadOnly
from .serializers import (
    LoiSerializer, ConferencePresidentSerializer, ConferenceLoisSerializer,
    PleniereSerializer, VoteSerializer, NotificationSerializer, DeputeSerializer
)
from app.permissions import IsConseillerPrincipal
from .utils.auth import token_required
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
class DeputeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Depute.objects.all()
    serializer_class = DeputeSerializer
    permission_classes = [AllowAny]
class LoisViewSet(viewsets.ModelViewSet):
    queryset = Loi.objects.all()
    serializer_class = LoiSerializer
    permission_classes = [IsAuthenticated, IsDeputeOrReadOnly]
    parser_classes = [MultiPartParser, FormParser] 

class ConferencePresidentViewSet(viewsets.ModelViewSet):
    queryset = ConferencePresident.objects.all()
    serializer_class = ConferencePresidentSerializer
    permission_classes = [IsAuthenticated, IsPresidentOrReadOnly]

class ConferenceLoisViewSet(viewsets.ModelViewSet):
    queryset = ConferenceLois.objects.all()
    serializer_class = ConferenceLoisSerializer
    permission_classes = [IsAuthenticated, IsPresidentOrReadOnly, IsConseillerPrincipal]

class PleniereViewSet(viewsets.ModelViewSet):
    queryset = Pleniere.objects.all()
    serializer_class = PleniereSerializer
    permission_classes = [IsAuthenticated, IsPresidentOrReadOnly]

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated, IsPresidentOrReadOnly]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsPresidentOrReadOnly]

class TestProtectedView(APIView):
    @token_required
    def get(self, request):
        serializer = DeputeSerializer(request.user)
        return Response({
            'message': f'Salut {request.user.prenom} {request.user.nom} ! Tu es bien authentifié.',
            'user': serializer.data
        })

class LoginView(APIView):
    permission_classes = []  # Permet l'accès sans authentification
    authentication_classes = []  # Désactive l'authentification pour cette vue

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = Depute.objects.get(email=email)  # Corrigé ici
            if check_password(password, user.password):
                user.statut = True
                user.save(update_fields=['statut'])

                payload = {
                    'id': user.id,
                    'email': user.email,
                    'role': user.role,
                    'nom': user.nom,
                    'prenom': user.prenom,
                    'postnom': user.postnom,
                    'sexe': user.sexe,
                    'circonscription': user.circonscription,
                    'partie_politique': user.partie_politique,
                    'poste_partie': user.poste_partie,
                    'direction': user.direction,
                    'groupe_parlementaire': user.groupe_parlementaire,
                    'statut': user.statut,
                    'exp': datetime.utcnow() + timedelta(hours=24),
                }
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
                return Response({
                    'token': token,
                    'role': user.role,
                    'user': DeputeSerializer(user).data
                }, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Mot de passe incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
        except Depute.DoesNotExist:
            return Response({'detail': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)