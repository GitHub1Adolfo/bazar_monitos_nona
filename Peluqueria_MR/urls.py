"""
URL configuration for Peluqueria_MR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from producto import views as producto
from login import views as login
from gestor_inventario import views as gestor_inventario
from carritoapp import views as carrito

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #INDEX
    path('',producto.index, name='index'),

    # LOGIN
    path('login/',login.user_login, name='login'),
    path('logout/', login.user_logout, name='user_logout'),

    #GESTOR_INVENTARIO
    path('gestor_inventario/', gestor_inventario.tabla_productos, name='tabla_productos'),
    path('eliminarProducto/<int:id>', gestor_inventario.eliminarProducto, name='eliminarProducto'),
    path('agregar_producto/', gestor_inventario.agregar_producto, name='agregar_producto'),
    path('actualizarProducto/<int:id>',gestor_inventario.actualizarProducto),
    #PRODUCTO DETALLE
    path('producto/<int:producto_id>/', producto.producto_detalle, name='producto_detalle'),

    #CARRITO
    path('tienda', carrito.tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', carrito.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', carrito.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', carrito.restar_producto, name="Sub"),
    path('limpiar/', carrito.limpiar_carrito, name="CLS"),
    path('boleta/', carrito.generar_boleta, name='Boleta'),
    path('limpiar-y-volver/', carrito.limpiar_carrito_y_volver, name='limpiar_y_volver'),
    path('valida_carrito/', carrito.validar_carrito, name='validar_carrito'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)