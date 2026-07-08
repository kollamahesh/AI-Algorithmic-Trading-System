import yfinance as yf
import config

from strategies.ema_rsi_strategy import generate_signals
from backtesting.backtester import run_backtest


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
    # Generate Trading Signals
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
    # Final Results
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

    print("===================================")


if __name__ == "__main__":
    main()