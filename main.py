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

print("\n===================================")
print("BACKTEST RESULTS")
print("===================================")
print(f"Total Trades : {len(profits)}")
print(f"Total Profit : ₹{total_profit:.2f}")
print(f"Final Capital: ₹{100000 + total_profit:.2f}")

