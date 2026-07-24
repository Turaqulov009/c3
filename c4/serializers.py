from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser

class RegisterSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=CustomUser
        fields=["experience","slug","username","email","password","company","salary"]
        read_only_fields=["id","created_at"]

    def create(self,validated_data):
        user=CustomUser.objects.create_user(username=validated_data["username"],email=validated_data["email"],password=validated_data["password"],experience=validated_data["experience"],company=validated_data["company"],salary=validated_data["salary"],slug=validated_data["slug"])
        return user