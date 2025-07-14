from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

# Permission : Président peut tout faire, les autres peuvent juste lire
class IsPresidentOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.role == 'président'

# Permission pour les utilisateurs authentifiés
class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

# Permission : Députés peuvent créer/lire, présidents peuvent tout faire
class IsDeputeOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.role in ['député', 'président']

# Permission pour les Rapporteurs uniquement
class IsRapporteur(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'rapporteur'

# Permission pour le Bureau d'Études uniquement
class IsCommission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'questeur'  # Vérifie si 'questeur' est correct