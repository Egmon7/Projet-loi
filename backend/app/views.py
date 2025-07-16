from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import (
    Loi,
    ConferencePresident,
    ConferenceLois,
    Pleniere,
    Vote,
    Notification
)
from .permissions import IsPresidentOrReadOnly, IsDeputeOrReadOnly
from .serializers import (
    LoiSerializer,
    ConferencePresidentSerializer,
    ConferenceLoisSerializer,
    PleniereSerializer,
    VoteSerializer,
    NotificationSerializer,
    CustomTokenObtainPairSerializer
)

class LoisViewSet(viewsets.ModelViewSet):
    queryset = Loi.objects.all()
    serializer_class = LoiSerializer
    permission_classes = [IsAuthenticated, IsDeputeOrReadOnly]

class ConferencePresidentViewSet(viewsets.ModelViewSet):
    queryset = ConferencePresident.objects.all()
    serializer_class = ConferencePresidentSerializer
    permission_classes = [IsAuthenticated, IsPresidentOrReadOnly]

class ConferenceLoisViewSet(viewsets.ModelViewSet):
    queryset = ConferenceLois.objects.all()
    serializer_class = ConferenceLoisSerializer
    permission_classes = [IsAuthenticated, IsPresidentOrReadOnly]

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