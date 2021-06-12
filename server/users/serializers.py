
from .models import Address, Profile
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['refresh_token'] = str(refresh)
#         data['access_token'] = str(refresh.access_token)

#         # Add extra responses here
#         data['username'] = self.user.username
#         data['groups'] = self.user.groups.values_list('name', flat=True)
#         return data

# class MyTokenRefreshSerializer(TokenRefreshSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = RefreshToken(attrs['refresh'])
#         data['access_token'] = str(refresh.access_token)


#         return data

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

    def to_representation(self, obj):
        return obj.name


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# User Serializer


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    address = AddressSerializer(read_only=True)
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserUpdateSerializer(serializers.ModelSerializer):
    address = AddressSerializer(allow_null=True, required=False)
    # profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name','address')

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        address_data = validated_data.get('address')
        # profile_data = validated_data.get('profile')

        if(address_data):
            address, created = Address.objects.get_or_create(
                user=instance, **address_data)
            if not created:
                instance.address = address

        # profile, created = Profile.objects.get_or_create(user=instance, **profile_data)

        # if not created:
        #     instance.profile = profile

        instance.save()
        return instance


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user

        raise serializers.ValidationError("Incorrect Credentials")
