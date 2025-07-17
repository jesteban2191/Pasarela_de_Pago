from .paymentmethod_interface import PaymentMethodInterface
import stripe
from ..auth import *
from typing import Dict, Any
import pandas as pd

class StripePaymentMethod(PaymentMethodInterface):
    def create_paymentmethod(self, type_paymentmethod: str, customer_id: str = "", account_number: str = "", account_type: str = "", account_holder_type: str = "", account_holder_name: str = "", routing_number: str = "", bank_name: str = "",card_number: str = "", card_exp_month: str = "", card_exp_year: str = "", card_cvc: str = "", token_card: str = "") -> Dict[str, Any]:
        # Implementation for creating a payment method using Stripe API
        if type_paymentmethod == "us_bank_account":
            data_type_paymentmethod = {
                "account_number": account_number,
                "account_type": account_type,
                "account_holder_type": account_holder_type,
                "account_holder_name": account_holder_name,
                "routing_number": routing_number,
                "bank_name": bank_name 
            }

            payment_method = stripe.PaymentMethod.create(
                type="us_bank_account",
                us_bank_account=data_type_paymentmethod,
                customer=customer_id,
                billing_details={
                    "name": account_holder_name
                }
            )
        
        elif type_paymentmethod == "credit":
            if token_card:
                data_type_paymentmethod = {
                    "token": token_card
                }
            else:
                data_type_paymentmethod = {
                    "number": card_number,
                    "exp_month": card_exp_month,
                    "exp_year": card_exp_year,
                    "cvc": card_cvc
                }

            payment_method = stripe.PaymentMethod.create(
                type = "card",
                card=data_type_paymentmethod,
                customer=customer_id
            )

               
        pass

    def update_paymentmethod(self, type_paymentmethod: str, customer_id: str = "", account_number: str = "", account_type: str = "", account_holder_type: str = "", account_holder_name: str = "", routing_number: str = "", bank_name: str = "",card_number: str = "", card_exp_month: str = "", card_exp_year: str = "", card_cvc: str = "", token_card: str = "")-> Dict[str, Any]:
        # Implementation for updating a payment method using Stripe API
        if type_paymentmethod == "us_bank_account":
            data_type_paymentmethod = {
                "account_number": account_number,
                "account_type": account_type,
                "account_holder_type": account_holder_type,
                "account_holder_name": account_holder_name,
                "routing_number": routing_number,
                "bank_name": bank_name 
            }
        elif type_paymentmethod == "credit":
            if token_card:
                data_type_paymentmethod = {
                    "token": token_card
                }
            else:
                data_type_paymentmethod = {
                    "number": card_number,
                    "exp_month": card_exp_month,
                    "exp_year": card_exp_year,
                    "cvc": card_cvc
                }        
        pass

    def get_customer_paymentmethods(self, customer_id: str):
        # Implementation for retrieving customer payment methods using Stripe API
        pass

    def get_paymentmethod(self, paymentmethod_id: str):
        # Implementation for retrieving a specific payment method using Stripe API
        pass

    def get_paymentmethods(self, ending_before: str, starting_after: str, limit: int, customer_id: str, type: str):
        # Implementation for listing payment methods using Stripe API
        pass

    def atach_paymentmethod_to_customer(self, paymentmethod_id: str, customer_id: str):
        # Implementation for attaching a payment method to a customer using Stripe API
        pass

    def detach_paymentmethod_from_customer(self, paymentmethod_id: str):
        # Implementation for detaching a payment method from a customer using Stripe API
        pass
