from django.db import models
from Institucion.models import Institucion
from .choices import estados

# Create your models here.


class Inscritos(models.Model):
    nombre =  models.CharField(blank=True, max_length=100)
    telefono =  models.CharField(blank=True, max_length=100)
    fechaInscripcion = models.DateField(blank=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, blank=True)
    horaInscripcion = models.TimeField()
    estado =  models.CharField(blank=True, choices=estados, default=1, max_length=100)
    observacion =  models.TextField(null=True)