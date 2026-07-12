import yfinance as yf

from paper_trading.portfolio import open_positions
from paper_trading.monitor import check_position


def start_monitor():

    print("\n")
    print("=" * 60)
    print("LIVE POSITION MONITOR")
    print("=" * 60)

    if len(open_positions) == 0:

        print("No open positions.")

        return

    print("\nChecking Market...\n")

    for position in open_positions[:]:

        symbol = position["Symbol"]

        try:

            df = yf.download(
                symbol,
                period="1d",
                interval="1m",
                progress=False,
                auto_adjust=True
            )

            if len(df) == 0:
                continue

            close = df["Close"].iloc[-1]

            if hasattr(close, "iloc"):
                price = float(close.iloc[0])
            else:
                price = float(close)

            print(
                f"{symbol:<18}"
                f"Current Price : ₹{price:.2f}"
            )

            check_position(
                symbol,
                price
            )

        except Exception as e:

            print(f"{symbol}: {e}")

    print("\nMonitor cycle complete.\n")