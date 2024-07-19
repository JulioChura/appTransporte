from django.db import models
from .cliente import Cliente

class Voucher(models.Model):
    Name = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Cost = models.IntegerField(null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return f"{self.Name} {self.Cost}"