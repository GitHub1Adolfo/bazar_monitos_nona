from django.db import models

# Create your models here.

class Producto(models.Model):

    CATEGORIAS = [
        ('Shampoo', 'SHAMPOO'),
        ('Acondicionador', 'ACONDICIONADOR'),
        ('Crema capilar', 'CREMA CAPILAR'),
        ('Tintura', 'TINTURA'),
    ]

    nombre=models.CharField(max_length=100, verbose_name="Nombre")
    precio=models.IntegerField(verbose_name="Precio")
    descripcion = models.TextField(verbose_name="Descripción")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    stock = models.PositiveIntegerField(verbose_name="Stock")
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
    