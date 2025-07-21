from .paymentmethod_interface import PaymentMethodInterface
import stripe
from ..auth import *
from typing import Dict, Any, List
import pandas as pd
from ..decorators import check_type_args

class StripePaymentMethod(PaymentMethodInterface):

    @check_type_args
    def create_paymentmethod(self, type_paymentmethod: str, customer_id: str = "", account_number: str = "", account_type: str = "", account_holder_type: str = "", account_holder_name: str = "", routing_number: str = "", bank_name: str = "",card_number: str = "", card_exp_month: str = "", card_exp_year: str = "", card_cvc: str = "", token_card: str = "") -> Dict[str, Any]:
        # Implementation for creating a payment method using Stripe API
        if type_paymentmethod not in ["us_bank_account", "card"]:
            raise ValueError("Invalid payment method type.")
        
        params = {"type": type_paymentmethod}
        data_paymentmethod = {}

        if type_paymentmethod == "us_bank_account":
            if account_number:
                data_paymentmethod["account_number"] = account_number
            if account_type:
                data_paymentmethod["account_type"] = account_type
            if account_holder_type:
                data_paymentmethod["account_holder_type"] = account_holder_type
            if account_holder_name:
                data_paymentmethod["account_holder_name"] = account_holder_name
                params["billing_details"] = {"name": account_holder_name}
            if routing_number:
                data_paymentmethod["routing_number"] = routing_number
            if bank_name:
                data_paymentmethod["bank_name"] = bank_name
            
            if data_paymentmethod:
                params["us_bank_account"] = data_paymentmethod
            else:
                raise ValueError("At least one bank account detail must be provided.")
        
        elif type_paymentmethod == "credit":
            data_paymentmethod = {}
            if token_card:
                data_paymentmethod["token"] = token_card
            else:
                if card_number:
                    data_paymentmethod["number"] = card_number
                if card_exp_month:
                    data_paymentmethod["exp_month"] = card_exp_month
                if card_exp_year:
                    data_paymentmethod["exp_year"] = card_exp_year
                if card_cvc:
                    data_paymentmethod["cvc"] = card_cvc

                if data_paymentmethod:
                    params["card"] = data_paymentmethod
                else:
                    raise ValueError("At least one card detail must be provided.")
    
        payment_method = stripe.PaymentMethod.create(**params)

        return payment_method

    @check_type_args
    def update_paymentmethod(self, paymentmethod_id: str, type_paymentmethod: str, account_number: str = "", account_type: str = "", account_holder_type: str = "", account_holder_name: str = "", routing_number: str = "", bank_name: str = "",card_number: str = "", card_exp_month: str = "", card_exp_year: str = "", card_cvc: str = "", token_card: str = "")-> Dict[str, Any]:
        # Implementation for updating a payment method using Stripe API
        if paymentmethod_id == "":
            raise ValueError("Payment method ID cannot be empty.")
        if type_paymentmethod not in ["us_bank_account", "card"]:
            raise ValueError("Invalid payment method type.")
        
        params = {"id": paymentmethod_id}
        
        if type_paymentmethod == "us_bank_account":
            data_paymentmethod = {}

            if account_number:
                data_paymentmethod["account_number"] = account_number
            if account_type:
                data_paymentmethod["account_type"] = account_type
            if account_holder_type:
                data_paymentmethod["account_holder_type"] = account_holder_type
            if account_holder_name:
                data_paymentmethod["account_holder_name"] = account_holder_name
                params["billing_details"] = {"name": account_holder_name}
            if routing_number:
                data_paymentmethod["routing_number"] = routing_number
            if bank_name:
                data_paymentmethod["bank_name"] = bank_name
            
            params["type"] = "us_bank_account"
            params["us_bank_account"] = data_paymentmethod            
        elif type_paymentmethod == "card":
            params["type"] = "card"
            data_paymentmethod = {}
            if token_card:
                data_paymentmethod ["token"] = token_card
            else:
                if card_number:
                    data_paymentmethod["number"] = card_number
                if card_exp_month:
                    data_paymentmethod["exp_month"] = card_exp_month
                if card_exp_year:
                    data_paymentmethod["exp_year"] = card_exp_year
                if card_cvc:
                    data_paymentmethod["cvc"] = card_cvc

                params["card"] = data_paymentmethod


        payment_method = stripe.PaymentMethod.modify(**params)

        return payment_method

    @check_type_args
    def get_customer_paymentmethods(self, customer_id: str, limit: int = 0, starting_after: str = "", ending_before: str = "") -> Dict[str, Any]:
        # Implementation for retrieving customer payment methods using Stripe API
        if customer_id == "":
            raise ValueError("Customer ID cannot be empty.")
        param = {"customer": customer_id}
        if limit > 0:
            param["limit"] = limit
        if starting_after:
            param["starting_after"] = starting_after
        if ending_before:
            param["ending_before"] = ending_before


        customer_paymentmethods = stripe.Customer.list_payment_methods(**param)

        return customer_paymentmethods

    @check_type_args
    def get_paymentmethod(self, paymentmethod_id: str) -> Dict[str, Any]:
        # Implementation for retrieving a specific payment method using Stripe API
        if paymentmethod_id == "":
            raise ValueError("Payment method ID cannot be empty.")
        
        paymentmethod = stripe.PaymentMethod.retrieve(paymentmethod_id)
        return paymentmethod

    @check_type_args
    def get_paymentmethods(self, ending_before: str = "", starting_after: str = "", limit: int = 0, type: str = "") -> List[Dict[str, Any]]:
        # Implementation for listing payment methods using Stripe API
        params = {}

        if type == "":
            params["type"] = type
        if limit > 0:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before

        paymentmethods = stripe.PaymentMethod.list(**params)
        return paymentmethods

    @check_type_args
    def atach_paymentmethod_to_customer(self, paymentmethod_id: str, customer_id: str):
        # Implementation for attaching a payment method to a customer using Stripe API
        if paymentmethod_id == "":
            raise ValueError("Payment method ID cannot be empty.")
        if customer_id == "":
            raise ValueError("Customer ID cannot be empty.")
        paymentmethod = stripe.PaymentMethod.attach(payment_method=paymentmethod_id, customer=customer_id)
        return paymentmethod

    @check_type_args
    def detach_paymentmethod_from_customer(self, paymentmethod_id: str):
        # Implementation for detaching a payment method from a customer using Stripe API
        if paymentmethod_id == "":
            raise ValueError("Payment method ID cannot be empty.")
        paymentmethod = stripe.PaymentMethod.detach(payment_method=paymentmethod_id)
        return paymentmethod
