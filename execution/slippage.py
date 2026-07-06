"""
slippage.py

Functions for simulating execution slippage.
"""


def apply_buy_slippage(price, slippage_percent=0.05):
    """
    Buy orders become slightly more expensive.
    """

    actual_price = price * (1 + slippage_percent / 100)

    return round(actual_price, 2)


def apply_sell_slippage(price, slippage_percent=0.05):
    """
    Sell orders receive a slightly lower price.
    """

    actual_price = price * (1 - slippage_percent / 100)

    return round(actual_price, 2)


def calculate_slippage(expected_price, actual_price):
    """
    Returns slippage amount.
    """

    return round(actual_price - expected_price, 2)