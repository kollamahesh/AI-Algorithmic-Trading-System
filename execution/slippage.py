"""
execution/slippage.py

Handles buy and sell slippage.
"""

from config.settings import SLIPPAGE_PERCENT


def apply_buy_slippage(price):
    """
    Apply slippage when buying.

    Example:
    Price = 100
    Slippage = 0.10%

    Buy Price = 100.10
    """

    return price * (1 + SLIPPAGE_PERCENT / 100)


def apply_sell_slippage(price):
    """
    Apply slippage when selling.

    Example:
    Price = 100
    Slippage = 0.10%

    Sell Price = 99.90
    """

    return price * (1 - SLIPPAGE_PERCENT / 100)