from django.shortcuts import render
from .models import Libro, Contacto

def home(request):
    return render(request, 'libreria/home.html')

def catalogo(request):
    libros = Libro.objects.all()
    return render(request, 'libreria/catalogo.html', {'libros': libros})

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