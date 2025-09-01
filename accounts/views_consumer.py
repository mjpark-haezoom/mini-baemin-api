# accounts/views_consumer.py

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import AllowUserTypes
from .serializers import ConsumerLoginSerializer, ConsumerUserSerializer


class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ConsumerUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = ConsumerLoginSerializer

class ConsumerView(APIView): # 일반 소비자
    """Permission class to allow access only to users with the 'consumer' type."""
    permission_classes = [IsAuthenticated, AllowUserTypes]
    user_type = "consumer"

    def get(self, request):
        return Response({"message": "Welcome!, 고객님"})