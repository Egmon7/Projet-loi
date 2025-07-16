from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    Depute,
    Loi,
    Vote,
    Pleniere,
    ConferencePresident,
    ConferenceLois,
    AvisBureau,
    Notification
)

class DeputeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depute
        exclude = ['password']  # Exclure password pour la sécurité

class LoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loi
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class PleniereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pleniere
        fields = '__all__'

class ConferencePresidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferencePresident
        fields = '__all__'

class ConferenceLoisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceLois
        fields = '__all__'

class AvisBureauSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvisBureau
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
