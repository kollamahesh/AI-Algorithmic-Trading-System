"""
equity_curve.py

Creates account equity curve.
"""

import config


def build_equity_curve(profits):

    equity = []

    capital = config.INITIAL_CAPITAL

    equity.append(capital)

    for profit in profits:

        capital += profit

        equity.append(round(capital, 2))

    return equity