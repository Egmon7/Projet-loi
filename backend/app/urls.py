from rest_framework.routers import DefaultRouter
from django.urls import path, include
from app.views import TestProtectedView
from .views import (
    LoisViewSet, ConferencePresidentViewSet, PleniereViewSet,
    VoteViewSet, NotificationViewSet, ConferenceLoisViewSet,LoginView
)
from .views import DeputeViewSet

router = DefaultRouter()
router.register(r'lois', LoisViewSet)
router.register(r'conferences', ConferencePresidentViewSet)
router.register(r'plenieres', PleniereViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'conferences-lois', ConferenceLoisViewSet)
router.register(r'deputes', DeputeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('test-auth/', TestProtectedView.as_view(), name='test_auth'),
]