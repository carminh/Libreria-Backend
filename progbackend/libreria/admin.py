from django.contrib import admin
from .models import Libro, Contacto

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'precio', 'disponible')
    list_filter = ('disponible', 'autor')
    search_fields = ('titulo', 'autor')

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'edad', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('nombre', 'email')
    readonly_fields = ('fecha',)
