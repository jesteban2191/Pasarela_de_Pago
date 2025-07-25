from abc import ABC, abstractmethod

class RefundInterface(ABC):

    @abstractmethod
    def create_refund(self, payment_intent_id: str, amount: float = 0.0, reason: str = ""):
        """
        Create a refund for a payment intent.

        :param payment_intent_id: The ID of the payment intent to refund.
        :param amount: The amount to refund in cents. If None, refunds the full amount.
        :param reverse_transfer: Whether to reverse the transfer associated with the payment intent.
        :param refund_application_fee: Whether to refund the application fee.
        :return: A dictionary containing the refund details.
        """
        pass

    @abstractmethod
    def retrieve_refund(self, refund_id: str):
        """
        Retrieve a specific refund by its ID.

        :param refund_id: The ID of the refund to retrieve.
        :return: A dictionary containing the refund details.
        """
        pass


    @abstractmethod
    def list_refunds(self, payment_intent_id: str = "", limit: int = 100, date: str = "", ending_before: str = "", starting_after: str = ""):
        """
        List all refunds for a specific payment intent.

        :param payment_intent_id: The ID of the payment intent whose refunds are to be listed.
        :param limit: The maximum number of refunds to return.
        :param date: Filter refunds by date.
        :param ending_before: A cursor for pagination, returning refunds before this ID.
        :param starting_after: A cursor for pagination, returning refunds after this ID.
        :return: A list of dictionaries containing refund details.
        """
        pass