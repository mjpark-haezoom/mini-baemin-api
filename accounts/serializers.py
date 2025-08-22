# accounts/serializers.py

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "user_type", "phone_number"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            user_type=validated_data.get("user_type", "comsumer"),
            phone_number=validated_data.get("phone_number")
        )
        return user