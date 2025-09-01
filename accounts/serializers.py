# accounts/serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "user_type", "phone_number"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        validated_data['is_active'] = True
        validated_data['password'] = make_password(validated_data['password'])

        email = validated_data.get("email")
        password = validated_data.get("password")
        username = validated_data.get("username")
        user_type = validated_data.get("user_type", "consumer")
        phone_number = validated_data.get("phone_number")

        user = User.objects.create_user(
            email=email,
            password=password,
            username=username,
            user_type=user_type,
            phone_number=phone_number
        )
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password) # save hash
        instance.save()
        return instance

class LoginSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        data = super().validate(attrs)
        # Add user_type to the token payload
        data["user_type"] = self.user.user_type
        return data