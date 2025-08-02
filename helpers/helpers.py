from ..decorators.decorators import check_type_args
from datetime import datetime, timedelta
from typing import Dict, Any
import os

@check_type_args
def convert_to_cents(amount: float) -> int:
    return int(amount * 100)

@check_type_args
def convert_date_to_timestamp(date_str: str) -> int:
    """
    Convert a date string in the format 'DD/MM/YYYY' to a Unix timestamp.
    
    :param date_str: Date string to convert.
    :return: Unix timestamp.
    """
    try:
        dt = datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Invalid date format. Please use 'DD/MM/YYYY'.")
    
    # Convert datetime to Unix timestamp
    return int(dt.timestamp())



def get_trm(currency_base: str, currency_quote: list[str]) -> float:
    """
    Get the TRM (Tasa Representativa del Mercado) for a given currency pair.
    
    :param currency_base: Base currency code.
    :param currency_quote: Quote currency code.
    :param trm_data: Dictionary containing TRM data.
    :return: TRM value for the specified currency pair.
    """
    api_key_trm = os.getenv('API_KEY_TRM')
    date = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")

    url_request = f"https://api.exchangeratesapi.io/v1/{date}?access_key={api_key_trm}&base={currency_base}&symbols={','.join(currency_quote)}"