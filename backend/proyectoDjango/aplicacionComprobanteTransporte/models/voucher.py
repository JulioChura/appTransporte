from django.db import models
from .cliente import Cliente
from .ruta import Ruta

class Voucher(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vouchers')
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    cost = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Voucher for {self.cliente} on route {self.ruta} costing {self.cost}"