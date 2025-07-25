from .StripePaymentIntent import StripePaymentIntent

class PaymentIntentFactory:

    @staticmethod
    def get_payment_intent(gateway: str):
        if gateway == "stripe":
            return StripePaymentIntent()
        # Add other gateways here as needed
        else:
            raise ValueError(f"Unsupported payment gateway: {gateway}")