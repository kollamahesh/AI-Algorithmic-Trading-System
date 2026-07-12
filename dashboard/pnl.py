"""
dashboard/pnl.py

Live Profit & Loss Dashboard
"""

from broker.zerodha import get_ltp
from paper_trading.portfolio import get_open_positions


def print_pnl():

    positions = get_open_positions()

    print("\n")
    print("=" * 95)
    print("LIVE PROFIT & LOSS")
    print("=" * 95)

    if not positions:

        print("No Open Positions")

        return

    print(
        f"{'Symbol':<18}"
        f"{'Entry':>12}"
        f"{'Current':>12}"
        f"{'Qty':>8}"
        f"{'P/L':>15}"
    )

    print("-" * 95)

    total_pnl = 0

    for position in positions:

        try:

            current = get_ltp(position["Symbol"])

            entry = position["Entry"]

            qty = position["Quantity"]

            pnl = (current - entry) * qty

            total_pnl += pnl

            print(
                f"{position['Symbol']:<18}"
                f"{entry:>12.2f}"
                f"{current:>12.2f}"
                f"{qty:>8}"
                f"{pnl:>15.2f}"
            )

        except Exception:

            print(
                f"{position['Symbol']:<18}"
                f"{'ERROR':>45}"
            )

    print("-" * 95)

    print(f"{'TOTAL LIVE P/L':<50} ₹{total_pnl:,.2f}")

    print("=" * 95)