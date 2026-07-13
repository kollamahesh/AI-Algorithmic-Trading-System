"""
paper_trading/monitor.py

Automatic Position Monitor
"""

from kite_api.live_price import get_live_price
from paper_trading.execution import close_paper_trade
from paper_trading.portfolio import get_open_positions


def monitor_positions():
    """
    Monitor all open positions.

    If target or stop loss is hit,
    automatically closes the trade.
    """

    messages = []

    positions = get_open_positions().copy()

    for position in positions:

        symbol = position["Symbol"]

        try:
            live_price = get_live_price(symbol)

        except Exception:
            continue

        # ----------------------------
        # Target Hit
        # ----------------------------

        if live_price >= position["Target"]:

            success, _ = close_paper_trade(symbol)

            if success:
                messages.append(
                    f"🎯 Target Hit : {symbol}"
                )

        # ----------------------------
        # Stop Loss Hit
        # ----------------------------

        elif live_price <= position["Stop"]:

            success, _ = close_paper_trade(symbol)

            if success:
                messages.append(
                    f"🛑 Stop Loss Hit : {symbol}"
                )

    return messages