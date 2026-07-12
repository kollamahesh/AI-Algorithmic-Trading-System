"""
sharpe_ratio.py

Calculates Sharpe Ratio.
"""

import numpy as np


def calculate_sharpe_ratio(profits):

    if len(profits) < 2:
        return 0

    profits = np.array(profits)

    average_return = np.mean(profits)

    std_return = np.std(profits)

    if std_return == 0:
        return 0

    sharpe = average_return / std_return

    return round(sharpe, 2)