"""
stop_loss.py

Contains functions related to
Stop Loss and Take Profit calculations.
"""


def calculate_stop_loss(entry_price, stop_percent=2):
    """
    Calculate stop-loss price.

    Example:
    Entry = 1500
    Stop = 2%

    Output:
    1470
    """

    stop_price = entry_price * (1 - stop_percent / 100)

    return round(stop_price, 2)


def calculate_target(entry_price, target_percent=4):
    """
    Calculate target price.

    Example:
    Entry = 1500
    Target = 4%

    Output:
    1560
    """

    target_price = entry_price * (1 + target_percent / 100)

    return round(target_price, 2)


def check_stop_loss(current_price, stop_price):
    """
    Returns True if stop loss is hit.
    """

    return current_price <= stop_price