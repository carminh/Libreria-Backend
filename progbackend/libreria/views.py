from django.shortcuts import render, redirect
from .models import Libro, Contacto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def home(request):
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

@login_required(login_url='libreria:login')
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

# 🔒 Vista protegida: solo usuarios logueados
@login_required
def perfil_usuario(request):
    return render(request, 'libreria/perfil.html')

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect('libreria:home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'libreria/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('libreria:home')
