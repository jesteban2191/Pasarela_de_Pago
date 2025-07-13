from abc import ABC, abstractmethod
import os

class AuthInterface(ABC):
    @abstractmethod
    def get_token(sefl) -> str:
        """Return the secret key for the payment gateway."""
        pass
              
       