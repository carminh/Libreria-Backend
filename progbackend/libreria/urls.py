from django.urls import path
from . import views

app_name = 'libreria'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('contacto/', views.contacto, name='contacto'),
    path('clientes/', views.clientes, name='clientes'),
    path('gracias/', views.gracias, name='gracias'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),  # coincide con views.py
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # URLs para API de Google Books
    path('api-libros/', views.api_libros, name='api_libros'),
    path('api-libros/search/', views.api_libros_search, name='api_libros_search'),
    path('api-libros/libro/<str:book_id>/', views.api_libro_detalle, name='api_libro_detalle'),
]
