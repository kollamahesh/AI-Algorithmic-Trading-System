import yfinance as yf

import config
from analytics.monthly_returns import calculate_monthly_returns
from analytics.sharpe_ratio import calculate_sharpe_ratio
from strategies.ema_rsi_strategy import generate_signals
from analytics.drawdown import calculate_max_drawdown
from backtesting.backtester import run_backtest
from analytics.charts import plot_equity_curve
from analytics.performance import (
    calculate_average_win,
    calculate_average_loss,
    calculate_profit_factor
)

from analytics.equity_curve import build_equity_curve

from journal.trade_journal import (
    get_trade_history,
    save_trade_history
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

    # ----------------------------------
    # Download Market Data
    # ----------------------------------

    df = yf.download(
        config.SYMBOL,
        start=config.START_DATE,
        end=config.END_DATE,
        auto_adjust=True
    )

    # ----------------------------------
    # Generate Trading Signals
    # ----------------------------------

    df = generate_signals(df)

    # ----------------------------------
    # Run Backtest
    # ----------------------------------

    results = run_backtest(df)

    profits = results["profits"]

    equity = build_equity_curve(profits)
    max_drawdown = calculate_max_drawdown(equity)
    sharpe = calculate_sharpe_ratio(profits)
    
    plot_equity_curve(equity)

    # ----------------------------------
    # Backtest Results
    # ----------------------------------

    print("\n===================================")
    print("BACKTEST RESULTS")
    print("===================================")

    print(f"Total Trades    : {results['total_trades']}")
    print(f"Winning Trades  : {results['winning_trades']}")
    print(f"Losing Trades   : {results['losing_trades']}")
    print(f"Win Rate        : {results['win_rate']}%")
    print(f"Total Profit    : ₹{results['total_profit']:.2f}")
    print(f"Final Capital   : ₹{results['final_capital']:.2f}")

    # ----------------------------------
    # Performance Metrics
    # ----------------------------------

    print("\n===================================")
    print("PERFORMANCE METRICS")
    print("===================================")

    print(f"Win Rate        : {results['win_rate']}%")

    print(
        f"Average Win     : ₹{calculate_average_win(profits):.2f}"
    )

    print(
        f"Average Loss    : ₹{calculate_average_loss(profits):.2f}"
    )

    print(
        f"Profit Factor   : {calculate_profit_factor(profits):.2f}"
    )   
    print(f"Max Drawdown  : {max_drawdown:.2f}%")
    print(f"Sharpe Ratio    : {sharpe}")
    

    print("===================================")
    
    # ----------------------------------
    # Trade Journal
    # ----------------------------------

    history = get_trade_history()
    monthly_returns = calculate_monthly_returns(history)

    print("\n===================================")
    print("TRADE JOURNAL")
    print("===================================")

    if len(history) == 0:

        print("No trades recorded.")

    else:

        for i, trade in enumerate(history, start=1):

            print(f"\nTrade {i}")
            print("-" * 30)

            print(f"Date         : {trade['Date']}")
            print(f"Symbol       : {trade['Symbol']}")
            print(f"Entry Price  : ₹{trade['Entry Price']}")
            print(f"Exit Price   : ₹{trade['Exit Price']}")
            print(f"Quantity     : {trade['Quantity']}")
            print(f"Stop Loss    : ₹{trade['Stop Loss']}")
            print(f"Target       : ₹{trade['Target']}")
            print(f"Gross Profit : ₹{trade['Gross Profit']}")
            print(f"Brokerage    : ₹{trade['Brokerage']}")
            print(f"Net Profit   : ₹{trade['Net Profit']}")
            print(f"Exit Reason  : {trade['Exit Reason']}")

    print("===================================")

    # ----------------------------------
    # Save Trade History
    # ----------------------------------

    save_trade_history()
    
    # ----------------------------------
    # Equity Curve
    # ----------------------------------

    print("\n===================================")
    print("EQUITY CURVE")
    print("===================================")

    for i, value in enumerate(equity):

        print(f"Trade {i:<2} : ₹{value:.2f}")

    print("===================================")
    
    print("\n===================================")
    print("MONTHLY RETURNS")
    print("===================================")

    for month, profit in monthly_returns.items():
        print(f"{month} : ₹{profit:.2f}")

    print("===================================")


if __name__ == "__main__":
    main()