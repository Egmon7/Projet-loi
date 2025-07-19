from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticated(BasePermission):
    """
    Autorise uniquement les utilisateurs authentifiés.
    Utilisé pour restreindre l'accès aux vues nécessitant une connexion.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsPresidentOrReadOnly(BasePermission):
    """
    Autorise :
    - Les méthodes sécurisées (GET, HEAD, OPTIONS) pour tous.
    - Les méthodes d'écriture (POST, PUT, DELETE) uniquement pour les utilisateurs avec le rôle 'président'.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.role == 'président'


class IsDeputeOrReadOnly(BasePermission):
    """
    Autorise :
    - Les méthodes sécurisées (GET, HEAD, OPTIONS) pour tous.
    - Les méthodes d'écriture (POST, PUT, DELETE) pour les utilisateurs avec les rôles 'député' ou 'président'.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.role in ['député', 'président']


class IsRapporteur(BasePermission):
    """
    Autorise uniquement les utilisateurs avec le rôle 'rapporteur'.
    Utilisé pour les actions réservées aux rapporteurs (ex. : gestion de rapports spécifiques).
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'rapporteur'


class IsCommission(BasePermission):
    """
    Autorise uniquement les utilisateurs avec le rôle 'questeur' (à confirmer si c'est le bon rôle).
    Si la commission inclut d'autres rôles (ex. : 'membre_commission'), ajouter ici.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'questeur'