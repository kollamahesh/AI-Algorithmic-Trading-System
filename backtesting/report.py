"""
backtesting/report.py

Professional Backtest Report
"""

from analytics.drawdown import calculate_max_drawdown
from analytics.sharpe_ratio import calculate_sharpe_ratio
from analytics.performance import (
    calculate_average_win,
    calculate_average_loss,
    calculate_profit_factor
)


def print_report(results):

    profits = results["profits"]

    equity = results["equity_curve"]

    print("\n")
    print("=" * 65)
    print("AI BACKTEST REPORT")
    print("=" * 65)

    print(f"Initial Capital : ₹{equity[0]:,.2f}")
    print(f"Final Capital   : ₹{results['final_capital']:,.2f}")
    print(f"Net Profit      : ₹{results['total_profit']:,.2f}")

    if equity[0] != 0:
        returns = (results["total_profit"] / equity[0]) * 100
    else:
        returns = 0

    print(f"Return          : {returns:.2f}%")

    print("-" * 65)

    print(f"Total Trades    : {results['total_trades']}")
    print(f"Winning Trades  : {results['winning_trades']}")
    print(f"Losing Trades   : {results['losing_trades']}")
    print(f"Win Rate        : {results['win_rate']}%")

    print("-" * 65)

    print(f"Average Win     : ₹{calculate_average_win(profits):,.2f}")
    print(f"Average Loss    : ₹{calculate_average_loss(profits):,.2f}")
    print(f"Profit Factor   : {calculate_profit_factor(profits)}")
    print(f"Sharpe Ratio    : {calculate_sharpe_ratio(profits)}")
    print(f"Max Drawdown    : {calculate_max_drawdown(equity)}%")

    print("=" * 65)