"""
analytics/metrics.py

Calculate trading statistics from trade history.
"""

import pandas as pd
import os


FILE = "trade_journal/trade_history.csv"


def calculate_metrics():

    if not os.path.exists(FILE):

        return None

    df = pd.read_csv(FILE)

    if len(df) == 0:

        return None

    total = len(df)

    wins = df[df["Profit"] > 0]

    losses = df[df["Profit"] <= 0]

    total_profit = df["Profit"].sum()

    win_rate = len(wins) / total * 100

    avg_win = wins["Profit"].mean() if len(wins) else 0

    avg_loss = losses["Profit"].mean() if len(losses) else 0

    gross_profit = wins["Profit"].sum()

    gross_loss = abs(losses["Profit"].sum())

    if gross_loss == 0:
        profit_factor = 999
    else:
        profit_factor = gross_profit / gross_loss

    return {

        "Total Trades": total,

        "Winning Trades": len(wins),

        "Losing Trades": len(losses),

        "Net Profit": total_profit,

        "Win Rate": win_rate,

        "Average Win": avg_win,

        "Average Loss": avg_loss,

        "Profit Factor": profit_factor

    }