from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Vehiculo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.CharField(null=False, blank=False, max_length=155)
    license_plate = models.CharField(null=False, blank=False, max_length=155)
    seats = models.IntegerField(null=False, blank=False)
    year = models.IntegerField(null=True, blank=True)
    operational = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    
    class Meta:
        ordering = ['license_plate', 'year', 'model']
    
    def save(self, *args, **kwargs):
        self.license_plate = self.license_plate.upper()
        self.model = self.model.upper()
        return super(Vehiculo, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s" % (self.license_plate, self.year, self.model)

    