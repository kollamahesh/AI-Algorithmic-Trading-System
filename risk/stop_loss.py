"""
risk/stop_loss.py

Stop Loss & Target Calculations
"""

from config.settings import STOP_LOSS_PERCENT, TARGET_PERCENT


def calculate_stop_loss(entry_price):
    """
    Calculate stop loss price.
    """

    return entry_price * (
        1 - STOP_LOSS_PERCENT / 100
    )


def calculate_target(entry_price):
    """
    Calculate target price.
    """

    return entry_price * (
        1 + TARGET_PERCENT / 100
    )


def check_stop_loss(current_price, stop_loss_price):
    """
    Returns True if stop loss is hit.
    """

    return current_price <= stop_loss_price