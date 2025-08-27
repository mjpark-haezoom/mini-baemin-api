# stores/owner_views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import AllowUserTypes
from stores.serializers import StoreCreateSerializer

# 사장님이 새 가게를 생성하는 API (사장님 전용)
class OwnerStoreCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, AllowUserTypes]
    serializer_class = StoreCreateSerializer