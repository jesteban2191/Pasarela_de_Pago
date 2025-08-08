from abc import ABC, abstractmethod
from typing import Dict, List, Any
import pandas as pd

class ClientHandlerInterface(ABC):
    @abstractmethod
    def get_customers(self, limit: int = 0, starting_after: str = "", ending_before: str = "") -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_customer_info(self, customer_id: str):
        pass

    @abstractmethod
    def create_customer(self, name: str, email: str, address: str = "", city: str = "", country: str = "", phone: str = "", state: str = "", postal_code: str = "", description: str = "", currency: str = "usd", default_payment_method: str = "", payments_methods: pd.DataFrame = pd.DataFrame()):
        pass

    def update_customer(self, customer_id: str, name: str = "", email: str = "", address: str = "", city: str = "", country: str = "", phone: str = "", state: str = "", postal_code: str = "", description: str = "", currency: str = "usd", default_payment_method: str = "", payments_methods: pd.DataFrame = pd.DataFrame()):
        """Update an existing customer with the provided details."""
        pass

    def delete_customer(self, customer_id: str):
        pass