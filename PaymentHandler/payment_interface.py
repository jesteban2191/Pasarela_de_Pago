from abc import ABC, abstractmethod

class PaymentInterface(ABC):
    @abstractmethod
    def create_payment(self, amount: float, currency: str, payment_method_id: str, customer_id: str = "", description: str = ""):
        """
        Create a payment using the specified payment method.
        
        :param amount: Amount to be charged.
        :param currency: Currency of the payment.
        :param payment_method_id: ID of the payment method to be used.
        :param customer_id: ID of the customer making the payment.
        :param description: Optional description for the payment.
        :return: Payment object or identifier.
        """
        pass
    
    @abstractmethod
    def retrieve_payment(self, payment_intent_id: str):
        """
        Retrieve a payment using its identifier.
        
        :param payment_intent_id: ID of the payment intent to retrieve.
        :return: Payment object or details.
        """
        pass

    @abstractmethod
    def list_all_paymentintents(self, customer_id: str = "", date: int = 0, limit: int = 0, starting_after: str = "", ending_before: str = ""):
        """
        List all payment intents for a customer.
        
        :param customer_id: ID of the customer whose payment intents are to be listed.
        :return: List of payment intents.
        """
        pass

        