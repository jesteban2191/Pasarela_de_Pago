from ..decorators.decorators import check_type_args
import stripe
from ..auth import *
from .client_interface import ClientInterface
from typing import Dict, Any

class StripeClient(ClientInterface):
    def __init__(self, auth: AuthContext) -> None:
        self.auth = auth
        self._token = self.auth.get_token()

    @check_type_args
    def get_customers(self) -> Dict[str, Any]:
        """Retrieve the current customer."""
        stripe.api_key = self._token
        return stripe.Customer.list()
    
    @check_type_args
    def get_customer_info(self, customer_id: str) -> Dict[str, Any]:
        """Retrieve information about a specific customer."""
        stripe.api_key = self._token
        return stripe.Customer.retrieve(customer_id)