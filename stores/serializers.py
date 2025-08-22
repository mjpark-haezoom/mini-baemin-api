# stores/serializers.py

from rest_framework import serializers
from .models import Store, Menu

class StoreListSerializer(serializers.ModelSerializer):
    """Serializer for retrieving a list of stores."""
    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'phone_number']

class MenuSerializer(serializers.ModelSerializer):
    """Serializer for retrieving the menu of a specific store."""
    class Meta:
        model = Menu
        fields = ['id', 'name', 'description', 'price']