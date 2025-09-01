# accounts/serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# make_password 임포트를 삭제합니다.
from .models import User, ConsumerUser, OwnerUser, OperatorUser


# Legacy User Serializer (deprecated)
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "user_type", "phone_number"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data.get('username'),
            user_type=validated_data.get("user_type", "consumer"),
            phone_number=validated_data.get("phone_number")
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


# Consumer User Serializer
class ConsumerUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = ConsumerUser
        fields = ["email", "username", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = ConsumerUser.objects.create_user(**validated_data)
        return user


# Owner User Serializer
class OwnerUserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = OwnerUser
        fields = ["phone_number", "username", "password", "business_license", "store_name"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = OwnerUser.objects.create_user(**validated_data)
        return user


# Operator User Serializer
class OperatorUserSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(required=True)

    class Meta:
        model = OperatorUser
        fields = ["employee_id", "username", "password", "department", "position"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = OperatorUser.objects.create_user(**validated_data)
        return user


# Login Serializers
class LoginSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user_type"] = self.user.user_type
        return data


class ConsumerLoginSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user_type"] = "consumer"
        return data


class OwnerLoginSerializer(TokenObtainPairSerializer):
    username_field = "phone_number"

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user_type"] = "owner"
        return data


class OperatorLoginSerializer(TokenObtainPairSerializer):
    username_field = "employee_id"

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user_type"] = "operator"
        return data