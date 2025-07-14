# 1. Chemin vers le dossier projet
import os
import sys
import django

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(BASE_DIR)

# 2. Charger le bon settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetloi.settings")

# 3. Initialiser Django
django.setup()

from app.models import Depute
from django.contrib.auth.hashers import make_password

# Liste des députés (bureau + comité des sages)
deputes_bureau = [
    {
        "nom": "Engeba",
        "postnom": "Ntotimbe",
        "prenom": "Prospere",
        "sexe": "masculin",
        "email": "engebaprospere@gmail.com",
        "circonscription": "Lukunga",
        "role": "président",
        "partie_politique": "UNC",
        "poste_partie": "Président",
        "groupe_parlementaire": "UNC-A",
        "direction": "Bureau",
        "statut": "0",
        "password": "motdepasse123"
    },
    {
        "nom": "Tshilumbayi",
        "postnom": "Musawu",
        "prenom": "Jean-Claude",
        "sexe": "masculin",
        "email": "tshilumbayi.jeanclaude@parlement.cd",
        "circonscription": "Funa",
        "role": "1er vice-président",
        "partie_politique": "UDPS",
        "poste_partie": "Vice-président",
        "groupe_parlementaire": "UDPS-A",
        "direction": "Bureau",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Mboso",
        "postnom": "Nkodia Pwanga",
        "prenom": "Christophe",
        "sexe": "masculin",
        "email": "mboso.christophe@parlement.cd",
        "circonscription": "Mont Amba",
        "role": "2e vice-président",
        "partie_politique": "AFDC",
        "poste_partie": "Vice-président",
        "groupe_parlementaire": "AFDC-A",
        "direction": "Bureau",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Djoli",
        "postnom": "Eseng'Ekeli",
        "prenom": "Jacques",
        "sexe": "masculin",
        "email": "djoli.jacques@parlement.cd",
        "circonscription": "Lukunga",
        "role": "rapporteur",
        "partie_politique": "MLC",
        "poste_partie": "Rapporteur",
        "groupe_parlementaire": "MLC-Groupe",
        "direction": "Bureau",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Munongo",
        "postnom": "",
        "prenom": "Dominique",
        "sexe": "féminin",
        "email": "munongo.dominique@parlement.cd",
        "circonscription": "Funa",
        "role": "rapporteur adjoint",
        "partie_politique": "Indépendant",
        "poste_partie": "Adjoint",
        "groupe_parlementaire": "Indépendants",
        "direction": "Bureau",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Polipoli",
        "postnom": "Lunda",
        "prenom": "Chimène",
        "sexe": "féminin",
        "email": "polipoli.chimene@parlement.cd",
        "circonscription": "Tshangu",
        "role": "questeur",
        "partie_politique": "PPRD",
        "poste_partie": "Questeur",
        "groupe_parlementaire": "FCC",
        "direction": "Bureau",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Neema",
        "postnom": "Paininye",
        "prenom": "Grace",
        "sexe": "féminin",
        "email": "neema.grace@parlement.cd",
        "circonscription": "Tshangu",
        "role": "questeur adjoint",
        "partie_politique": "AFDC-A",
        "poste_partie": "Adjoint",
        "groupe_parlementaire": "AFDC-A",
        "direction": "Bureau",
        "statut": 0,
        "password": "motdepasse123"
    },

    # Membres fictifs du Comité des sages
    {
        "nom": "Kabeya",
        "postnom": "Ntumba",
        "prenom": "Paul",
        "sexe": "Masculin",
        "email": "paul.kabeya@assemblee.cd",
        "circonscription": "Tshangu",
        "role": "Président",
        "partie_politique": "UDPS",
        "poste_partie": "Membre",
        "groupe_parlementaire": "CACH",
        "direction": "Comité des sages",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Kalombo",
        "postnom": "Makiese",
        "prenom": "Luc",
        "sexe": "Masculin",
        "email": "luc.kalombo@assemblee.cd",
        "circonscription": "Lukunga",
        "role": "Vice président",
        "partie_politique": "AFDC",
        "poste_partie": "Vice-président",
        "groupe_parlementaire": "AFDC-A",
        "direction": "Comité des sages",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Mbala",
        "postnom": "Ntolo",
        "prenom": "Florence",
        "sexe": "Féminin",
        "email": "florence.mbala@assemblee.cd",
        "circonscription": "Funa",
        "role": "Rapporteur",
        "partie_politique": "PPRD",
        "poste_partie": "Rapporteure",
        "groupe_parlementaire": "FCC",
        "direction": "Comité des sages",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Kasongo",
        "postnom": "Mwene",
        "prenom": "Jean-Pierre",
        "sexe": "Masculin",
        "email": "jeanpierre.kasongo@assemblee.cd",
        "circonscription": "Funa",
        "role": "Membre",
        "partie_politique": "MLC",
        "poste_partie": "Membre",
        "groupe_parlementaire": "Opposition",   
        "direction": "Comité des sages",
        "statut": 0,
        "password": "motdepasse123"
    },
    {
        "nom": "Lukusa",
        "postnom": "Mbuyi",
        "prenom": "Carine",
        "sexe": "Féminin",
        "email": "carine.lukusa@assemblee.cd",
        "circonscription": "Lukunga",
        "role": "Membre",
        "partie_politique": "Indépendant",
        "poste_partie": "Membre",
        "groupe_parlementaire": "Indépendants",
        "direction": "Comité des sages",
        "statut": 0,
        "password": "motdepasse123"
    }
]

# Insertion dans la base de données
for d in deputes_bureau:
    d["password"] = make_password(d["password"])
    obj, created = Depute.objects.get_or_create(email=d["email"], defaults=d)
    if created:
        print(f"✅ Créé : {d['prenom']} {d['nom']}")
    else:
        print(f"⚠️ Existe déjà : {d['prenom']} {d['nom']}")

