# accounts/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class UserRegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # return Response(
            #     {
            #         "id":user.id,
            #         "email": user.email,
            #         "username": getattr(user, "username", None)
            #     },
            #     serializer.data, status=status.HTTP_201_CREATED
            # )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)