# accounts/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import LoginSerializer, UserSerializer
from .permissions import IsUserType

class UserRegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class ConsumerView(APIView): # 일반 소비자
    """Permission class to allow access only to users with the 'consumer' type."""
    permission_classes = [IsAuthenticated, IsUserType]
    user_type = 'consumer'

    def get(self, request):
        return Response({"message": "Welcome!, 고객님"})


class OwnerView(APIView): # 점주 (사장님)
    """Permission class to allow access only to users with the 'owner' type."""
    permission_classes = [IsAuthenticated, IsUserType]
    user_type = 'owner'

    def get(self, request):
        return Response({"message": "Welcome, 점주님!"})


class OperatorView(APIView): # 배민 운영자
    """Permission class to allow access only to users with the 'operator' type."""
    permission_classes = [IsAuthenticated, IsUserType]
    user_type = 'operator'

    def get(self, request):
        return Response({"message": "Welcome, 운영자님!"})

