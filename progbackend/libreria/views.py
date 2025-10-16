from django.shortcuts import render, redirect
from .models import Libro, Contacto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def home(request):
    # Obtener estadísticas para mostrar en la página de inicio
    total_libros = Libro.objects.count()
    libros_destacados = Libro.objects.filter(disponible=True)[:3]
    total_usuarios = Contacto.objects.count()
    
    context = {
        'total_libros': total_libros,
        'libros_destacados': libros_destacados,
        'total_usuarios': total_usuarios
    }
    return render(request, 'libreria/home.html', context)

def catalogo(request):
    libros = Libro.objects.all()
    total_libros = libros.count()
    libros_disponibles = libros.filter(disponible=True).count()
    total_contactos = Contacto.objects.count()
    
    context = {
        'libros': libros,
        'total_libros': total_libros,
        'libros_disponibles': libros_disponibles,
        'total_contactos': total_contactos
    }
    return render(request, 'libreria/catalogo.html', context)

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("correo")
        edad = request.POST.get("edad")
        mensaje = request.POST.get("mensaje")
        
        Contacto.objects.create(nombre=nombre, email=email, edad=edad, mensaje=mensaje)
        return render(request, 'libreria/gracias.html')
    
    return render(request, 'libreria/contacto.html')

def clientes(request):
    contactos = Contacto.objects.all().order_by('-fecha')  
    return render(request, 'libreria/clientes.html', {'contactos': contactos})

def gracias(request):
    return render(request, 'libreria/gracias.html')

@login_required
def perfil_usuario(request):
    return render(request, 'perfil.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('home')