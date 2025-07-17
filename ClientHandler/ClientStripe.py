from ..decorators.decorators import check_type_args
import stripe
from ..auth import *
from .client_interface import ClientHandlerInterface
from typing import Dict, Any
import pandas as pd

class StripeClient(ClientHandlerInterface):

    ####################################################################################
    ###                         Get all customers in Stripe
    ####################################################################################
    @check_type_args
    def get_customers(self) -> Dict[str, Any]:
        """Retrieve the current customer."""
        try:
            return stripe.Customer.list()
        except stripe.error.RateLimitError as e:
            # Handle rate limit errors
            print(f"Code error: {e.code}, Rate Limit Error Message: {e.user_message}")

        except stripe.error.InvalidRequestError as e:
            # Handle invalid request errors
            print(f"Code error: {e.code}, Invalid Requests Error Message: {e.user_message}")

        except stripe.error.AuthenticationError as e:
            # Handle Authentication Error
            print(f"Code error: {e.code}, Authentication Error Message: {e.user_message}")

        except stripe.error.APIConnectionError as e:
            # Handle API connection errors
            print(f"Code error: {e.code}, API Connection Error Message: {e.user_message}")

        except stripe.error.StripeError as e:
            # Handle generic Stripe errors
            print(f"Code error: {e.code}, Stripe Generic Error Message: {e.user_message}")

        except Exception as e:
            # Handle exceptions (e.g., log the error, re-raise, etc.)
            print(f"Error creating customer: {e}")
    

    ####################################################################################
    ###                         Get customer information by ID
    ####################################################################################
    @check_type_args
    def get_customer_info(self, customer_id: str) -> Dict[str, Any]:
        """Retrieve information about a specific customer."""
        if not customer_id:
            raise ValueError("Customer ID must be provided to retrieve customer information.")
        try:
            return stripe.Customer.retrieve(customer_id)
        except stripe.error.RateLimitError as e:
            # Handle rate limit errors
            print(f"Code error: {e.code}, Rate Limit Error Message: {e.user_message}")

        except stripe.error.InvalidRequestError as e:
            # Handle invalid request errors
            print(f"Code error: {e.code}, Invalid Requests Error Message: {e.user_message}")

        except stripe.error.AuthenticationError as e:
            # Handle Authentication Error
            print(f"Code error: {e.code}, Authentication Error Message: {e.user_message}")

        except stripe.error.APIConnectionError as e:
            # Handle API connection errors
            print(f"Code error: {e.code}, API Connection Error Message: {e.user_message}")

        except stripe.error.StripeError as e:
            # Handle generic Stripe errors
            print(f"Code error: {e.code}, Stripe Generic Error Message: {e.user_message}")

        except Exception as e:
            # Handle exceptions (e.g., log the error, re-raise, etc.)
            print(f"Error creating customer: {e}")

        

    ####################################################################################
    ###                         Create a new customer in Stripe
    ####################################################################################
    @check_type_args
    def create_customer(self, name: str, email: str, address: str = "", city: str = "", country: str = "", phone: str = "", state: str = "", postal_code: str = "", description: str = "", currency: str = "usd", default_payment_method: str = "", payments_methods: pd.DataFrame = pd.DataFrame()) -> Dict[str, Any]:

        if not name or not email:
            raise ValueError("Name and email must be provided to create a customer.")
        
        try:
            stripe_customer = stripe.Customer.create(
                name=name,
                email=email,
                address={
                    "line1": address,
                    "city": city,
                    "country": country,
                    "phone": phone,
                    "state": state,
                    "postal_code": postal_code
                },
                currency=currency,
                description=description,
                invoice_settings={
                    "default_payment_method": default_payment_method
                },
                metadata={
                    "description": description,
                    "payment_methods": payments_methods.to_dict(orient='records') if not payments_methods.empty else []
                }
            )
        except stripe.error.RateLimitError as e:
            # Handle rate limit errors
            print(f"Code error: {e.code}, Rate Limit Error Message: {e.user_message}")

        except stripe.error.InvalidRequestError as e:
            # Handle invalid request errors
            print(f"Code error: {e.code}, Invalid Requests Error Message: {e.user_message}")

        except stripe.error.AuthenticationError as e:
            # Handle Authentication Error
            print(f"Code error: {e.code}, Authentication Error Message: {e.user_message}")

        except stripe.error.APIConnectionError as e:
            # Handle API connection errors
            print(f"Code error: {e.code}, API Connection Error Message: {e.user_message}")

        except stripe.error.StripeError as e:
            # Handle generic Stripe errors
            print(f"Code error: {e.code}, Stripe Generic Error Message: {e.user_message}")

        except Exception as e:
            # Handle exceptions (e.g., log the error, re-raise, etc.)
            print(f"Error creating customer: {e}")


        return stripe_customer
    
    ####################################################################################
    ###                         Update an existing customer in Stripe
    ####################################################################################
    
    @check_type_args
    def update_customer(self, customer_id: str, name: str = "", email: str = "", address: str = "", city: str = "", country: str = "", phone: str = "", state: str = "", postal_code: str = "", description: str = "", currency: str = "usd", default_payment_method: str = "", payments_methods: pd.DataFrame = pd.DataFrame()) -> Dict[str, Any]:
        """Update an existing customer with the provided details."""
        

        if not customer_id:
            raise ValueError("Customer ID must be provided for updating a customer.")
    
        try:
            customer = stripe.Customer.modify(
                customer_id,
                name=name,
                email=email,
                address={
                    "line1": address,
                    "city": city,
                    "country": country,
                    "phone": phone,
                    "state": state,
                    "postal_code": postal_code
                },
                currency=currency,
                invoice_settings={
                    "default_payment_method": default_payment_method
                },
                metadata={
                    "description": description,
                    "payment_methods": payments_methods.to_dict(orient='records') if not payments_methods.empty else []
                }
            )
        except stripe.error.RateLimitError as e:
            # Handle rate limit errors
            print(f"Code error: {e.code}, Rate Limit Error Message: {e.user_message}")

        except stripe.error.InvalidRequestError as e:
            # Handle invalid request errors
            print(f"Code error: {e.code}, Invalid Requests Error Message: {e.user_message}")

        except stripe.error.AuthenticationError as e:
            # Handle Authentication Error
            print(f"Code error: {e.code}, Authentication Error Message: {e.user_message}")

        except stripe.error.APIConnectionError as e:
            # Handle API connection errors
            print(f"Code error: {e.code}, API Connection Error Message: {e.user_message}")

        except stripe.error.StripeError as e:
            # Handle generic Stripe errors
            print(f"Code error: {e.code}, Stripe Generic Error Message: {e.user_message}")

        except Exception as e:
            # Handle exceptions (e.g., log the error, re-raise, etc.)
            print(f"Error updating customer: {e}")

        return customer
    
    ####################################################################################
    ###                         Delete a customer in Stripe
    ####################################################################################
    @check_type_args
    def delete_customer(self, customer_id: str) -> Dict[str, Any]:
        """Delete a customer by their ID."""
        if not customer_id:
            raise ValueError("Customer ID must be provided for deletion.")
        try:
            stripe.Customer.delete(customer_id)
        except stripe.error.RateLimitError as e:
            # Handle rate limit errors
            print(f"Code error: {e.code}, Rate Limit Error Message: {e.user_message}")

        except stripe.error.InvalidRequestError as e:
            # Handle invalid request errors
            print(f"Code error: {e.code}, Invalid Requests Error Message: {e.user_message}")

        except stripe.error.AuthenticationError as e:
            # Handle Authentication Error
            print(f"Code error: {e.code}, Authentication Error Message: {e.user_message}")

        except stripe.error.APIConnectionError as e:
            # Handle API connection errors
            print(f"Code error: {e.code}, API Connection Error Message: {e.user_message}")

        except stripe.error.StripeError as e:
            # Handle generic Stripe errors
            print(f"Code error: {e.code}, Stripe Generic Error Message: {e.user_message}")

        except Exception as e:
            # Handle exceptions (e.g., log the error, re-raise, etc.)
            print(f"Error updating customer: {e}")


    
    ####################################################################################
    ###                         Search customer in Stripe by query
    ####################################################################################
    @check_type_args
    def search_customers(self, query: str) -> Dict[str, Any]:
        """Search for customers based on a query."""
        if not query:
            raise ValueError("Query must be provided for searching customers.")
        
        try:
            return stripe.Customer.search(query=query)
        except stripe.error.RateLimitError as e:
            # Handle rate limit errors
            print(f"Code error: {e.code}, Rate Limit Error Message: {e.user_message}")

        except stripe.error.InvalidRequestError as e:
            # Handle invalid request errors
            print(f"Code error: {e.code}, Invalid Requests Error Message: {e.user_message}")

        except stripe.error.AuthenticationError as e:
            # Handle Authentication Error
            print(f"Code error: {e.code}, Authentication Error Message: {e.user_message}")

        except stripe.error.APIConnectionError as e:
            # Handle API connection errors
            print(f"Code error: {e.code}, API Connection Error Message: {e.user_message}")

        except stripe.error.StripeError as e:
            # Handle generic Stripe errors
            print(f"Code error: {e.code}, Stripe Generic Error Message: {e.user_message}")

        except Exception as e:
            # Handle exceptions (e.g., log the error, re-raise, etc.)
            print(f"Error searching customers: {e}")