from abc import ABC, abstractmethod

class PaymentMethodInterface(ABC):
    @abstractmethod
    def create_paymentmethod(self, type_paymentmethod: str, customer_id: str = "", account_number: str = "", account_type: str = "", account_holder_type: str = "", account_holder_name: str = "", routing_number: str = "", bank_name: str = "",card_number: str = "", card_exp_month: str = "", card_exp_year: str = "", card_cvc: str = "", token_card: str = ""):
        """
        Create a payment method for the customer.
        
        :param type_paymentmethod: Type of payment method (e.g., 'card', 'bank_account').
        :param customer_id: ID of the customer to whom the payment method will be associated.
        :param kwargs: Additional parameters specific to the payment method type.
        :return: Payment method object or identifier.
        """
        pass

    @abstractmethod
    def update_paymentmethod(self, paymentmethod_id: str, type_paymentmethod: str, account_number: str = "", account_type: str = "", account_holder_type: str = "", account_holder_name: str = "", routing_number: str = "", bank_name: str = "",card_number: str = "", card_exp_month: str = "", card_exp_year: str = "", card_cvc: str = "", token_card: str = ""):
        """
        Update an existing payment method for the customer.
        
        :param paymentmethod_id: ID of the payment method to update.
        :param type_paymentmethod: Type of payment method (e.g., 'card', 'bank_account').
        :param customer_id: ID of the customer to whom the payment method is associated.
        :param kwargs: Additional parameters specific to the payment method type.
        :return: Updated payment method object or identifier.
        """
        pass

    @abstractmethod
    def get_customer_paymentmethods(self, customer_id: str, limit: int = 0, starting_after: str = "", ending_before: str = ""):
        """
        List all payment methods associated with a customer.
        
        :param customer_id: ID of the customer whose payment methods are to be listed.
        :return: List of payment method objects or identifiers.
        """
        pass

    @abstractmethod
    def get_paymentmethod(self, paymentmethod_id: str):
        """
        Retrieve a specific payment method by its ID.
        
        :param paymentmethod_id: ID of the payment method to retrieve.
        :return: Payment method object or identifier.
        """
        pass
    
    @abstractmethod
    def get_paymentmethods(self, ending_before: str = "", starting_after: str = "", limit: int = 0, type: str = ""):

        pass

    @abstractmethod
    def atach_paymentmethod_to_customer(self, paymentmethod_id: str, customer_id: str):
        """
        Attach a payment method to a customer.
        
        :param paymentmethod_id: ID of the payment method to attach.
        :param customer_id: ID of the customer to whom the payment method will be attached.
        :return: Confirmation of attachment or updated customer object.
        """
        pass

    @abstractmethod
    def detach_paymentmethod_from_customer(self, paymentmethod_id: str):
        """
        Detach a payment method from a customer.
        
        :param paymentmethod_id: ID of the payment method to detach.
        :return: Confirmation of detachment or updated customer object.
        """
        pass

    