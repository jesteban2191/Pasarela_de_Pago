from .StripeGateway import StripeGateway
from typing import Dict, Any

class PaymentGatewayFactory:
    """
    Factory class to create payment gateways.
    """

    @staticmethod
    def create_gateway(gateway_type: str):
        """
        Create a payment gateway instance based on the specified type.
        
        :param gateway_type: Type of the payment gateway (e.g., 'stripe').
        :return: An instance of the specified payment gateway.
        """
        if gateway_type.lower() == 'stripe':
            return StripeGateway()
        else:
            raise ValueError(f"Unsupported gateway type: {gateway_type}")