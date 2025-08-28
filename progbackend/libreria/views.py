from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'libreria/home.html')

def catalogo(request):

    libros = [
        {
            'titulo': 'El Señor de los Anillos',
            'autor': 'J.R.R. Tolkien',
            'descripcion': 'Una épica aventura en la Tierra Media donde un hobbit debe destruir un anillo poderoso.',
            'portada': 'images/1.jpg',
            'id': 1
        },
        {
            'titulo': 'Cien años de soledad',
            'autor': 'Gabriel García Márquez',
            'descripcion': 'La historia de la familia Buendía a lo largo de siete generaciones en Macondo.',
            'portada': 'images/2.png',
            'id': 2
        },
        {
            'titulo': '1984',
            'autor': 'George Orwell',
            'descripcion': 'Una distopía que retrata una sociedad totalitaria bajo constante vigilancia.',
            'portada': 'images/3.jpeg',
            'id': 3
        }
    ]
    
    context = {
        'libros': libros
    }
    return render(request, 'libreria/catalogo.html', context)

#AÑADE CONTACTO
def contacto(request):
    return render(request, 'libreria/contacto.html')
