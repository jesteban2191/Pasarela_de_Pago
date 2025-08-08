from .base_repository import CRUDRepositoryInterface
import requests
from typing import Any
from ..decorators import *

class RequestOperationHandler(CRUDRepositoryInterface):
    """
    Clase encargada de manejar las operaciones de request a un sitio web.
    """

    @check_type_args
    def url_get(self, url: str, token : str = "") -> Any:
        """Método encargado de hacer el get al sitio web."""
        params = {"url": url}
        if token:
            headers = {"Authorization": f"Bearer {token}"}
            params["headers"] = headers

        response = requests.get(**params)
        return response.json()

    @check_type_args
    def url_post(self, url: str, data: dict, token: str = "") -> Any:
        """Método encargado de hacer el post al sitio web."""
        response = requests.post(url, json=data)
        return response.json()