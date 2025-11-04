from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    

class Formato(models.Model):
    nombre = models.CharField(max_length=100)
    resolucion = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.resolucion}"
    
class Visual(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visuales')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    formato = models.ForeignKey(Formato, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


