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
]
