from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models.cliente import Cliente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # para serializar todos los datos: fields = '__all__'
        fields = ['id','username', 'email', 'password']
    
    #validar la creacion de usuario mediante tokens
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["email", "password", "Name", "LastName", "DNI", "Cellphone", "id_company"]        
        extra_kwargs = {
            'password': {"write_only": True}
        }
        
    def create(self, validated_data):
        cliente = Cliente.objects.create(
            Name=validated_data['Name'],
            LastName=validated_data['LastName'],
            DNI=validated_data['DNI'],
            Cellphone=validated_data['Cellphone'],
            email=validated_data['email'],
            id_company=validated_data['id_company'],
            password=make_password(validated_data['password'])
        )
        return cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 