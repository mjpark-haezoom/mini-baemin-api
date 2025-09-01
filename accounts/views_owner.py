# accounts/views_owner.py

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import AllowUserTypes
from .serializers import LoginSerializer


class OwnerLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

class OwnerView(APIView): # 점주 (사장님)
    """Permission class to allow access only to users with the 'owner' type."""
    permission_classes = [IsAuthenticated, AllowUserTypes]

    def get(self, request):
        return Response({"message": "Welcome, 점주님!"})