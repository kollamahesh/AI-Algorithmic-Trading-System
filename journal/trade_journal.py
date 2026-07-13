"""
trade_journal.py

Trade Journal Module
"""

import datetime
import pandas as pd

# Stores all completed trades
trade_history = []


def add_trade(
    symbol,
    entry_price,
    exit_price,
    quantity,
    stop_loss,
    target,
    gross_profit,
    brokerage,
    net_profit,
    exit_reason
):
    """
    Store one completed trade
    """

    trade = {

        "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "Symbol": symbol,

        "Entry Price": round(entry_price, 2),

        "Exit Price": round(exit_price, 2),

        "Quantity": quantity,

        "Stop Loss": round(stop_loss, 2),

        "Target": round(target, 2),

        "Gross Profit": round(gross_profit, 2),

        "Brokerage": round(brokerage, 2),

        "Net Profit": round(net_profit, 2),

        "Exit Reason": exit_reason

    }

    trade_history.append(trade)


def get_trade_history():
    """
    Return all completed trades
    """

    return trade_history


def save_trade_history(filename="trade_history.csv"):
    """
    Save trade history to CSV
    """

    if len(trade_history) == 0:
        return

    df = pd.DataFrame(trade_history)

    df.to_csv(
        filename,
        index=False
    )

    print(f"\nTrade history saved to {filename}")