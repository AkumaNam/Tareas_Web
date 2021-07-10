from django.db import models
from django.contrib.auth.models import User

from django.db.models.fields import BooleanField, DateField, DateTimeField

# Create your models here.
#Nombre, Apellido, Dirección, Fecha de nacimiento, Teléfono y Correo
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank= False, null=False)
    telefono = models.IntegerField()
    correo = models.EmailField()

    def __str__(self) -> str:
        return f'Cliente {self.nombre} {self.apellido}'

class Cuentas(models.Model):
    fecha_creada = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
    proprietario = models.ForeignKey(Cliente, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return f'Cuenta de {self.proprietario}'