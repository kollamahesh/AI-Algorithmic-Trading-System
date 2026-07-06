"""
brokerage.py

Simple brokerage calculator for backtesting.
"""


def calculate_brokerage(quantity, buy_price, sell_price):
    """
    Calculates brokerage using a simplified model.

    Assumption:
    Flat 0.1% of turnover.
    """

    turnover = (buy_price + sell_price) * quantity

    brokerage = turnover * 0.001

    return round(brokerage, 2)