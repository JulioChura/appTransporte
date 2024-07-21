from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer, ClienteSerializer


from .models.cliente import Cliente

from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models.cliente import Cliente

# Ver todos los Usuarios /api/usuarios
class UserList(generics.ListCreateAPIView):   
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
#Detalles de usuario /api/usuarios/#
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
#Registro /api/usuarios/registro
class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        user = serializer.save()
        user.is_staff = True  # Asignar el permiso de staff para el inicio de sesion en django
        user.save()


class ClienteCreateView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny] 
