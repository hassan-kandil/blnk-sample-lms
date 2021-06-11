from django.urls import path, include
from .api import ProfileViewSet, UserAPI, RegisterAPI, UserListAPI, CurrentUserAPI, AddressViewSet, LogoutView, RefreshTokenView, LoginAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

class CustomDefaultRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = '/?'

router = CustomDefaultRouter()
router.register('api/addresses', AddressViewSet, 'addresses')
router.register('api/profiles', ProfileViewSet, 'profiles')



urlpatterns = [
    path('api/auth/login', LoginAPI.as_view(), name='auth_login'),
    path('api/auth/logout', LogoutView.as_view(), name='auth_logout'),
    path('api/auth/refresh', RefreshTokenView.as_view() ),
    path('api/users/<int:pk>', UserAPI.as_view()),
    path('api/users', UserListAPI.as_view()),
    path('api/auth/me', CurrentUserAPI.as_view()),
    path('api/auth/register', RegisterAPI.as_view()),
    path('', include(router.urls))
]
