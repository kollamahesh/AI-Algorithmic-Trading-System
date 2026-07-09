"""
trade_journal.py

Stores completed trades.
"""

# List that stores all completed trades
trade_history = []


def add_trade(
    entry_price,
    exit_price,
    quantity,
    exit_reason,
    profit
):
    """
    Store one completed trade.
    """

    trade = {

        "Entry Price": round(entry_price, 2),

        "Exit Price": round(exit_price, 2),

        "Quantity": quantity,

        "Exit Reason": exit_reason,

        "Profit": round(profit, 2)

    }

    trade_history.append(trade)


def get_trade_history():
    """
    Return all completed trades.
    """

    return trade_history