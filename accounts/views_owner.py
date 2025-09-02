# accounts/views_owner.py

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import AllowUserTypes
from .serializers import OwnerLoginSerializer, OwnerUserSerializer


class OwnerRegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = OwnerUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OwnerLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = OwnerLoginSerializer

class OwnerView(APIView): # 점주 (사장님)
    """Permission class to allow access only to users with the 'owner' type."""
    permission_classes = [IsAuthenticated, AllowUserTypes]

    def get(self, request):
        return Response({"message": "Welcome, 점주님!"})