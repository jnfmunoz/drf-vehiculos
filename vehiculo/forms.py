from django import forms
from vehiculo.models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class  Meta:
        model = Vehiculo
        fields = '__all__'
        exclude = ['fecha_modificacion', 'fecha_creacion']