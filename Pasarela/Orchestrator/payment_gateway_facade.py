from ..GatewayFactories import PaymentGatewayFactory

class PaymentGatewayFacade(OrchestratorInterface):

    @staticmethod
    def get_payment_gateway_factory(gateway: str):
        """
        Get the payment gateway factory for the specified gateway.
        
        :param gateway: Name of the payment gateway (e.g., 'stripe', 'wompi').
        :return: Payment gateway factory instance.
        """
        if gateway.lower() == "stripe":
            
            return PaymentGatewayFactory.create_gateway(gateway)
        else:
            raise ValueError(f"Unknown payment gateway: {gateway}")

    

    
    



    