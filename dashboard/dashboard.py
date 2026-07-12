"""
dashboard/dashboard.py

Main Portfolio Dashboard
"""
from dashboard.pnl import print_pnl
from dashboard.summary import print_summary
from dashboard.positions import print_positions


def show_dashboard():

    print("\n" * 2)

    print("=" * 90)
    print("AI TRADING PORTFOLIO DASHBOARD")
    print("=" * 90)

    print_summary()

    print_positions()
    
    print_pnl()

    print("\n")