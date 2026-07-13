"""
equity_curve.py

Creates account equity curve.
"""

from config.settings import CAPITAL


def build_equity_curve(profits):
    """
    Builds the account equity after each trade.
    """

    equity = []

    capital = CAPITAL

    equity.append(capital)

    for profit in profits:

        capital += profit

        equity.append(round(capital, 2))

    return equity