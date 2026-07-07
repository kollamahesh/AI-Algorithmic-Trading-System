"""
stop_loss.py

Contains functions related to
Stop Loss and Take Profit calculations.
"""


import config


def calculate_stop_loss(entry_price):
    stop_price = entry_price * (
        1 - config.STOP_LOSS_PERCENT / 100
    )

    return round(stop_price, 2)


def calculate_target(entry_price):
    target_price = entry_price * (
        1 + config.TARGET_PERCENT / 100
    )

    return round(target_price, 2)


def check_stop_loss(current_price, stop_price):
    return current_price <= stop_price