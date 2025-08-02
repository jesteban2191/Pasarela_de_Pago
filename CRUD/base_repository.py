from abc import ABC, abstractmethod

class CRUDRepositoryInterface(ABC):
    """
    CRUDRepositoryInterface:
    Clase encargada ser la interfaz para el manejo del CRUD de las listas de Sharepoint.
    
    Los métodos abstractos son:
        - url_request
        - url_posts
        - url_patch
        - url_delete"""

    @abstractmethod
    def url_get(self, url, token):
        """Método abstracto encargado de hacer el requerimiento al sitio de sharepoint."""
        pass

    @abstractmethod
    def url_posts(self, url, data):
        """Método abstracto encargado de hacer el post al sitio de sharepoint."""
        pass

    

