from django.db import models
from django.urls import reverse

# Create your models here.
class Vehiculo(models.Model):

    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    
    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]
    
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    #DateField , DateTimeField

    class Meta:
        managed = True
        db_table = 'vehiculo'

    def get_absoluted_url(self):
        return reverse('vehiculo', args=[str(self.id)])
    
    def __str__(self):
        return f"marca: {self.marca}, modelo: {self.modelo} fecha_creacion: {self.fecha_creacion}, fecha_modificacion: {self.fecha_modificacion}"