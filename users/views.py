from rest_framework import generics
from .serializers import *
from users.models import CustomUser


class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializers
