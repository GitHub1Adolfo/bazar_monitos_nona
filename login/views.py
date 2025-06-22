from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages

# LOGIN ADMINISTRADOR
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')
        try:
            # Autenticamos al usuario
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige al index si login es exitoso
            else:
                # Si el usuario no es autenticado
                messages.error(request, "Usuario o contraseña incorrectos.")
        
        except Exception as e:
            # Capturamos cualquier otra excepción no esperada
            messages.error(request, f"Hubo un error en el proceso de login: {str(e)}")

        # Si hay errores, volvemos a mostrar el formulario de login con mensajes
        return render(request, 'login.html')

    # Renderizamos el formulario de login si el método es GET
    return render(request, 'login.html')

# LOGOUT
@login_required
def user_logout(request):
    logout(request)
    # Opcional: puedes agregar un mensaje aquí si lo deseas
    # messages.success(request, "Sesión cerrada con éxito.")
    return redirect('login')

# INDEX
@login_required
@never_cache
def index(request):
    return render(request, 'index.html')
