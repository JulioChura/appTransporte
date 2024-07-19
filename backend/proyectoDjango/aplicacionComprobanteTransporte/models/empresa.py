from django.db import models

# Create your models here.
# modelo = tabla

class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    Ruc = models.IntegerField()
    Name = models.CharField(max_length=100)
    Adress = models.CharField(max_length=255)
    Contact = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return self.Name