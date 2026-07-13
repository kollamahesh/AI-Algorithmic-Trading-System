from scanner.scanner import scan_stock
from backtesting.backtester import run_backtest

symbol = "RELIANCE.NS"

print("=" * 60)
print(f"Running Backtest : {symbol}")
print("=" * 60)

df = scan_stock(symbol)

results = run_backtest(df)

print("\nReturned Results:")
print(results)