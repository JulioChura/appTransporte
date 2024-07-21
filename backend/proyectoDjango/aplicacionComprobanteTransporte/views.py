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

from rest_framework.views import APIView
from rest_framework import status


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


# manejar las operaciones del cliente

class ClienteCreateView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny] 

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(f"Intento de login con email: {email}")

        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            clientes = Cliente.objects.filter(email=email)
            print(f"Clientes encontrados: {clientes.count()}")

            if clientes.count() == 0:
                return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

            cliente = clientes.first()
            print(f"Verificando contraseña para cliente: {cliente.email}")

            if cliente.verify_password(password):
                serializer = ClienteSerializer(cliente)
                print("Login exitoso")
                return Response({"message": "Login successful", "cliente": serializer.data}, status=status.HTTP_200_OK)
            else:
                print("Contraseña incorrecta")
                return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            print(f"Error en login: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)