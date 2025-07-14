from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.urls import path
from .views import (
    LoisViewSet,
    ConferencePresidentViewSet,
    PleniereViewSet,
    VoteViewSet,
    NotificationViewSet,
    ConferenceLoisViewSet
)

router = DefaultRouter()
router.register(r'lois', LoisViewSet)
router.register(r'conferences', ConferencePresidentViewSet)
router.register(r'plenieres', PleniereViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'conferences-lois', ConferenceLoisViewSet)



urlpatterns = [
    path('', include(router.urls)),
    
]