from django.shortcuts import render
from django.http import HttpResponse
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
        },
        {
            'titulo': 'Fahrenheit 451',
            'autor': 'Ray Bradbury',
            'descripcion': 'Novela distópica de una sociedad estounidense futurista en la que los libros están prohibidos.',
            'portada': 'images/4.jpg',
            'id': 4
        },
        {
            'titulo': 'El Cuervo',
            'autor': 'Edgar Allan Poe',
            'descripcion': 'Poema narrativo publicado por primera vez en 1845.',
            'portada': 'images/5.jpg',
            'id': 5
        },
        {
            'titulo': 'Harry Potter y la Piedra Filosofal',
            'autor': 'J.K. Rowling',
            'descripcion': 'Harry Potter, huérfano y maltratado por sus tíos, descubre un día que ha sido aceptado en Hogwarts, un colegio de magia que cambiará su vida.',
            'portada': 'images/6.jpg',
            'id': 6
        },
        {
            'titulo': 'El Silencio de los Corderos',
            'autor': 'Thomas Harris',
            'descripcion': 'Novela de misterio y terror escrita en 1988. Una agente en entrenamiento del FBI busca la ayuda y consejo de un brillante asesino para poder capturar a otro asesino, el doctor Hannibal Lecter.',
            'portada': 'images/7.jpg',
            'id': 7
        },
        {
            'titulo': 'El Evangelio del Mal',
            'autor': 'Patrick Graham',
            'descripcion': 'Lucha entre una Agente Especial del FBI y una organización satanista que se plantea asumir el control del Vaticano de manera inminente.',
            'portada': 'images/8.jpg',
            'id': 8
        },
        {
            'titulo': 'Siddhartha',
            'autor': 'Hermann Hesse',
            'descripcion': 'Relata la vida de un indio llamado Siddhartha.',
            'portada': 'images/9.jpg',
            'id': 9
        }

    ]
    
    context = {
        'libros': libros
    }
    return render(request, 'libreria/catalogo.html', context)

#AÑADE CONTACTO
def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        edad = request.POST.get("edad")
        correo = request.POST.get("correo")
        mensaje = request.POST.get("mensaje")

        # Por ahora, solo mostramos los datos en pantalla
        return HttpResponse(f"""
            <h2>Gracias por tu mensaje, {nombre}!</h2>
            <p><strong>Edad:</strong> {edad}</p>
            <p><strong>Correo:</strong> {correo}</p>
            <p><strong>Mensaje:</strong> {mensaje}</p>
            <a href='/contacto/'>Volver</a>
        """)
    
    return render(request, 'libreria/contacto.html')
