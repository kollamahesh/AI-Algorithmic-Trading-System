import yfinance as yf

from strategies.ema_rsi_strategy import generate_signals
from backtesting.backtester import run_backtest

# Download Data
df = yf.download(
    "RELIANCE.NS",
    start="2024-01-01",
    end="2025-01-01",
    auto_adjust=True
)

# Fix MultiIndex
if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
    df.columns = df.columns.get_level_values(0)

# Generate Signals
df = generate_signals(df)

# Run Backtest
profits = run_backtest(df)

total_profit = sum(profits)

print("\n===================")
print("BACKTEST RESULTS")
print("===================")

print("Total Trades :", len(profits))
print("Total Profit :", round(total_profit, 2))
print("Final Capital:", round(100000 + total_profit, 2))

from risk.risk_manager import calculate_position_size

quantity = calculate_position_size(
    capital=100000,
    risk_percent=1,
    entry_price=1500,
    stop_loss_price=1470
)

total_profit = sum(profits)

print("\n===================================")
print("BACKTEST RESULTS")
print("===================================")

print(f"Total Trades : {len(profits)}")
print(f"Total Profit : ₹{total_profit:.2f}")
print(f"Final Capital: ₹{100000 + total_profit:.2f}")