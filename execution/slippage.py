"""
slippage.py

Functions for simulating execution slippage.
"""


import config


def apply_buy_slippage(price):
    actual_price = price * (
        1 + config.SLIPPAGE_PERCENT / 100
    )

    return round(actual_price, 2)


def apply_sell_slippage(price):
    actual_price = price * (
        1 - config.SLIPPAGE_PERCENT / 100
    )

    return round(actual_price, 2)


def calculate_slippage(expected_price, actual_price):
    return round(actual_price - expected_price, 2)