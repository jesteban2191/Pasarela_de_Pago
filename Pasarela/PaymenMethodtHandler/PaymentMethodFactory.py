from .StripePaymentMethod import StripePaymentMethod

class PaymentMethodFactory:
    @staticmethod
    def get_payment_method(payment_method_type: str):
        if payment_method_type == "stripe":
            return StripePaymentMethod()
        else:
            raise ValueError(f"Unsupported payment method type: {payment_method_type}")