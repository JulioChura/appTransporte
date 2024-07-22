from django.db import models
from .conductor import Conductor
from .vehiculo import Vehiculo

class Ruta(models.Model):
    id = models.BigAutoField(primary_key=True)
    startingPlace = models.CharField(null=False, blank=False, max_length=155)
    destinationPlace = models.CharField(null=False, blank=False, max_length=155)
    distance = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    stops = models.IntegerField(null=True, blank=True, default=0)
    drivers = models.ForeignKey(Conductor, on_delete=models.CASCADE, related_name='rutas', default=None, null=True, blank=True)
    vehicles = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='rutas', default=None, null=True, blank=True)
    horario = models.TimeField(null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)     
    created_at = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        ordering = ['startingPlace', 'destinationPlace', 'distance', 'horario', 'fecha']

    def save(self, *args, **kwargs):
        self.startingPlace = self.startingPlace.upper()
        self.destinationPlace = self.destinationPlace.upper()
        return super(Ruta, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s a las %s el %s" % (self.startingPlace, self.destinationPlace, self.distance, self.horario, self.fecha)


