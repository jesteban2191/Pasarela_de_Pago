from .authinterface import AuthInterface
import os

class WompiAuth(AuthInterface):
    def get_token(self) -> str:
        wompi_key_secret = os.getenv('WOMPI_SECRET_KEY')
        
        if not wompi_key_secret:
            raise ValueError("Wompi secret key not found in environment variables.")
        else:
            return wompi_key_secret