from django.db import models
from django.contrib.auth.hashers import make_password, check_password
#----------
from django.contrib.auth.models import User
#-----------
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
    #--------
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 
    #-----------------
    
    def __str__(self):
        return f"{self.Name} {self.LastName}"
    
    def save(self, *args, **kwargs):
        if self.pk is None:  # Solo para nuevos clientes
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def verify_password(self, password):
        return check_password(password, self.password)