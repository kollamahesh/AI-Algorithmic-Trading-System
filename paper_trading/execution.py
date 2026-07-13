"""
paper_trading/execution.py

Paper Trading Execution Engine
"""

from datetime import datetime
from trade_journal.journal import save_trade
from kite_api.live_price import get_live_price

from paper_trading.portfolio import (
    get_capital,
    update_capital,
    add_position,
    close_position,
    get_open_positions,
    commit,
)


# ==========================================================
# BUY ORDER
# ==========================================================

def execute_paper_trade(trade):

    capital = get_capital()

    investment = trade["Investment"]

    if investment > capital:
        return False, "Not enough capital."

    for position in get_open_positions():

        if position["Symbol"] == trade["Symbol"]:
            return False, "Position already exists."

    position = {

        "Symbol": trade["Symbol"],

        "Entry": trade["Entry"],

        "Stop": trade["Stop"],

        "Target": trade["Target"],

        "Quantity": trade["Quantity"],

        "Investment": investment,

        "Entry Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "Status": "OPEN"

    }

    add_position(position)

    update_capital(capital - investment)

    commit()

    return True, "Trade Executed Successfully."


# ==========================================================
# SELL ORDER
# ==========================================================

def close_paper_trade(symbol):

    positions = get_open_positions()

    for position in positions:

        if position["Symbol"] == symbol:

            try:
                exit_price = get_live_price(symbol)
            except Exception:
                exit_price = position["Entry"]

            investment = position["Investment"]
            quantity = position["Quantity"]
            entry = position["Entry"]

            sale_value = exit_price * quantity
            profit = sale_value - investment
            return_pct = (profit / investment) * 100

            capital = get_capital()
            capital += sale_value

            update_capital(capital)

            position["Exit"] = round(exit_price, 2)
            position["Exit Time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            position["Sale Value"] = round(sale_value, 2)
            position["Profit"] = round(profit, 2)
            position["Return %"] = round(return_pct, 2)
            position["Status"] = "CLOSED"

            trade = {

                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

                "Symbol": symbol,

                "Entry": round(entry, 2),

                "Exit": round(exit_price, 2),

                "Quantity": quantity,

                "Investment": round(investment, 2),

                "Sale Value": round(sale_value, 2),

                "Profit": round(profit, 2),

                "Return %": round(return_pct, 2),

                "Status": "CLOSED"

            }

            save_trade(trade)

            close_position(position)

            commit()

            return True, f"Trade Closed. P/L : ₹{profit:.2f}"

    return False, "Position not found."

# ==========================================================
# HELPERS
# ==========================================================

def has_open_position(symbol):

    for position in get_open_positions():

        if position["Symbol"] == symbol:
            return True

    return False


def get_position(symbol):

    for position in get_open_positions():

        if position["Symbol"] == symbol:
            return position

    return None