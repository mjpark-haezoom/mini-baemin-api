# accounts/views_operator.py

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import AllowUserTypes
from .serializers import OperatorLoginSerializer


class OperatorLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = OperatorLoginSerializer


class OperatorView(APIView):  # 운영자
    """Permission class to allow access only to users with the 'operator' type."""

    permission_classes = [IsAuthenticated, AllowUserTypes]

    def get(self, request):
        return Response({"message": "Welcome, 운영자님!"})
