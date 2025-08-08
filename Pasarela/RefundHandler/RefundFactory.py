from .StripeRefund import StripeRefund

class RefundFactory:
    @staticmethod
    def get_refund_handler(gateway: str):
        if gateway == "stripe":
            return StripeRefund()
        # Add other gateways here as needed
        else:
            raise ValueError(f"Unsupported payment gateway: {gateway}")