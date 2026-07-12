"""
dashboard/summary.py
"""

from paper_trading.portfolio import (
    get_capital,
    get_total_investment,
    get_total_positions
)


def print_summary():

    print("=" * 60)
    print("PORTFOLIO SUMMARY")
    print("=" * 60)

    print(f"Available Capital : ₹{get_capital():,.2f}")

    print(f"Invested Amount   : ₹{get_total_investment():,.2f}")

    print(f"Open Positions    : {get_total_positions()}")

    print("=" * 60)