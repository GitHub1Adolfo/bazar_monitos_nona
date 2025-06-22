from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gestor_inventario.models import Producto
# Create your views here.
def index(request):
    categoria = request.GET.get('categoria')  # Obtén la categoría de la URL
    if categoria:
        productos = Producto.objects.filter(categoria=categoria)  # Filtra productos por categoría
    else:
        productos = Producto.objects.all()  # Muestra todos los productos si no se especifica categoría
    return render(request, 'index.html', {'productos': productos, 'categoria': categoria})

def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto_detalle.html', {'producto': producto})