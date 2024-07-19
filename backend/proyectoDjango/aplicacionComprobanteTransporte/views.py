from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response

from .serializer import UserSerializer, ClienteLoginSerializer, ClienteSerializer


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


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
@api_view(['POST'])
def cliente_login(request):
    serializer = ClienteLoginSerializer(data=request.data)
    if serializer.is_valid():
        cliente = serializer.validated_data
        token, created = Token.objects.get_or_create(user=cliente)
        return Response({'token': token.key})
    return Response(serializer.errors, status=400)