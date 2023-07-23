from django.contrib import admin
from .models import Vehiculo

# Register your models here.
class VehiculoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vehiculo, VehiculoAdmin)