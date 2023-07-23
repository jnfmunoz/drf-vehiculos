from django.shortcuts import redirect, render
from . import models
from .forms import VehiculoForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission

# Create your views here.
@permission_required('vehiculo.add_vehiculo')
def new_vehiculo(request):
    data = { 
        'form': VehiculoForm() 
    }
    
    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
        else:
            data["form"] = formulario
    return render(request, 'vehiculo/new_vehiculo.html', data)

@login_required
def list_vehiculo(request):
    vehiculos = models.Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    for vehiculo in vehiculos:
        if vehiculo.precio < 10000:
            vehiculo.condicion_precio = 'Bajo'
        elif vehiculo.precio >= 10000 and vehiculo.precio < 30000:
            vehiculo.condicion_precio = 'Medio'
        else:
            vehiculo.condicion_precio = 'Alto'
    return render(request, 'vehiculo/list_vehiculo.html', context)