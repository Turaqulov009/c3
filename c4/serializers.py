from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=CustomUser
        fields=["id","phone_number","age","bio","slug"]
        read_only_fields=["id"]

    def create(self,validated_data):
        user=CustomUser.objects.create_user(phone_number=validated_data["phone_number"],age=validated_data["age"],bio=validated_data["bio"],slug=validated_data["slug"],username=validated_data["username"])
        return user
        

class LoginSerializers(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
    def validate(self,attrs):
        username=attrs.get("username")
        passwors=attrs.get("password")

        user=authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Username yoki parol xato")
        refresh=RefreshToken.for_user(user)

        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token),
            "username": user.email,
            "email":user.email,
        }


class RefreshSerializers(serializers.Serializer):
    refresh=serializers.CharField()

    def validate(self,attrs):
        refresh_token=attrs.get("refresh")

        try:
            token=RefreshToken(refresh_token)

            return{
                "access":str(token.access_token)
            }
        except TokenError:
            raise serializers.ValidationError("Refresh token yaroqsiz")