from django.db import models

# Create your models here.
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.PositiveIntegerField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.email})"
