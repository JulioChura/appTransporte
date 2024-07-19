from django.db import models

class Conductor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, blank=False, max_length=155)
    surName = models.CharField(null=False, blank=False, max_length=155)
    DNI = models.IntegerField(null=True, blank=True, default=0)
    adress = models.CharField(null=False, blank=False, max_length=155)
    phoneNumber = models.IntegerField(null=True, blank=True, default=0)
    licenseType = models.CharField(null=False, blank=False, max_length=5)
    created_at = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)
    
    
    class Meta:
        ordering = ['name', 'surName', 'DNI']
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.surName = self.surName.upper()
        self.adress = self.adress.upper()
        return super(Conductor, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s" % (self.name, self.surName, self.DNI)