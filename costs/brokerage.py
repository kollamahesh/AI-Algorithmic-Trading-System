"""
costs/brokerage.py

Brokerage Calculation
"""

from config.settings import BROKERAGE_PERCENT


def calculate_brokerage(quantity, buy_price, sell_price):
    """
    Calculates total brokerage for a round-trip trade.
    """

    turnover = (buy_price + sell_price) * quantity

    brokerage = turnover * (BROKERAGE_PERCENT / 100)

    return brokerage