"""
paper_trading/trader.py

Paper Trading Module
"""

from datetime import datetime

from paper_trading.portfolio import (
    open_positions,
    add_position,
    get_capital,
    update_capital,
    commit,
)


def buy_stock(symbol, entry, stop, target, quantity):

    # ==========================================
    # Prevent Duplicate Positions
    # ==========================================

    for position in open_positions:

        if (
            position["Symbol"] == symbol
            and position["Status"] == "OPEN"
        ):

            print(f"\nAlready holding {symbol}")

            return False

    # ==========================================
    # Capital Check
    # ==========================================

    investment = entry * quantity

    capital = get_capital()

    if investment > capital:

        print(f"\nNot enough capital to buy {symbol}")

        return False

    # ==========================================
    # Update Capital
    # ==========================================

    update_capital(capital - investment)

    # ==========================================
    # Create Position
    # ==========================================

    position = {

        "Symbol": symbol,

        "Entry": entry,

        "Stop": stop,

        "Target": target,

        "Quantity": quantity,

        "Investment": investment,

        "Entry Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "Status": "OPEN"

    }

    add_position(position)

    # ==========================================
    # Save Portfolio (ONE SAVE ONLY)
    # ==========================================

    commit()

    # ==========================================
    # Confirmation
    # ==========================================

    print("\n====================================")
    print("PAPER BUY ORDER")
    print("====================================")
    print(f"Symbol      : {symbol}")
    print(f"Entry       : ₹{entry:.2f}")
    print(f"Quantity    : {quantity}")
    print(f"Investment  : ₹{investment:.2f}")
    print(f"Capital Left: ₹{get_capital():.2f}")
    print("====================================")

    return True