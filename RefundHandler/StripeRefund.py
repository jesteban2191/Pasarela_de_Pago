from .refundinterface import RefundInterface
from ..decorators.decorators import check_type_args
from ..helpers.helpers import *
import stripe
from typing import Dict, Any

class StripeRefund(RefundInterface):

    @check_type_args
    def create_refund(self, payment_intent_id: str, amount: float = 0.0, reason: str = "requested_by_customer") -> Dict[str, Any]:

        params = {"payment_intent": payment_intent_id, "reason": reason}

        if amount > 0.0:
            amount_in_cents = convert_to_cents(amount)
            params["amount"] = amount_in_cents

        try:
            refund = stripe.Refund.create(**params)
        except stripe.error.CardError as e:
            print(f"Card Error: {e.user_message}")
        except stripe.error.RateLimitError as e:
            print(f"Rate Limit Error: {e.user_message}")
        except stripe.error.InvalidRequestError as e:
            print(f"Invalid Request Error: {e.user_message}")
        except stripe.error.AuthenticationError as e:
            print(f"Authentication Error: {e.user_message}")
        except stripe.error.APIConnectionError as e:
            print(f"API Connection Error: {e.user_message}")
        except stripe.error.StripeError as e:
            print(f"Stripe Error: {e.user_message}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        return refund
    

    @check_type_args
    def retrieve_refund(self, refund_id: str) -> Dict[str, Any]:
        try:
            refund = stripe.Refund.retrieve(refund_id)
            
        except stripe.error.InvalidRequestError as e:
            print(f"Invalid Request Error: {e.user_message}")
        except stripe.error.AuthenticationError as e:
            print(f"Authentication Error: {e.user_message}")
        except stripe.error.APIConnectionError as e:
            print(f"API Connection Error: {e.user_message}")
        except stripe.error.StripeError as e:
            print(f"Stripe Error: {e.user_message}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        return refund
    
    @check_type_args
    def list_refunds(self, payment_intent_id: str = "", limit: int = 0, date: str = "", ending_before: str = "", starting_after: str = "") -> Dict[str, Any]:
        params = {}

        if payment_intent_id:
            params["payment_intent"] = payment_intent_id

        if date:
            timestamp = convert_date_to_timestamp(date)
            params["created"] = {"gte": timestamp}

        if not params:
            if limit > 0:
                params["limit"] = limit
            else:
                params["limit"] = 100

        try:
            refunds = stripe.Refund.list(**params)
            has_more = refunds['has_more']
            list_refunds = refunds['data']

            while has_more:

                params["starting_after"] = list_refunds[-1].id
                refunds = stripe.Refund.list(**params)
                has_more = refunds['has_more']
                list_refunds.extend(refunds['data'])

        except stripe.error.InvalidRequestError as e:
            print(f"Invalid Request Error: {e.user_message}")
        except stripe.error.AuthenticationError as e:
            print(f"Authentication Error: {e.user_message}")
        except stripe.error.APIConnectionError as e:
            print(f"API Connection Error: {e.user_message}")
        except stripe.error.StripeError as e:
            print(f"Stripe Error: {e.user_message}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        return list_refunds
