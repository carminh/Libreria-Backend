"""
Servicio para consumir la API de Google Books
"""
import requests
import logging
from typing import Dict, List, Optional
from django.conf import settings

logger = logging.getLogger(__name__)

class GoogleBooksService:
    """
    Servicio para interactuar con la API de Google Books
    """
    
    BASE_URL = "https://www.googleapis.com/books/v1"
    
    def __init__(self, api_key: str = None):
        """
        Inicializa el servicio con una clave de API
        """
        self.api_key = api_key or getattr(settings, 'GOOGLE_BOOKS_API_KEY', None)
        if not self.api_key:
            logger.warning("No se ha configurado GOOGLE_BOOKS_API_KEY en settings")
    
    def search_books(self, query: str, max_results: int = 20, start_index: int = 0) -> Dict:
        """
        Busca libros en Google Books
        
        Args:
            query (str): Término de búsqueda
            max_results (int): Número máximo de resultados (máximo 40)
            start_index (int): Índice de inicio para paginación
            
        Returns:
            Dict: Respuesta de la API con los libros encontrados
        """
        if not query.strip():
            return {"items": [], "totalItems": 0}
        
        # Limitar max_results a 40 (límite de la API)
        max_results = min(max_results, 40)
        
        params = {
            'q': query,
            'maxResults': max_results,
            'startIndex': start_index,
            'printType': 'books',  # Solo libros, no revistas
            'orderBy': 'relevance'  # Ordenar por relevancia
        }
        
        if self.api_key:
            params['key'] = self.api_key
        
        try:
            response = requests.get(
                f"{self.BASE_URL}/volumes",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            return self._process_search_results(data)
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al consultar Google Books API: {e}")
            return {"items": [], "totalItems": 0, "error": str(e)}
        except Exception as e:
            logger.error(f"Error inesperado al procesar respuesta: {e}")
            return {"items": [], "totalItems": 0, "error": str(e)}
    
    def get_book_details(self, book_id: str) -> Optional[Dict]:
        """
        Obtiene detalles específicos de un libro
        
        Args:
            book_id (str): ID del libro en Google Books
            
        Returns:
            Dict: Detalles del libro o None si no se encuentra
        """
        params = {}
        if self.api_key:
            params['key'] = self.api_key
        
        try:
            response = requests.get(
                f"{self.BASE_URL}/volumes/{book_id}",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            return self._process_book_details(response.json())
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al obtener detalles del libro {book_id}: {e}")
            return None
        except Exception as e:
            logger.error(f"Error inesperado al procesar detalles del libro: {e}")
            return None
    
    def _process_search_results(self, data: Dict) -> Dict:
        """
        Procesa los resultados de búsqueda para extraer información relevante
        """
        processed_items = []
        
        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            
            # Extraer información básica
            book_data = {
                'id': item.get('id'),
                'title': volume_info.get('title', 'Sin título'),
                'authors': volume_info.get('authors', ['Autor desconocido']),
                'description': volume_info.get('description', 'Sin descripción disponible'),
                'published_date': volume_info.get('publishedDate', 'Fecha desconocida'),
                'publisher': volume_info.get('publisher', 'Editorial desconocida'),
                'page_count': volume_info.get('pageCount'),
                'language': volume_info.get('language', 'es'),
                'categories': volume_info.get('categories', []),
                'average_rating': volume_info.get('averageRating'),
                'ratings_count': volume_info.get('ratingsCount', 0),
                'preview_link': volume_info.get('previewLink'),
                'info_link': volume_info.get('infoLink'),
                'thumbnail': self._get_thumbnail_url(volume_info.get('imageLinks', {})),
                'isbn_10': self._get_isbn(volume_info.get('industryIdentifiers', []), 'ISBN_10'),
                'isbn_13': self._get_isbn(volume_info.get('industryIdentifiers', []), 'ISBN_13'),
                'price_info': self._get_price_info(item.get('saleInfo', {}))
            }
            
            processed_items.append(book_data)
        
        return {
            'items': processed_items,
            'totalItems': data.get('totalItems', 0),
            'query': data.get('query', '')
        }
    
    def _process_book_details(self, data: Dict) -> Dict:
        """
        Procesa los detalles de un libro específico
        """
        volume_info = data.get('volumeInfo', {})
        
        return {
            'id': data.get('id'),
            'title': volume_info.get('title', 'Sin título'),
            'authors': volume_info.get('authors', ['Autor desconocido']),
            'description': volume_info.get('description', 'Sin descripción disponible'),
            'published_date': volume_info.get('publishedDate', 'Fecha desconocida'),
            'publisher': volume_info.get('publisher', 'Editorial desconocida'),
            'page_count': volume_info.get('pageCount'),
            'language': volume_info.get('language', 'es'),
            'categories': volume_info.get('categories', []),
            'average_rating': volume_info.get('averageRating'),
            'ratings_count': volume_info.get('ratingsCount', 0),
            'preview_link': volume_info.get('previewLink'),
            'info_link': volume_info.get('infoLink'),
            'thumbnail': self._get_thumbnail_url(volume_info.get('imageLinks', {})),
            'isbn_10': self._get_isbn(volume_info.get('industryIdentifiers', []), 'ISBN_10'),
            'isbn_13': self._get_isbn(volume_info.get('industryIdentifiers', []), 'ISBN_13'),
            'price_info': self._get_price_info(data.get('saleInfo', {}))
        }
    
    def _get_thumbnail_url(self, image_links: Dict) -> str:
        """
        Obtiene la URL de la imagen más grande disponible
        """
        # Prioridad: large > medium > small > thumbnail
        for size in ['large', 'medium', 'small', 'thumbnail']:
            if size in image_links:
                return image_links[size]
        return ''
    
    def _get_isbn(self, identifiers: List[Dict], isbn_type: str) -> str:
        """
        Extrae el ISBN específico de la lista de identificadores
        """
        for identifier in identifiers:
            if identifier.get('type') == isbn_type:
                return identifier.get('identifier', '')
        return ''
    
    def _get_price_info(self, sale_info: Dict) -> Dict:
        """
        Extrae información de precios y disponibilidad
        """
        return {
            'is_ebook': sale_info.get('isEbook', False),
            'list_price': sale_info.get('listPrice', {}).get('amount'),
            'retail_price': sale_info.get('retailPrice', {}).get('amount'),
            'currency': sale_info.get('listPrice', {}).get('currencyCode', 'USD'),
            'buy_link': sale_info.get('buyLink'),
            'saleability': sale_info.get('saleability', 'NOT_FOR_SALE')
        }
