from rest_framework import serializers
from .models import Depute, Loi, Vote, Pleniere, ConferencePresident, ConferenceLois, AvisBureau, Notification

# backend/app/serializers.py
class DeputeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    billsProposed = serializers.IntegerField(default=0)
    participationRate = serializers.FloatField(default=0)

    class Meta:
        model = Depute
        fields = [
            'id', 'nom', 'postnom', 'prenom', 'email', 'sexe', 'circonscription',
            'role', 'partie_politique', 'poste_partie', 'direction',
            'groupe_parlementaire', 'statut','password', 'billsProposed', 'participationRate'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Depute(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

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
    metadata = serializers.JSONField(default=dict)

    class Meta:
        model = Notification
        fields = '__all__'
