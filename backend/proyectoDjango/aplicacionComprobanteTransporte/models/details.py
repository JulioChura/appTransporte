from django.db import models
from .voucher import Voucher
from .ruta import Ruta

class Details(models.Model):
    ClientData = models.ForeignKey(Ruta,on_delete=models.CASCADE)
    Name = models.ForeignKey(Voucher,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

