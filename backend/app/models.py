from django.db import models
from django.contrib.auth.hashers import make_password, identify_hasher

# Types de notification disponibles
NOTIFICATION_TYPES = [
    ("conference", "Conférence"),
    ("pleniere", "Plénière"),
    ("bill_update", "Mise à jour de loi"),
    ("bureau_etudes", "Bureau d'études"),
]

class Depute(models.Model):
    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sexe = models.CharField(max_length=10)
    circonscription = models.CharField(max_length=100)
    role = models.CharField(max_length=50)  # président, rapporteur, etc.
    partie_politique = models.CharField(max_length=100)
    poste_partie = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)  # Bureau, Comité des sages, etc.
    groupe_parlementaire = models.CharField(max_length=100)
    statut = models.BooleanField(default=True)  # actif/inactif
    password = models.CharField(max_length=128)  # haché automatiquement


    def save(self, *args, **kwargs):
        # Hachage du mot de passe si ce n’est pas déjà fait
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Loi(models.Model):
    sujet = models.CharField(max_length=200)
    exposer = models.TextField()
    piece = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    date_depot = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    study_bureau_analysis = models.JSONField(null=True, blank=True)
    conference_decision = models.JSONField(null=True, blank=True)
    final_result = models.JSONField(null=True, blank=True)
    etat = models.IntegerField()
    status = models.IntegerField(default=0)
    id_depute = models.ForeignKey(Depute, on_delete=models.CASCADE, related_name='lois')

    def __str__(self):
        return self.sujet


class ConferencePresident(models.Model):
    titre = models.CharField(max_length=200)
    date = models.DateTimeField()
    id_loi = models.ForeignKey(Loi, on_delete=models.CASCADE, related_name='conferences_president')

    def __str__(self):
        return self.titre


class ConferenceLois(models.Model):
    id_conference_president = models.ForeignKey(ConferencePresident, on_delete=models.CASCADE, related_name='conference_lois')
    id_loi = models.ForeignKey(Loi, on_delete=models.CASCADE)
    date_conference = models.DateTimeField()


class AvisBureau(models.Model):
    avis = models.CharField(max_length=50)  # Oui, Non
    justification = models.TextField()
    date = models.DateTimeField()
    id_loi = models.ForeignKey(Loi, on_delete=models.CASCADE, related_name='avis_bureau')


class BureauEtude(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom


class Pleniere(models.Model):
    titre = models.CharField(max_length=200)
    date = models.DateTimeField()
    id_loi = models.ForeignKey(Loi, on_delete=models.CASCADE, related_name='plenieres')
    id_conference_president = models.ForeignKey(ConferencePresident, on_delete=models.CASCADE, related_name='plenieres')


class Commission(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom


class Vote(models.Model):
    nombre_oui = models.IntegerField(default=0)
    nombre_non = models.IntegerField(default=0)
    abstention = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    id_loi = models.ForeignKey(Loi, on_delete=models.CASCADE, related_name='votes')
    id_pleniere = models.ForeignKey(Pleniere, on_delete=models.CASCADE, related_name='votes')


class Notification(models.Model):
    message = models.CharField(max_length=255)
    lu = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    id_depute = models.ForeignKey(Depute, on_delete=models.CASCADE, related_name='notifications')
    type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES, null=True, blank=True)
    id_loi = models.ForeignKey(Loi, null=True, blank=True, on_delete=models.SET_NULL, related_name='notifications')
