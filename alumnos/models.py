from django.db import models

# Create your models here.


class Alumno(models.Model):
    nombre = models.CharField(max_length=300, verbose_name='Nombre')
    nota = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Promedio')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['nombre']
