"""
dashboard/positions.py

Shows all open positions.
"""

from paper_trading.portfolio import get_open_positions


def print_positions():

    positions = get_open_positions()

    print("\n")
    print("=" * 90)
    print("OPEN POSITIONS")
    print("=" * 90)

    if not positions:

        print("No Open Positions")

        return

    print(
        f"{'Symbol':<18}"
        f"{'Qty':>6}"
        f"{'Entry':>12}"
        f"{'Target':>12}"
        f"{'Stop':>12}"
        f"{'Investment':>15}"
    )

    print("-" * 90)

    for position in positions:

        print(
            f"{position['Symbol']:<18}"
            f"{position['Quantity']:>6}"
            f"{position['Entry']:>12.2f}"
            f"{position['Target']:>12.2f}"
            f"{position['Stop']:>12.2f}"
            f"{position['Investment']:>15.2f}"
        )

    print("=" * 90)