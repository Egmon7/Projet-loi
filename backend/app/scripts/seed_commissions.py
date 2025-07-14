import os
import sys
import django
from django.contrib.auth.hashers import make_password

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetloi.settings")
django.setup()

from app.models import Depute

# Membres du bureau d'étude
membres_bureau_etude = [
    {
        "nom": "Mwamba",
        "postnom": "Lusamba",
        "prenom": "Jean",
        "sexe": "masculin",
        "email": "jean.mwamba@assemblee.cd",
        "circonscription": "Funa",
        "role": "Conseiller principal",
        "partie_politique": "UDPS",
        "poste_partie": "Membre",
        "groupe_parlementaire": "UDPS-A",
        "direction": "Bureau d’étude",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Kabasele",
        "postnom": "Nkulu",
        "prenom": "Marie",
        "sexe": "féminin",
        "email": "marie.kabasele@assemblee.cd",
        "circonscription": "Lukunga",
        "role": "Conseiller",
        "partie_politique": "PPRD",
        "poste_partie": "Membre",
        "groupe_parlementaire": "FCC",
        "direction": "Bureau d’étude",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Ilunga",
        "postnom": "Kabuya",
        "prenom": "Paul",
        "sexe": "masculin",
        "email": "paul.ilunga@assemblee.cd",
        "circonscription": "Mont Amba",
        "role": "Assistant",
        "partie_politique": "AFDC",
        "poste_partie": "Membre",
        "groupe_parlementaire": "AFDC-A",
        "direction": "Bureau d’étude",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Ngalula",
        "postnom": "Mbuyi",
        "prenom": "Alice",
        "sexe": "féminin",
        "email": "alice.ngalula@assemblee.cd",
        "circonscription": "Tshangu",
        "role": "Analyste",
        "partie_politique": "Indépendant",
        "poste_partie": "Membre",
        "groupe_parlementaire": "Indépendants",
        "direction": "Bureau d’étude",
        "statut": 0,
        "password": "motdepasse123"
    }
]

# Membres des commissions
membres_commission = [
    {
        "nom": "Mbaya",
        "postnom": "Kasongo",
        "prenom": "Robert",
        "sexe": "masculin",
        "email": "robert.mbaya@assemblee.cd",
        "circonscription": "Funa",
        "role": "Président",
        "partie_politique": "MLC",
        "poste_partie": "Président",
        "groupe_parlementaire": "Opposition",
        "direction": "Commission",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Mputu",
        "postnom": "Ndaya",
        "prenom": "Jeanine",
        "sexe": "féminin",
        "email": "jeanine.mputu@assemblee.cd",
        "circonscription": "Lukunga",
        "role": "Vice-président",
        "partie_politique": "UDPS",
        "poste_partie": "Vice-présidente",
        "groupe_parlementaire": "UDPS-A",
        "direction": "Commission",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Kalala",
        "postnom": "Mukuna",
        "prenom": "Anne",
        "sexe": "féminin",
        "email": "anne.kalala@assemblee.cd",
        "circonscription": "Mont Amba",
        "role": "Rapporteur",
        "partie_politique": "PPRD",
        "poste_partie": "Rapporteure",
        "groupe_parlementaire": "FCC",
        "direction": "Commission",
        "statut": 0,
        "password": "motdepasse123"
    }
]

# Fonction d'insertion pour éviter répétition
def inserer_membres(liste):
    for membre in liste:
        membre["password"] = make_password(membre["password"])
        obj, created = Depute.objects.update_or_create(
            email=membre["email"], defaults=membre
        )
        print(f"{'Créé' if created else 'Mis à jour'} : {membre['prenom']} {membre['nom']}")

if __name__ == "__main__":
    inserer_membres(membres_bureau_etude)
    inserer_membres(membres_commission)
    print("\n✅ Insertion/Mise à jour terminée pour bureau d’étude et commissions.")
