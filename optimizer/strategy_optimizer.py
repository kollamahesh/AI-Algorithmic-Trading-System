"""
optimizer/strategy_optimizer.py

Tests multiple EMA strategies and ranks them.
"""

import itertools
from results.export_results import export_results
from scanner.scanner import scan_stock
from strategies.ema_rsi_strategy import generate_signals
from backtesting.backtester import run_backtest


# ==========================================================
# PARAMETER COMBINATIONS
# ==========================================================

def generate_parameter_combinations():
    """
    Generate EMA combinations.
    """

    ema_fast = [10, 15, 20]
    ema_slow = [30, 50, 100]

    combinations = []

    for fast, slow in itertools.product(ema_fast, ema_slow):

        if fast < slow:

            combinations.append((fast, slow))

    return combinations


# ==========================================================
# OPTIMIZER
# ==========================================================

def optimize(symbol="RELIANCE.NS"):

    combinations = generate_parameter_combinations()

    optimization_results = []

    print("\n")
    print("=" * 70)
    print("EMA STRATEGY OPTIMIZER")
    print("=" * 70)
# ----------------------------------------
# Download historical data ONCE
# ----------------------------------------

    df_original = scan_stock(symbol)
    
    for fast, slow in combinations:

        print(f"\nTesting EMA {fast}/{slow}")

        try:

            # ----------------------------------------
            # Copy original dataframe
            # ----------------------------------------

            df = df_original.copy()

            # ----------------------------------------
            # Generate Signals
            # ----------------------------------------

            df = generate_signals(

                df,

                ema_fast=fast,

                ema_slow=slow

            )

            # ----------------------------------------
            # Backtest
            # ----------------------------------------

            results = run_backtest(

                df,

                verbose=False

            )

            optimization_results.append(

                {

                    "EMA_FAST": fast,

                    "EMA_SLOW": slow,

                    "Trades": results["total_trades"],

                    "Win Rate": results["win_rate"],

                    "Profit": round(results["total_profit"], 2),

                    "Capital": round(results["final_capital"], 2)

                }

            )

        except Exception as e:

            print(f"ERROR : {e}")

    # ----------------------------------------
    # Sort
    # ----------------------------------------

    optimization_results.sort(

        key=lambda x: x["Profit"],

        reverse=True

    )

    return optimization_results


# ==========================================================
# PRINT RESULTS
# ==========================================================

def print_results(results):

    print("\n")
    print("=" * 90)
    print("TOP EMA STRATEGIES")
    print("=" * 90)

    print(

        f"{'Rank':<6}"

        f"{'EMA':<12}"

        f"{'Trades':<10}"

        f"{'Win %':<10}"

        f"{'Profit':<15}"

        f"{'Capital'}"

    )

    print("-" * 90)

    for rank, result in enumerate(results, start=1):

        print(

            f"{rank:<6}"

            f"{str(result['EMA_FAST']) + '/' + str(result['EMA_SLOW']):<12}"

            f"{result['Trades']:<10}"

            f"{result['Win Rate']:<10}"

            f"₹{result['Profit']:<14,.2f}"

            f"₹{result['Capital']:,.2f}"

        )

from scanner.watchlist import load_watchlist


def optimize_all_stocks():

    symbols = load_watchlist()

    overall_results = []

    print("\n")
    print("=" * 80)
    print("MULTI STOCK OPTIMIZER")
    print("=" * 80)

    for symbol in symbols:

        print(f"\nOptimizing {symbol}...")

        results = optimize(symbol)

        if len(results) > 0:

            best = results[0]

            best["Symbol"] = symbol

            overall_results.append(best)

    overall_results.sort(

        key=lambda x: x["Profit"],

        reverse=True

    )

    return overall_results
# ==========================================================
# START
# ==========================================================

if __name__ == "__main__":

    results = optimize_all_stocks()
    
    print_results(results)

    export_results(results)

    print("\n")
    print("=" * 100)
    print("BEST STRATEGY FOR EACH STOCK")
    print("=" * 100)

    print(

        f"{'Rank':<6}"

        f"{'Stock':<18}"

        f"{'EMA':<12}"

        f"{'Profit':<15}"

        f"{'Capital'}"

    )

    print("-" * 100)

    for rank, result in enumerate(results, start=1):

        print(

            f"{rank:<6}"

            f"{result['Symbol']:<18}"

            f"{str(result['EMA_FAST'])+'/'+str(result['EMA_SLOW']):<12}"

            f"₹{result['Profit']:<14,.2f}"

            f"₹{result['Capital']:,.2f}"

        )