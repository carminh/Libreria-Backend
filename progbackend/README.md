# Librería Backend - Django

Una aplicación web Django para gestión de librería con integración de Google Books API.

## 🚀 Características

- **Gestión de Libros**: CRUD completo para libros con portadas
- **Sistema de Contacto**: Formulario de contacto con validación
- **Autenticación**: Sistema de login/logout
- **Google Books API**: Búsqueda de libros en tiempo real
- **Diseño Responsive**: Interfaz moderna y adaptable

## 📋 Requisitos

- Python 3.8+
- Django 5.2+
- SQLite (incluido con Python)

## 🛠️ Instalación

### 1. Clonar el repositorio
```bash
git clone <repository-url>
cd Libreria-Backend/progbackend
```

### 2. Crear entorno virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
# Instalación básica
pip install -r requirements.txt

# Para desarrollo (incluye herramientas adicionales)
pip install -r requirements-dev.txt
```

```

### 5. Ejecutar migraciones
```bash
python manage.py migrate
```

### 6. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor de desarrollo
```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## 🎯 Funcionalidades

### Páginas Disponibles

- **Inicio** (`/`): Dashboard con estadísticas
- **Catálogo** (`/catalogo/`): Lista de libros locales
- **Buscar Libros** (`/api-libros/`): Búsqueda con Google Books API
- **Contacto** (`/contacto/`): Formulario de contacto (requiere login)
- **Clientes** (`/clientes/`): Lista de contactos
- **Login/Logout**: Sistema de autenticación

### API de Google Books

- **Búsqueda**: Por título, autor, ISBN, etc.
- **Paginación**: 20 resultados por página
- **Detalles**: Información completa de cada libro
- **Enlaces**: Vista previa y compra en Google Books

## 🗂️ Estructura del Proyecto

```
progbackend/
├── libreria/                 # App principal
│   ├── models.py            # Modelos de datos
│   ├── views.py             # Vistas
│   ├── urls.py              # URLs
│   ├── services.py          # Servicio Google Books API
│   └── admin.py             # Admin interface
├── templates/               # Templates HTML
│   └── libreria/
├── static/                  # Archivos estáticos
├── media/                   # Archivos de medios
├── requirements.txt         # Dependencias básicas
├── requirements-dev.txt     # Dependencias de desarrollo
└── env.example             # Variables de entorno ejemplo
```

## 🔧 Desarrollo

### Comandos útiles

```bash
# Ejecutar migraciones
python manage.py migrate

# Crear migraciones
python manage.py makemigrations

# Ejecutar tests
python manage.py test

# Recopilar archivos estáticos
python manage.py collectstatic

# Shell de Django
python manage.py shell
```

### Herramientas de desarrollo incluidas

- **django-debug-toolbar**: Debug en desarrollo
- **django-extensions**: Comandos adicionales
- **flake8**: Linting de código
- **black**: Formateo de código
- **pytest**: Testing framework

### Archivos estáticos

```bash
python manage.py collectstatic
```

## 📝 Dependencias

### Básicas (`requirements.txt`)
- **Django 5.2.7**: Framework web
- **requests 2.32.5**: HTTP requests para Google Books API
- **Pillow 12.0.0**: Procesamiento de imágenes

## 🐛 Troubleshooting

### Problemas con archivos estáticos
```bash
python manage.py collectstatic --noinput
```

## 👥 Contribuidores

- 💻 Britanny Labraña
- 💻 Carmen Herrera

