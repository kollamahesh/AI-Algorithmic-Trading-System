"""
brokerage.py

Simple brokerage calculator for backtesting.
"""

import config


def calculate_brokerage(quantity, buy_price, sell_price):

    turnover = (
        buy_price + sell_price
    ) * quantity

    brokerage = (
        turnover *
        config.BROKERAGE_PERCENT / 100
    )

    return round(brokerage, 2)