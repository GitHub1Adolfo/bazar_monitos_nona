from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def tabla_productos(request):
    productos = Producto.objects.all()
    data = {'productos' : productos}
    return render(request, 'tabla_productos.html', data)

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tabla_productos')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

@login_required
def actualizarProducto(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoForm(instance=producto) 
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)  
        if form.is_valid():
            form.save()
            return tabla_productos(request)
        data = {'form' : form} 
    data = {'form': form}
    
    return render(request, 'producto_form.html', data)

@login_required
def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('/gestor_inventario')
