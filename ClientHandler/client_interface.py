from abc import ABC, abstractmethod
from typing import Dict, List

class ClientHandlerInterface(ABC):
    @abstractmethod
    def get_customers(self):
        pass

    @abstractmethod
    def get_customer_info(self, customer_id: str):
        pass

    @abstractmethod
    def create_customer(self, name: str, email: str, address: str = None, city: str = None, country: str = None, phone: str = None, state: str = None, postal_code: str = None, description: str = None, currency: str = "usd", default_payment_method: str = None, payment_methods: list[Dict[str,str]] = []):
        pass

    def update_customer(self, customer_id: str, name: str = None, email: str = None, address: str = None, city: str = None, country: str = None, phone: str = None, state: str = None, postal_code: str = None, description: str = None, currency: str = "usd", default_payment_method: str = None):
        """Update an existing customer with the provided details."""
        pass