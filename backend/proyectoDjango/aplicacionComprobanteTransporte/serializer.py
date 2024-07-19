from django.contrib.auth.models import User
from rest_framework import serializers

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



class ClienteLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            cliente = Cliente.objects.get(email=data['email'])
        except Cliente.DoesNotExist:
            raise serializers.ValidationError("Email or password is incorrect.")
        
        if not cliente.check_password(data['password']):
            raise serializers.ValidationError("Email or password is incorrect.")
        
        return cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 