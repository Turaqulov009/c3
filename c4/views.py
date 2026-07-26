from django.shortcuts import render
from .serializers import RegisterSerializers,LoginSerializers,RefreshSerializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

# Create your views here.

class RegisterAPIView(generics.CreateAPIView):
    serializer_class=RegisterSerializers

class ProfileAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        return Response({
            "username":request.user.username,
            "email":request.user.email
        })

class LogoutAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        try:
            refresh_token=request.data["refresh"]
            token=RefreshToken(refresh_token)
            token=blacklist()
            return Response({
            "message":"logout succesfuly"
            })

        except Exception:
            return Response({"message":"invalid"})

class LoginAPIView(APIView):
    def post(self,request):
        serializers=LoginSerializers
        serializers.is_valid(raise_exception=True)
        return Response(serializers.validated_data, status=status.HTTP_200_OK)


class RefreshAPIView(APIView):
    def post(self,request):
        serializers=RefreshSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        return Response(serializers.validated_data)