"""
monthly_returns.py

Calculates monthly profit.
"""

from collections import defaultdict


def calculate_monthly_returns(history):

    monthly = defaultdict(float)

    for trade in history:

        month = trade["Date"][:7]      # YYYY-MM

        monthly[month] += trade["Net Profit"]

    return dict(monthly)