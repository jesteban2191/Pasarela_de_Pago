from abc import ABC, abstractmethod
from typing import Any, Dict, List
import pandas as pd

class GatewayInterface(ABC):

    ################################################################################################
    ###                         Abstract methods for client management
    ################################################################################################

    @abstractmethod
    def get_clients(self):
        pass

    @abstractmethod
    def get_client(self, client_id):
        pass

    @abstractmethod
    def create_client(self, name: str, email: str, address: str = "", city: str = "", country: str = "", phone: str = "", state: str = "", postal_code: str = "", description: str = "", currency: str = "usd", default_payment_method: str = "", payments_methods: pd.DataFrame = pd.DataFrame()):
        pass

    @abstractmethod
    def update_client(self, customer_id: str, name: str = "", email: str = "", address: str = "", city: str = "", country: str = "", phone: str = "", state: str = "", postal_code: str = "", description: str = "", currency: str = "usd", default_payment_method: str = "", payments_methods: pd.DataFrame = pd.DataFrame()):
        pass

    @abstractmethod
    def delete_client(self, client_id: str):
        pass
    
    ################################################################################################
    ###                         Abstract methods for payment method management
    ################################################################################################

    @abstractmethod
    def create_payment_method(self, type_paymentmethod: str, customer_id: str = "", account_number: str = "", account_type: str = "", account_holder_type: str = "", account_holder_name: str = "", routing_number: str = "", bank_name: str = "",card_number: str = "", card_exp_month: str = "", card_exp_year: str = "", card_cvc: str = "", token_card: str = ""):
        pass

    @abstractmethod
    def update_payment_method(self, paymentmethod_id: str, type_paymentmethod: str, account_number: str = "", account_type: str = "", account_holder_type: str = "", account_holder_name: str = "", routing_number: str = "", bank_name: str = "",card_number: str = "", card_exp_month: str = "", card_exp_year: str = "", card_cvc: str = "", token_card: str = ""):
        pass

    @abstractmethod
    def get_client_paymentmethods(self, customer_id: str, limit: int = 0, starting_after: str = "", ending_before: str = ""):
        pass

    @abstractmethod
    def get_payment_method(self, paymentmethod_id: str):
        pass

    @abstractmethod
    def get_payment_methods(self, ending_before: str = "", starting_after: str = "", limit: int = 0, type: str = ""):
        pass

    @abstractmethod
    def atach_paymentmethod_to_client(self, paymentmethod_id: str, customer_id: str):
        pass

    @abstractmethod
    def detach_paymentmethod_from_client(self, paymentmethod_id: str, customer_id: str):
        pass

    ################################################################################################
    ###                         Abstract methods for paymentintent management
    ################################################################################################

    @abstractmethod
    def create_payment(self, amount: float, currency: str, payment_method_id: str, customer_id: str = "", description: str = ""):
        pass

    @abstractmethod
    def get_payment(self, payment_intent_id: str):
        pass

    @abstractmethod
    def get_list_payments(self, customer_id: str = "", date: int = 0, limit: int = 0, starting_after: str = "", ending_before: str = ""):
        pass

    ################################################################################################
    ###                         Abstract methods for refund management
    ################################################################################################

    @abstractmethod
    def create_refund(self,  payment_intent_id: str, amount: float , reason: str):
        pass

    @abstractmethod
    def get_refund(self, refund_id: str):
        pass

    @abstractmethod
    def get_list_refunds(self, payment_intent_id: str = "", limit: int = 0, date: str = "", ending_before: str = "", starting_after: str = ""):
        pass
