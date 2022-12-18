from django.db import models

# Create your models here.

class Institucion(models.Model):
    nombre = models.CharField(blank=True, max_length=100)
    direccion =  models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        return self.nombre


