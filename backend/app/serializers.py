from rest_framework import serializers
from django.contrib.auth.hashers import check_password
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

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # On va redéfinir validate pour utiliser email au lieu de username
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(self.context['request'], username=email, password=password)
            if not user:
                raise serializers.ValidationError('Email ou mot de passe incorrect.')
        else:
            raise serializers.ValidationError('Email et mot de passe sont requis.')

        # On met dans attrs ce qu'attend la méthode parente (username, password)
        attrs['username'] = email
        attrs['password'] = password

        return super().validate(attrs)