from typing import Any
class AuthContext:

    """Contexto para la autenticación usando una estrategia.
    
    Esta clase permite utilizar diferentes estrategias de autenticación (por ejemplo, autenticación con Microsoft Graph) mediante el patrón Strategy. 
    
    Args:
        strategy: Objeto que implementa el método de autenticación deseado. Esta estrategia debe estar basada en la interfaz auth_interface.AuthenticationStrategy.
    
    Ejemplo:
        auth = AuthContext(MSGraphAuth(...))
        token = auth.get_token()
        main_url = auth.get_url()
     """
    
    def __init__(self, strategy: Any) -> None:
        self._strategy = strategy

    def get_token(self) -> str:
        """Obtiene el token de autenticación utilizando la estrategia definida."""
        return self._strategy.get_token()
