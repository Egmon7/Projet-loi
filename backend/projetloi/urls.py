from django.contrib import admin
from django.urls import path, include
from app.views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView  

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # ✅ personnalisé
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='login-depute'),
    path('api/', include('app.urls')),
]