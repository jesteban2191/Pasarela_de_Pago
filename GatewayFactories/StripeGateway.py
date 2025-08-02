from .Gatewayinterface import GatewayInterface
from typing import List, Dict, Any
import pandas as pd
from ..auth import *
from ..ClientHandler import *
from ..PaymentHandler import *
from ..PaymenMethodtHandler import *
from ..RefundHandler import *
from ..decorators import check_type_args
import stripe

class StripeFactory(GatewayInterface):

    def __init__(self):
        self._auth = AuthContext(StripeAuth())
        self._gateway = "stripe"
        self._token = self._auth.get_token()
        stripe.api_key = self._token
        self._client = ClientFactory.get_client(self._gateway)
        self._payment = PaymentIntentFactory.get_payment(self._gateway)
        self._payment_method = PaymentMethodFactory.get_payment_method(self._gateway)
        self._refund = RefundFactory.get_refund(self._gateway)

    ################################################################################################
    ###                         Methods for client management
    ################################################################################################
    @check_type_args
    def get_clients(self) ->  pd.DataFrame:

        list_all_customers = self._client.get_customers()
        if not list_all_customers:
            raise ValueError("No customers found.")
        
        df_customers = pd.DataFrame(list_all_customers)
        df_customers = pd.json_normalize(df_customers)

        return df_customers
    

    @check_type_args
    def get_client(self, client_id: str) -> pd.DataFrame:
        """
        Get a specific client by ID.
        """
        client_info = self._client.get_customer_info(client_id)
        if not client_info:
            raise ValueError(f"Client with ID {client_id} not found.")
        
        df_client_info = pd.DataFrame([client_info])
        df_client_info = pd.json_normalize(df_client_info)
        return df_client_info
    

    
    @check_type_args
    def create_client(self, name: str, email: str, address: str = "", city: str = "", country: str = "", phone: str = "", state: str = "", postal_code: str = "", description: str = "", currency: str = "usd", default_payment_method: str = "", payments_methods: pd.DataFrame = pd.DataFrame()):
        
        query = f"email:'{email}'"
        client_already_created = self._client.search_customers(query=query)
        client_already_created_info = client_already_created.get("data", [])

        if not client_already_created_info:

            created_client = self._client.create_customer(name, email, address, city, country, phone, state, postal_code, description, currency, default_payment_method, payments_methods)

            if not created_client:
                raise ValueError("Failed to create client.")
            
            df_created_client = pd.DataFrame([created_client])
            df_created_client = pd.json_normalize(df_created_client)
        else:
            df_created_client = pd.DataFrame(client_already_created_info)
            df_created_client = pd.json_normalize(df_created_client)
            print(f"Client with email {email} already exists. Returning existing client data.")

        return df_created_client
    

    @check_type_args
    def update_client(self, customer_id: str, name: str = "", email: str = "", address: str = "", city: str = "", country: str = "", phone: str = "", state: str = "", postal_code: str = "", description: str = "", currency: str = "usd", default_payment_method: str = "", payments_methods: pd.DataFrame = pd.DataFrame()):
        
        updated_client = self._client.update_customer(customer_id, name, email, address, city, country, phone, state, postal_code, description, currency, default_payment_method, payments_methods)

        if not updated_client:
            raise ValueError(f"Failed to update client with ID {customer_id}.")
        
        df_updated_client = pd.DataFrame([updated_client])
        df_updated_client = pd.json_normalize(df_updated_client)

        return df_updated_client
    

    @check_type_args
    def delete_client(self, customer_id: str) -> bool:
        deleted_client = self._client.delete_customer(customer_id)
        if not deleted_client:
            raise ValueError(f"Failed to delete client with ID {customer_id}.")
        
        df_deleted_client = pd.DataFrame([deleted_client])

        return df_deleted_client

    ################################################################################################
    ###                         Methods for payment method management
    ################################################################################################

    @check_type_args
    def create_payment_method(self, type_paymentmethod: str, customer_id: str = "", account_number: str = "", account_type: str = "", account_holder_type: str = "", account_holder_name: str = "", routing_number: str = "", bank_name: str = "",card_number: str = "", card_exp_month: str = "", card_exp_year: str = "", card_cvc: str = "", token_card: str = ""):        

        if customer_id:
            list_paymentmethods = self._payment_method.get_customer_paymentmethods(customer_id)
        else:
            list_paymentmethods = self._payment_method.get_paymentmethods()        

        if list_paymentmethods:
            df_paymentmethods = pd.DataFrame(list_paymentmethods)
            df_paymentmethods = pd.json_normalize(df_paymentmethods)



            if not df_paymentmethods.empty:
                filtro = pd.Series([True] * len(df_paymentmethods))
                
                if type_paymentmethod == "us_bank_account" and account_number and account_type:
                    filtro &= (df_paymentmethods["type"] == "us_bank_account")
                    filtro &= (df_paymentmethods["account_number"] == account_number)
                    filtro &= (df_paymentmethods["account_type"] == account_type)
                elif type_paymentmethod == "card" and card_number and card_exp_month and card_exp_year:
                    filtro &= (df_paymentmethods["type"] == "card")
                    filtro &= (df_paymentmethods["card_number"] == card_number)
                elif type_paymentmethod == "card" and token_card:
                    filtro &= (df_paymentmethods["type"] == "card")
                    filtro &= (df_paymentmethods["token"] == token_card)

                df_paymentmethods_filtered = df_paymentmethods[filtro]

                if df_paymentmethods_filtered.empty:
                    print(f"Creating the new payment method")
                    has_to_create = True

                else:
                    print(f"Payment method already exists, returning existing payment method data")
                    df_paymentmethod = pd.json_normalize(df_paymentmethods_filtered)

        else: 
            has_to_create = True


        if has_to_create:
            paymentmethod = self._payment_method.create_paymentmethod(
                        type=type_paymentmethod,
                        customer_id=customer_id,
                        account_number=account_number,
                        account_type=account_type,
                        account_holder_type=account_holder_type,
                        account_holder_name=account_holder_name,
                        routing_number=routing_number,
                        bank_name=bank_name,
                        card_number=card_number,
                        card_exp_month=card_exp_month,
                        card_exp_year=card_exp_year,
                        card_cvc=card_cvc,
                        token_card=token_card
                    )

            df_paymentmethod = pd.DataFrame([paymentmethod])

            df_paymentmethod = pd.json_normalize(df_paymentmethod)
        else: 
            df_paymentmethod = df_paymentmethods_filtered

        return df_paymentmethod
    

    @check_type_args
    def update_payment_method(self, paymentmethod_id: str, type_paymentmethod: str, account_number: str = "", account_type: str = "", account_holder_type: str = "", account_holder_name: str = "", routing_number: str = "", bank_name: str = "",card_number: str = "", card_exp_month: str = "", card_exp_year: str = "", card_cvc: str = "", token_card: str = ""):

        if paymentmethod_id:
            if type_paymentmethod in ["us_bank_account", "card"]:
                paymentmethod = self._payment_method.get_paymentmethod(paymentmethod_id)
                if not paymentmethod:
                    raise ValueError(f"Payment method with ID {paymentmethod_id} not found.")
                else:
                    paymentmethod_updated = self._payment_method.update_paymentmethod(
                        paymentmethod_id=paymentmethod_id,
                        type=type_paymentmethod,
                        account_number=account_number,
                        account_type=account_type,
                        account_holder_type=account_holder_type,
                        account_holder_name=account_holder_name,
                        routing_number=routing_number,
                        bank_name=bank_name,
                        card_number=card_number,
                        card_exp_month=card_exp_month,
                        card_exp_year=card_exp_year,
                        card_cvc=card_cvc,
                        token_card=token_card
                    )

                    if not paymentmethod_updated:
                        raise ValueError(f"Failed to update payment method with ID {paymentmethod_id}.")
                    
                    df_paymentmethod_updated = pd.DataFrame([paymentmethod_updated])
                    df_paymentmethod_updated = pd.json_normalize(df_paymentmethod_updated)
            
            else:
                raise ValueError("Invalid payment method type. Must be 'us_bank_account' or 'card'.")

        else:
            raise ValueError("Payment method ID cannot be empty.")
        
        return df_paymentmethod_updated
    

    @check_type_args
    def get_client_paymentmethods(self, customer_id: str, limit: int = 0, starting_after: str = "", ending_before: str = ""):

        if customer_id:
            list_paymentmethods = self._payment_method.get_customer_paymentmethods(customer_id, limit, starting_after, ending_before)
            if list_paymentmethods:
                df_client_paymentmethods = pd.DataFrame(list_paymentmethods)
                df_client_paymentmethods = pd.json_normalize(df_client_paymentmethods)
            else:
                raise ValueError(f"No payment methods found for client with ID {customer_id}.")
        else:
            raise ValueError("Customer ID cannot be empty.")
        
        return df_client_paymentmethods
    

    @check_type_args
    def get_payment_method(self, paymentmethod_id: str):

        if paymentmethod_id:
            paymentmethod = self._payment_method.get_paymentmethod(paymentmethod_id)
            if paymentmethod:
                df_paymentmethod = pd.DataFrame([paymentmethod])
                df_paymentmethod = pd.json_normalize(df_paymentmethod)
            else:
                print(f"Payment method with ID {paymentmethod_id} not found.")
            
        else:
            raise ValueError("Payment method ID cannot be empty.")
        
        return df_paymentmethod


    @check_type_args
    def get_payment_methods(self, ending_before: str = "", starting_after: str = "", limit: int = 0, type: str = ""):

        list_all_paymentmethods = self._payment_method.get_paymentmethods(ending_before, starting_after, limit, type)
        if list_all_paymentmethods:
            df_paymentmethods = pd.DataFrame(list_all_paymentmethods)
            df_paymentmethods = pd.json_normalize(df_paymentmethods)
        else:
            print(f"There are not Payment Method alredy created")

        return list_all_paymentmethods
    

    @check_type_args
    def atach_paymentmethod_to_client(self, paymentmethod_id: str, customer_id: str):

        list_client = self._client.get_customer_info(customer_id)

        if list_client:
            paymentmethod_attached = self._payment_method.atach_paymentmethod_to_customer(paymentmethod_id, customer_id)

            df_paymentmethod_attached = pd.DataFrame([paymentmethod_attached])
            df_paymentmethod_attached = pd.json_normalize(df_paymentmethod_attached)

        else:
            raise ValueError(f"Client with ID {customer_id} does not exist.")
        
        return df_paymentmethod_attached


    @check_type_args
    def detach_paymentmethod_from_client(self, paymentmethod_id: str, customer_id: str):

        list_client = self._client.get_customer_info(customer_id)

        if list_client:
            paymentmethod_detached = self._payment_method.detach_paymentmethod_from_customer(paymentmethod_id, customer_id)

            df_paymentmethod_detached = pd.DataFrame([paymentmethod_detached])
            df_paymentmethod_detached = pd.json_normalize(df_paymentmethod_detached)

        else:
            raise ValueError(f"Client with ID {customer_id} does not exist.")
        
        return df_paymentmethod_detached
    

    ################################################################################################
    ###                         Abstract methods for paymentintent management
    ################################################################################################

    @check_type_args
    def create_payment(self, amount: float, currency: str, payment_method_id: str, customer_id: str = "", description: str = ""):

        if customer_id:
            list_client = self._client.get_customer_info(customer_id)

            if list_client:
                valid_client = True
            else:
                raise ValueError(f"Client with ID {customer_id} does not exist.")
            
        else:
            valid_client = True


        paymentintent = self._payment.create_payment(
            amount=amount,
            currency=currency,
            payment_method_id=payment_method_id,
            customer_id=customer_id,
            description=description
        )

        if paymentintent:
            df_paymentintent = pd.DataFrame([paymentintent])
            df_paymentintent = pd.json_normalize(df_paymentintent)
        else:
            raise ValueError("Failed to create payment intent.")
        
        return df_paymentintent
    

    @check_type_args
    def get_payment(self, payment_intent_id: str):
        if payment_intent_id:
            payment_intent = self._payment.retrieve_payment(payment_intent_id)
            if payment_intent:
                df_payment_intent = pd.DataFrame([payment_intent])
                df_payment_intent = pd.json_normalize(df_payment_intent)
            else:
                raise ValueError(f"Payment intent with ID {payment_intent_id} not found.")
        else:
            raise ValueError("Payment intent ID cannot be empty.")
        
        return df_payment_intent
    

    @check_type_args
    def get_list_payments(self, customer_id: str = "", date: int = 0, limit: int = 100, starting_after: str = "", ending_before: str = ""):

        list_all_paymentintents = self._payment.list_all_paymentintents(customer_id, date, limit, starting_after, ending_before)
        if list_all_paymentintents:
            df_paymentintents = pd.DataFrame(list_all_paymentintents)
            df_paymentintents = pd.json_normalize(df_paymentintents)
        else:
            print(f"There are not Payment Intents alredy created")

        return df_paymentintents
    
    ################################################################################################
    ###                         Abstract methods for refund management
    ################################################################################################

    @check_type_args
    def create_refund(self,  payment_intent_id: str, amount: float = 0.0, reason: str = "") -> pd.DataFrame:
        if payment_intent_id:

            list_payment_intent = self._payment.retrieve_payment(payment_intent_id)

            if list_payment_intent:
                refund = self._refund.create_refund(payment_intent_id, amount, reason)

                if refund:
                    df_refund = pd.DataFrame([refund])
                    df_refund = pd.json_normalize(df_refund)
                else:
                    raise ValueError("Failed to create refund.")
                
            else:
                raise ValueError(f"Payment intent with ID {payment_intent_id} not found.")
        else:
            raise ValueError("Payment intent ID cannot be empty.")
        
        return df_refund
    

    @check_type_args
    def get_refund(self, refund_id: str):

        if refund_id:
            refund = self._refund.retrieve_refund(refund_id)
            if refund:
                df_refund = pd.DataFrame([refund])
                df_refund = pd.json_normalize(df_refund)
            else:
                raise ValueError(f"Refund with ID {refund_id} not found.")
        else:
            raise ValueError("Refund ID cannot be empty.")
        
        return df_refund
    

    @check_type_args
    def get_list_refunds(self, payment_intent_id: str = "", limit: int = 0, date: str = "", ending_before: str = "", starting_after: str = ""):

        list_refunds = self._refund.list_refunds(payment_intent_id, limit, date, ending_before, starting_after)
        if list_refunds:
            df_refunds = pd.DataFrame(list_refunds)
            df_refunds = pd.json_normalize(df_refunds)
        else:
            print(f"There are not Refunds alredy created")

        return df_refunds
