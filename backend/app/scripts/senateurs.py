import os
import sys
import django
import random
from django.contrib.auth.hashers import make_password

# Config Django
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetloi.settings")
django.setup()

from app.models import Depute

# --- Données de base ---
prenoms = [
    "Jean", "Alain", "Michel", "David", "Patrick", "Prosper", "Luc", "Serge", "Eric", "André",
    "Marie", "Jeanne", "Chantal", "Clarisse", "Sylvie", "Nadine", "Florence", "Carine", "Esther", "Aline",
    "Paul", "Jacques", "Fabrice", "Grace", "Cédric"
]

noms = [
    "Kalonda", "Mutombo", "Nsimba", "Kabongo", "Mbuyi", "Ndala", "Mpoyi", "Kashama", "Kasongo", "Makiese",
    "Tshibanda", "Ngoy", "Moke", "Tumba", "Kanku", "Mundele", "Lunda", "Mboma", "Kikuni", "Kitoko",
    "Kabila", "Kambale", "Ngandu", "Mukendi", "Mundele"
]

postnoms = [
    "Ilunga", "Kanyinda", "Pwanga", "Nzita", "Muteba", "Mukeba", "Ndombe", "Ngalula", "Tshilombo", "Kabasele",
    "Lukusa", "Kisimba", "Munganga", "Makengo", "Nkenge", "Ndombasi", "Sefu", "Mwene", "Kabuya", "Mabiala",
    "Mbokani", "Luboya", "Ndombo", "Kabeya", "Katumba"
]

circonscriptions = ["Funa", "Lukunga", "Mont Amba", "Tshangu"]
sexes = ["masculin", "féminin"]

partis = [
    "UDPS", "UNC", "PPRD", "AFDC", "MLC", "ECIDé", "MSR", "Envol", "Nouvel Élan", "Indépendant",
    "AA/a", "AAB"
]

groupes = {
    "UDPS": "UDPS-A",
    "UNC": "UNC-A",
    "PPRD": "FCC",
    "AFDC": "AFDC-A",
    "MLC": "MLC-Groupe",
    "ECIDé": "Opposition",
    "MSR": "MSR-A",
    "Envol": "Envol-Groupe",
    "Nouvel Élan": "Élan-National",
    "Indépendant": "Indépendants",
    "AA/a": "Alliance AA",
    "AAB": "Alliance AAB"
}

# --- Génération des sénateurs ---
nb_senateurs = 89
senateurs = []

# Compter combien existent déjà
deja = Depute.objects.count()

for i in range(nb_senateurs):
    prenom = random.choice(prenoms)
    nom = random.choice(noms)
    postnom = random.choice(postnoms)
    sexe = random.choice(sexes)
    circonscription = random.choice(circonscriptions)
    parti = random.choice(partis)
    email = f"{prenom.lower()}.{nom.lower()}{i+deja}@assemblee.cd"
    groupe = groupes.get(parti, "Indépendants")

    d = {
        "nom": nom,
        "postnom": postnom,
        "prenom": prenom,
        "sexe": sexe,
        "email": email,
        "circonscription": circonscription,
        "role": "sénateur",
        "partie_politique": parti,
        "poste_partie": "Membre",
        "groupe_parlementaire": groupe,
        "direction": "Parlementaire",
        "statut": 0,
        "password": make_password("motdepasse123")
    }
    senateurs.append(d)

# Insertion en base
for d in senateurs:
    try:
        Depute.objects.create(**d)
    except Exception as e:
        print(f"Erreur insertion {d['email']}: {e}")

print("✅ 89 sénateurs ajoutés.")
