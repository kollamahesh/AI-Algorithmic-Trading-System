"""
Trading Engine

Main AI Trading Engine
"""

import time

from scanner.scanner import scan_market
from paper_trading.trader import buy_stock
from paper_trading.live_monitor import start_monitor

from config.settings import SCAN_INTERVAL


def run_engine():

    print("\n")
    print("=" * 70)
    print("AI TRADING ENGINE STARTED")
    print("=" * 70)

    while True:

        print("\nScanning Market...\n")

        results, best_stock = scan_market()

        trade_placed = False

        # ==========================================
        # Try every ranked stock until one is bought
        # ==========================================

        for stock in results:

            print(f"\nChecking {stock['Symbol']}...")

            success = buy_stock(

                symbol=stock["Symbol"],

                entry=stock["Entry"],

                stop=stock["Stop"],

                target=stock["Target"],

                quantity=stock["Quantity"]

            )

            if success:

                print(f"\nTrade Executed -> {stock['Symbol']}")

                trade_placed = True

                break

        if not trade_placed:

            print("\nNo eligible trade found.")

        # ==========================================
        # Monitor Existing Positions
        # ==========================================

        start_monitor()

        print(f"\nSleeping {SCAN_INTERVAL} seconds...\n")

        time.sleep(SCAN_INTERVAL)


# ==========================================
# START ENGINE
# ==========================================

if __name__ == "__main__":

    run_engine()