from .authinterface import AuthInterface
import os

class StripeAuth(AuthInterface):
    def get_token(self) -> str:
         # Example usage of environment variables
        stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY')
        stripe_secret_key = os.getenv('STRIPE_SECRET_KEY')

        if not stripe_secret_key:
            raise ValueError("Stripe secret key not found in environment variables.")
        else:
            return stripe_secret_key