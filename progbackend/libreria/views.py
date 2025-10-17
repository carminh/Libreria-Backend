from django.shortcuts import render, redirect
from .models import Libro, Contacto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .services import GoogleBooksService
import json

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

# ===== NUEVAS VISTAS PARA API DE GOOGLE BOOKS =====

def api_libros(request):
    """
    Vista principal para buscar libros usando Google Books API
    """
    query = request.GET.get('q', '').strip()
    page = int(request.GET.get('page', 1))
    max_results = int(request.GET.get('max_results', 20))
    
    # Calcular índice de inicio para paginación
    start_index = (page - 1) * max_results
    
    books_service = GoogleBooksService()
    
    if query:
        results = books_service.search_books(
            query=query,
            max_results=max_results,
            start_index=start_index
        )
    else:
        results = {"items": [], "totalItems": 0}
    
    # Calcular información de paginación
    total_items = results.get('totalItems', 0)
    total_pages = (total_items + max_results - 1) // max_results if total_items > 0 else 0
    
    context = {
        'query': query,
        'books': results.get('items', []),
        'total_items': total_items,
        'current_page': page,
        'total_pages': total_pages,
        'has_previous': page > 1,
        'has_next': page < total_pages,
        'previous_page': page - 1 if page > 1 else None,
        'next_page': page + 1 if page < total_pages else None,
        'error': results.get('error')
    }
    
    return render(request, 'libreria/api_libros.html', context)

@require_http_methods(["GET"])
def api_libros_search(request):
    """
    API endpoint para búsqueda de libros (AJAX)
    """
    query = request.GET.get('q', '').strip()
    max_results = int(request.GET.get('max_results', 10))
    
    if not query:
        return JsonResponse({
            'success': False,
            'message': 'El término de búsqueda es requerido'
        })
    
    books_service = GoogleBooksService()
    results = books_service.search_books(
        query=query,
        max_results=max_results
    )
    
    return JsonResponse({
        'success': True,
        'data': results
    })

def api_libro_detalle(request, book_id):
    """
    Vista para mostrar detalles específicos de un libro
    """
    books_service = GoogleBooksService()
    book_details = books_service.get_book_details(book_id)
    
    if not book_details:
        messages.error(request, 'No se pudo encontrar el libro solicitado.')
        return redirect('libreria:api_libros')
    
    context = {
        'book': book_details
    }
    
    return render(request, 'libreria/api_libro_detalle.html', context)
