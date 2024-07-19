from django.db import models
from .empresa import Empresa
from django.contrib.auth.models import User
# Create your models here.
# modelo = tabla

class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DNI = models.IntegerField()
    Cellphone = models.IntegerField()
    TravelDate = models.DateField()
    id_company = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='clientes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True) 
    password = models.CharField(max_length=128)
    
    def __str__(self): 
        return f"{self.Name} {self.LastName}"