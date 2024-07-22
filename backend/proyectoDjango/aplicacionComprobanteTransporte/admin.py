from django.contrib import admin

# Register your models here.
from .models.vehiculo import Vehiculo
from .models.empresa import Empresa
from .models.cliente import Cliente
from .models.ruta import Ruta
from .models.conductor import Conductor
from .models.voucher import Voucher
# conf de personalizacion para el panel de admi
class EmpresaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ("id", "Ruc", "Name", "Adress", "Contact", "created_at", "updated_at")

class ClienteAmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ("id", "Name", "LastName", "DNI", "Cellphone", "id_company", "created_at", "updated_at", "email", "password")

class VehiculoAdmin(admin.ModelAdmin): 
    readonly_fields = ('created', 'modified')
    list_display = ("id", "model", "license_plate", "seats", "year", "operational", "created", "modified")

class RutaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ("id", "startingPlace", "destinationPlace", "distance", "stops", "drivers", "vehicles", "horario", "fecha", "created_at", "updated_at")
    list_filter = ('drivers', 'vehicles', 'horario', 'fecha')

class ConductorAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ("id", "name", "surName", "DNI", "adress", "phoneNumber", "licenseType", "created_at", "updated_at")

class VoucherAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ("cliente", "ruta", "cost", "created_at", "updated_at")

admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Cliente, ClienteAmin)
admin.site.register(Ruta, RutaAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Voucher, VoucherAdmin)