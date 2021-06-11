
from .models import Address, Profile
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import AddressSerializer, ProfileSerializer, UserSerializer, RegisterSerializer, UserUpdateSerializer, ProfileSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import MyTokenObtainPairSerializer, MyTokenRefreshSerializer
from rest_framework import status


# Register API


class RegisterAPI(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        })


# Get User API

class CurrentUserAPI(generics.RetrieveAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserListAPI(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# class MyTokenRefreshView(TokenRefreshView):
#     serializer_class = MyTokenRefreshSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    persmissions_classes = [IsAuthenticated]
    serializer_class = AddressSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    persmissions_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer


class LogoutView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class RefreshTokenView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            token = RefreshToken(request.headers["Refresh"])

            return Response(
                data={
                    "access": str(token.access_token)
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class LoginAPI(generics.GenericAPIView):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
