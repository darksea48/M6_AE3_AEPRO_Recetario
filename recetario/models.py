from django.db import models

# Create your models here.

class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    optativos = models.TextField(blank=True, null=True)
    instrucciones = models.TextField()
    """imagen = models.ImageField(upload_to='recetas_img/', null=True, blank=True)"""
    imagen = models.CharField(max_length=300, null=True, blank=True)

    """def __str__(self):
        return self.nombre"""