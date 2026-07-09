import yfinance as yf
import config
from journal.trade_journal import get_trade_history
from strategies.ema_rsi_strategy import generate_signals
from backtesting.backtester import run_backtest

from analytics.performance import (
    calculate_win_rate,
    calculate_average_win,
    calculate_average_loss,
    calculate_profit_factor
)


def main():

    print("\n===================================")
    print("AI ALGORITHMIC TRADING BOT")
    print("===================================")

    print(f"Symbol       : {config.SYMBOL}")
    print(f"Date Range   : {config.START_DATE} to {config.END_DATE}")
    print(f"EMA          : {config.EMA_FAST}/{config.EMA_SLOW}")
    print(f"RSI Period   : {config.RSI_PERIOD}")
    print(f"RSI Buy      : {config.RSI_BUY}")
    print(f"RSI Sell     : {config.RSI_SELL}")
    print(f"Stop Loss    : {config.STOP_LOSS_PERCENT}%")
    print(f"Target       : {config.TARGET_PERCENT}%")
    print(f"Slippage     : {config.SLIPPAGE_PERCENT}%")
    print(f"Brokerage    : {config.BROKERAGE_PERCENT}%")
    print(f"Capital      : ₹{config.INITIAL_CAPITAL}")

    print("===================================\n")

    # =====================================
    # Download Market Data
    # =====================================

    df = yf.download(
        config.SYMBOL,
        start=config.START_DATE,
        end=config.END_DATE,
        auto_adjust=True
    )

    # Fix MultiIndex Columns
    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    # =====================================
    # Generate Signals
    # =====================================

    df = generate_signals(df)

    # =====================================
    # Run Backtest
    # =====================================

    results = run_backtest(
        df,
        verbose=True
    )

    # =====================================
    # Backtest Results
    # =====================================

    print("\n===================================")
    print("BACKTEST RESULTS")
    print("===================================")

    print(f"Total Trades    : {results['total_trades']}")
    print(f"Winning Trades  : {results['winning_trades']}")
    print(f"Losing Trades   : {results['losing_trades']}")
    print(f"Win Rate        : {results['win_rate']}%")
    print(f"Total Profit    : ₹{results['total_profit']:.2f}")
    print(f"Final Capital   : ₹{results['final_capital']:.2f}")

    # =====================================
    # Performance Analytics
    # =====================================

    profits = results["profits"]

    print("\n===================================")
    print("PERFORMANCE METRICS")
    print("===================================")

    print(f"Win Rate        : {calculate_win_rate(profits)}%")
    print(f"Average Win     : ₹{calculate_average_win(profits):.2f}")
    print(f"Average Loss    : ₹{calculate_average_loss(profits):.2f}")
    print(f"Profit Factor   : {calculate_profit_factor(profits)}")

    print("===================================")


if __name__ == "__main__":
    main()
    
# =====================================
# Trade Journal
# =====================================

history = get_trade_history()

print("\n===================================")
print("TRADE JOURNAL")
print("===================================")

if len(history) == 0:

    print("No trades recorded.")

else:

    for i, trade in enumerate(history, start=1):

        print(f"\nTrade {i}")
        print("-" * 25)

        print(f"Entry Price : ₹{trade['Entry Price']}")
        print(f"Exit Price  : ₹{trade['Exit Price']}")
        print(f"Quantity    : {trade['Quantity']}")
        print(f"Exit Reason : {trade['Exit Reason']}")
        print(f"Profit      : ₹{trade['Profit']}")

print("===================================")