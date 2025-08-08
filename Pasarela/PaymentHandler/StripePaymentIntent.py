from .payment_interface import PaymentInterface
import stripe
from ..helpers.helpers import *
from ..decorators.decorators import check_type_args
from typing import Dict, Any


class StripePaymentIntent(PaymentInterface):

    @check_type_args
    def create_payment(self, amount: float, currency: str, payment_method_id: str, customer_id: str = "", description: str = "")-> Dict[str, Any]:
        """
        Create a payment using Stripe's Payment Intent API.
        
        :param amount: Amount to be charged in the currency unit.
        :param currency: Currency of the payment.
        :param payment_method_id: ID of the payment method to be used.
        :param customer_id: ID of the customer making the payment.
        :param description: Optional description for the payment.
        :return: Payment object or identifier.
        """
        amount_in_cents = convert_to_cents(amount)

        params = {"amount": amount_in_cents, "currency": currency, "payment_method": payment_method_id, "confirm": True, "confirmation_method": "automatic"}

        if customer_id:
            params["customer"] = customer_id
        if description:
            params["description"] = description
        
        try:
            payment_intent = stripe.PaymentIntent.create(**params)
        except stripe.error.CardError as e:
            # Handle card errors
            print(f"Code error: {e.code}, Card Error Message: {e.user_message}")

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

        return payment_intent
    
    @check_type_args
    def retrieve_payment(self, payment_intent_id: str) -> Dict[str, Any]:

        if payment_intent_id in ["", " "]:
            raise ValueError("Payment intent ID cannot be empty.")
        

        try:     
            paymentintent = stripe.PaymentIntent.retrieve(payment_intent_id)
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
        

        return paymentintent
    
    @check_type_args
    def list_all_paymentintents(self, customer_id: str = "", date: int = 0, limit: int = 100, starting_after: str = "", ending_before: str = "") -> Dict[str, Any]:
        """
        List all payment intents for a customer.
        
        :param customer_id: ID of the customer whose payment intents are to be listed.
        :param date: Optional date filter for the payment intents.
        :param limit: Optional limit on the number of payment intents to return.
        :param starting_after: Optional cursor for pagination.
        :param ending_before: Optional cursor for pagination.
        :return: List of payment intents.
        """
        params = {}
        
        if customer_id:
            params["customer"] = customer_id
        if date:
            date = convert_date_to_timestamp(date)
            params["created"] = {"gte": date}
        if limit:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        
        try:
            payment_intents = stripe.PaymentIntent.list(**params)
            has_more = payment_intents['has_more']

            list_payment_intents = payment_intents['data']

            while has_more:

                params["starting_after"] = list_payment_intents[-1]['id']
                payment_intents = stripe.PaymentIntent.list(**params)
                has_more = payment_intents['has_more']
                list_payment_intents.extend(payment_intents['data'])


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
            
        return list_payment_intents
        
