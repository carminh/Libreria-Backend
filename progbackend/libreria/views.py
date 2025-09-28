from django.shortcuts import render
from .models import Libro, Contacto

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