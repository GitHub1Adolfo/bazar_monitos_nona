from django.shortcuts import render, HttpResponse, redirect
from carritoapp.carrito import Carrito
from gestor_inventario.models import Producto
from datetime import datetime
from django.http import JsonResponse
# Create your views here.



def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def validar_carrito(request):
    if "carrito" not in request.session or not request.session["carrito"]:
        return JsonResponse({"error": "El carrito está vacío."}, status=400)

    carrito = request.session["carrito"]
    errores = []

    # Verificar si el stock de cada producto en el carrito es suficiente
    for key, item in carrito.items():
        producto = Producto.objects.get(id=item["producto_id"])
        if item["cantidad"] > producto.stock:
            errores.append(f"No hay suficiente stock para {producto.nombre}. Solo hay {producto.stock} disponible(s).")
        else:
            # Si hay stock suficiente, se resta el stock del producto
            producto.stock -= item["cantidad"]
            producto.save()  # Guardamos el cambio de stock en la base de datos

    if errores:
        return JsonResponse({"errores": errores}, status=400)

    return JsonResponse({"exito": "Compra validada."})


def generar_boleta(request):
    if "carrito" not in request.session or not request.session["carrito"]:
        return redirect("Tienda")
    
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    carrito = request.session["carrito"]
    total = sum(item["acumulado"] for item in carrito.values())
    
    context = {
        "fecha": fecha,
        "carrito": carrito,
        "total_carrito": total
    }
    
    del request.session['carrito']
    request.session.modified = True
    
    return render(request, "boleta.html", context)

def limpiar_carrito_y_volver(request):
    # Limpia el carrito eliminando la información de la sesión
    if 'carrito' in request.session:
        del request.session['carrito']
        request.session.modified = True
    # Redirige a la tienda
    return redirect("index")  # Asegúrate de que 'Tienda' es el nombre correcto de la URL de la tienda