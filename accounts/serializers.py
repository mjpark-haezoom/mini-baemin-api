# accounts/serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

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
        validated_data['is_active'] = True
        validated_data['password'] = make_password(validated_data['password'])

        email = validated_data.get("email")
        password = validated_data.get("password")
        username = validated_data.get("username")

        user = ConsumerUser.objects.create_user(
            email=email,
            password=password,
            username=username
        )
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
        validated_data['is_active'] = True
        validated_data['password'] = make_password(validated_data['password'])

        phone_number = validated_data.get("phone_number")
        password = validated_data.get("password")
        username = validated_data.get("username")
        business_license = validated_data.get("business_license")
        store_name = validated_data.get("store_name")

        user = OwnerUser.objects.create_user(
            phone_number=phone_number,
            password=password,
            username=username,
            business_license=business_license,
            store_name=store_name
        )
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
        validated_data['is_active'] = True
        validated_data['password'] = make_password(validated_data['password'])

        employee_id = validated_data.get("employee_id")
        password = validated_data.get("password")
        username = validated_data.get("username")
        department = validated_data.get("department")
        position = validated_data.get("position")

        user = OperatorUser.objects.create_user(
            employee_id=employee_id,
            password=password,
            username=username,
            department=department,
            position=position
        )
        return user


# Login Serializers
class LoginSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        data = super().validate(attrs)
        # Add user_type to the token payload
        data["user_type"] = self.user.user_type
        return data


class ConsumerLoginSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        data = super().validate(attrs)
        # Add user_type to the token payload
        data["user_type"] = "consumer"
        return data


class OwnerLoginSerializer(TokenObtainPairSerializer):
    username_field = "phone_number"

    def validate(self, attrs):
        data = super().validate(attrs)
        # Add user_type to the token payload
        data["user_type"] = "owner"
        return data


class OperatorLoginSerializer(TokenObtainPairSerializer):
    username_field = "employee_id"

    def validate(self, attrs):
        data = super().validate(attrs)
        # Add user_type to the token payload
        data["user_type"] = "operator"
        return data