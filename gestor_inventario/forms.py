# gestor_inventario/forms.py
from django import forms
from .models import Producto
from django.core.exceptions import ValidationError
from django.core import validators




def validar_precio(value):
    if value <= 0:
        raise forms.ValidationError("El precio debe ser mayor que cero")

def validar_stock(value):
    if value < 0:
        raise forms.ValidationError("El stock no puede ser negativo")

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(100)
        ]
    )
    precio = forms.IntegerField(
        validators=[
            validar_precio
        ]
    )
    descripcion = forms.CharField(
        max_length=255,
        validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(255)
        ]
    )
    categoria = forms.CharField(
        widget=forms.Select(choices=[('Shampoo', 'SHAMPOO'), ('Acondicionador', 'ACONDICIONADOR'),('Crema capilar', 'CREMA CAPILAR'),('Tintura', 'TINTURA')])
    )
    stock = forms.IntegerField(
        validators=[
            validar_stock
        ]
    )
    imagen = forms.ImageField(required=True)



    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'categoria', 'stock', 'imagen']
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
        #     'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
        #     'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
        #     'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
        #     'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad en stock'}),
        #     'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        # }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock
