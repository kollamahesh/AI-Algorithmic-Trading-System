"""
paper_trading/monitor.py
"""

from datetime import datetime

from paper_trading.portfolio import (
    open_positions,
    closed_positions,
    get_capital,
    update_capital
)


def check_position(symbol, current_price):

    for position in open_positions[:]:

        if position["Symbol"] != symbol:
            continue

        # -------------------------
        # TARGET HIT
        # -------------------------

        if current_price >= position["Target"]:

            profit = (
                current_price - position["Entry"]
            ) * position["Quantity"]

            capital = get_capital()

            capital += (
                position["Investment"] + profit
            )

            update_capital(capital)

            position["Exit"] = current_price
            position["Exit Time"] = datetime.now()
            position["Profit"] = round(profit, 2)
            position["Status"] = "TARGET HIT"

            open_positions.remove(position)
            closed_positions.append(position)

            print("\n================================")
            print("TARGET HIT")
            print("================================")
            print(f"Symbol : {symbol}")
            print(f"Exit   : ₹{current_price:.2f}")
            print(f"Profit : ₹{profit:.2f}")
            print(f"Capital: ₹{capital:.2f}")
            print("================================")

        # -------------------------
        # STOP LOSS
        # -------------------------

        elif current_price <= position["Stop"]:

            loss = (
                position["Entry"] - current_price
            ) * position["Quantity"]

            capital = get_capital()

            capital += (
                position["Investment"] - loss
            )

            update_capital(capital)

            position["Exit"] = current_price
            position["Exit Time"] = datetime.now()
            position["Profit"] = round(-loss, 2)
            position["Status"] = "STOP LOSS"

            open_positions.remove(position)
            closed_positions.append(position)

            print("\n================================")
            print("STOP LOSS HIT")
            print("================================")
            print(f"Symbol : {symbol}")
            print(f"Exit   : ₹{current_price:.2f}")
            print(f"Loss   : ₹{loss:.2f}")
            print(f"Capital: ₹{capital:.2f}")
            print("================================")