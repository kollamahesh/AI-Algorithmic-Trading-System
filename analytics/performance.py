"""
performance.py

Performance Analytics Module
"""


def calculate_win_rate(profits):

    total_trades = len(profits)

    if total_trades == 0:
        return 0

    wins = len(
        [p for p in profits if p > 0]
    )

    return round(
        (wins / total_trades) * 100,
        2
    )


def calculate_average_win(profits):

    wins = [
        p for p in profits
        if p > 0
    ]

    if len(wins) == 0:
        return 0

    return round(
        sum(wins) / len(wins),
        2
    )


def calculate_average_loss(profits):

    losses = [
        p for p in profits
        if p < 0
    ]

    if len(losses) == 0:
        return 0

    return round(
        sum(losses) / len(losses),
        2
    )


def calculate_profit_factor(profits):

    gross_profit = sum(
        p for p in profits
        if p > 0
    )

    gross_loss = abs(
        sum(
            p for p in profits
            if p < 0
        )
    )

    if gross_loss == 0:
        return 0

    return round(
        gross_profit / gross_loss,
        2
    )