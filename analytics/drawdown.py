"""
drawdown.py

Calculates Maximum Drawdown.
"""


def calculate_max_drawdown(equity):

    peak = equity[0]

    max_drawdown = 0

    for value in equity:

        if value > peak:
            peak = value

        drawdown = (
            (value - peak)
            / peak
        ) * 100

        if drawdown < max_drawdown:
            max_drawdown = drawdown

    return round(max_drawdown, 2)