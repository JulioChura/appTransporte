from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from .empresa import Empresa
class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DNI = models.IntegerField()
    Cellphone = models.IntegerField()
    #TravelDate = models.DateField()
    id_company = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='clientes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=255, unique=True) 
    password = models.CharField(max_length=128)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self): 
        return f"{self.Name} {self.LastName}"
