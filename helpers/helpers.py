from ..decorators.decorators import check_type_args
from datetime import datetime
from typing import Dict, Any

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