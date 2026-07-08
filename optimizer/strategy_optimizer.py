"""
strategy_optimizer.py

Strategy Optimizer
"""

import itertools
import yfinance as yf
import config

from strategies.ema_rsi_strategy import generate_signals
from backtesting.backtester import run_backtest


def generate_parameter_combinations():
    """
    Generate EMA parameter combinations.
    """

    ema_fast = [10, 15, 20]
    ema_slow = [30, 50, 100]

    return list(
        itertools.product(
            ema_fast,
            ema_slow
        )
    )


def optimize():

    results_list = []

    combinations = generate_parameter_combinations()

    print("\nOPTIMIZATION STARTED")
    print("=" * 70)

    # Download data only ONCE
    df = yf.download(
        config.SYMBOL,
        start=config.START_DATE,
        end=config.END_DATE,
        auto_adjust=True,
        progress=False
    )

    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    for fast, slow in combinations:

        if fast >= slow:
            continue

        print(f"Testing EMA {fast}/{slow}")

        # Update configuration
        config.EMA_FAST = fast
        config.EMA_SLOW = slow

        # Copy dataframe so each test starts fresh
        test_df = df.copy()

        # Generate signals
        test_df = generate_signals(test_df)

        # Run silent backtest
        results = run_backtest(
            test_df,
            verbose=False
        )

        results_list.append(
            {
                "EMA_FAST": fast,
                "EMA_SLOW": slow,
                "TRADES": results["total_trades"],
                "WIN_RATE": results["win_rate"],
                "PROFIT": results["total_profit"],
                "FINAL_CAPITAL": results["final_capital"]
            }
        )

    return results_list


if __name__ == "__main__":

    results = optimize()

    results.sort(
        key=lambda x: x["PROFIT"],
        reverse=True
    )

    print("\n")
    print("=" * 90)
    print("OPTIMIZATION RESULTS")
    print("=" * 90)

    print(
        f"{'Rank':<5}"
        f"{'EMA':<12}"
        f"{'Trades':<10}"
        f"{'Win Rate':<12}"
        f"{'Profit':<18}"
        f"{'Capital'}"
    )

    print("-" * 90)

    for rank, r in enumerate(results, start=1):

        ema = f"{r['EMA_FAST']}/{r['EMA_SLOW']}"

        print(
            f"{rank:<5}"
            f"{ema:<12}"
            f"{r['TRADES']:<10}"
            f"{str(r['WIN_RATE']) + '%':<12}"
            f"₹{r['PROFIT']:<17.2f}"
            f"₹{r['FINAL_CAPITAL']:.2f}"
        )