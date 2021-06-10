from django.urls import path, include
from .api import UserAPI, RegisterAPI, UserListAPI, CurrentUserAPI, MyTokenObtainPairView, MyTokenRefreshView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/auth/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/<int:pk>', UserAPI.as_view()),
    path('api/users', UserListAPI.as_view()),
    path('api/auth/me', CurrentUserAPI.as_view()),
    path('api/auth/register', RegisterAPI.as_view()),

]
