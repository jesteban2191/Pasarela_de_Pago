from abc import ABC, abstractmethod
import pandas as pd

class OrchestratorInterface(ABC):

    @abstractmethod
    def get_paymentgateway_factory(self, gateway: str):
        """
        Get the payment gateway factory for the specified gateway.
        
        :param gateway: Name of the payment gateway (e.g., 'stripe', 'wompi').
        :return: Payment gateway factory instance.
        """
        pass
    