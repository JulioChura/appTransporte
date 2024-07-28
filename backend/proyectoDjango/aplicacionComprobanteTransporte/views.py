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

from .serializer import *
from .models.ruta import Ruta

from .models.voucher import Voucher

import mercadopago
from django.http import JsonResponse

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
    

# obtener la data de las rutas disponibles
class RutaListView(APIView):
    def get(self, request):
        rutas = Ruta.objects.all()
        serializer = RutaSerializer(rutas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RegisterTripView(APIView):
    def post(self, request):
        cliente_id = request.data.get('cliente_id')
        ruta_id = request.data.get('ruta_id')
        cost = request.data.get('cost')

        if not cliente_id or not ruta_id or not cost:
            return Response({"error": "Todos los campos son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cliente = Cliente.objects.get(id=cliente_id)
            ruta = Ruta.objects.get(id=ruta_id)
            
            # Verificar si el viaje ya está registrado
            if Voucher.objects.filter(cliente=cliente, ruta=ruta).exists():
                return Response({"message": "Este viaje ya ha sido registrado."}, status=status.HTTP_200_OK)
            
            voucher = Voucher.objects.create(cliente=cliente, ruta=ruta, cost=cost)
            serializer = VoucherSerializer(voucher)
            
            return Response({"message": "Viaje registrado exitosamente", "voucher": serializer.data}, status=status.HTTP_201_CREATED)
        except Cliente.DoesNotExist:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Ruta.DoesNotExist:
            return Response({"error": "Ruta no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# historial de viajes
class HistoryTripView(APIView):
    def get(self, request, cliente_id):
        try:
            cliente = Cliente.objects.get(id=cliente_id)
            vouchers = Voucher.objects.filter(cliente=cliente)
            serializer = VoucherSerializer(vouchers, many=True)
            return Response({"vouchers": serializer.data}, status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# apartir de aca se va a la rama principal
# access token de producción
# sdk = mercadopago.SDK("TEST-1462140131147037-072711-23c541a04e4dd7e34c2aa3748ea63d4d-1920731848")
sdk = mercadopago.SDK("APP_USR-1133984688578946-072802-0a0a445f6db252514ec9ca9a5909bc5e-1921641584")
def create_preference(request, precio, ruta, ruta_id, user_id):
    title = ruta.replace('-', ' ').title()
    success_url = f"http://localhost:5173/registrado?ruta={ruta_id}&cost={precio}&user_id={user_id}"

    preference_data = {
        "items": [
            {
                "title": title,
                "quantity": 1,
                "unit_price": float(precio),
            }
        ],
        "metadata": {
            "ruta": ruta_id,
            "user_id": user_id
        },
        "back_urls": {
            "success": success_url,
            "failure": "http://yourdomain.com/failure",
            "pending": "http://yourdomain.com/pending"
        },
        "auto_return": "approved"
    }
    
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    
    return JsonResponse(preference)
