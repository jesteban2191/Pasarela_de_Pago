from .ClientStripe import StripeClient


class ClientFactory:
    @staticmethod
    def get_client(gateway: str):
        if gateway == "stripe":
            return StripeClient()
        elif gateway == "wompi":
            pass
        raise ValueError(f"Unknown payment gateway: {gateway}")