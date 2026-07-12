"""
scanner.py

Scans NIFTY 50 stocks and selects the best trading opportunities.
"""

from kite_api.data_provider import get_historical_data
from strategies.ema_rsi_strategy import generate_signals
from scanner.watchlist import load_watchlist
from scanner.selector import select_best_stock

from analytics.signal_score import calculate_signal_score
from analytics.atr import add_atr

from risk.atr_trade import atr_trade_levels
from risk.position_size import calculate_position_size

from config.settings import *


def scan_market():

    symbols = load_watchlist()

    results = []

    print("\nScanning NIFTY 50...")
    print("-" * 60)

    for symbol in symbols:

        try:

            # ----------------------------------------
            # Historical Data
            # ----------------------------------------

            df = get_historical_data(symbol)

            if len(df) < 60:
                continue

            # ----------------------------------------
            # Indicators
            # ----------------------------------------

            df = generate_signals(df)

            df = add_atr(df)

            last = df.iloc[-1]

            close = float(last["Close"])
            ema_fast = float(last["EMA_FAST"])
            ema_slow = float(last["EMA_SLOW"])
            rsi = float(last["RSI"])
            atr = float(last["ATR"])
            signal = int(last["Signal"])

            # ----------------------------------------
            # Trend
            # ----------------------------------------

            trend = "Bullish" if ema_fast > ema_slow else "Bearish"

            # ----------------------------------------
            # Action
            # ----------------------------------------

            if signal == 1:
                action = "BUY"

            elif signal == -1:
                action = "SELL"

            elif trend == "Bullish":
                action = "HOLD"

            else:
                action = "WAIT"

            # ----------------------------------------
            # Score
            # ----------------------------------------

            score = calculate_signal_score(

                close,
                ema_fast,
                ema_slow,
                rsi

            )

            # ----------------------------------------
            # ATR Trade Plan
            # ----------------------------------------

            trade = atr_trade_levels(

                close,
                atr

            )

            # ----------------------------------------
            # Position Size
            # ----------------------------------------

            position = calculate_position_size(

                capital=CAPITAL,

                risk_percent=RISK_PERCENT,

                entry=trade["Entry"],

                stop=trade["Stop"]

            )

            # ----------------------------------------
            # Store Result
            # ----------------------------------------

            results.append({

                "Symbol": symbol,

                "Close": close,

                "EMA20": ema_fast,

                "EMA50": ema_slow,

                "RSI": rsi,

                "ATR": atr,

                "Trend": trend,

                "Signal": action,

                "Score": score,

                "Entry": trade["Entry"],

                "Stop": trade["Stop"],

                "Target": trade["Target"],

                "Risk": trade["Risk"],

                "Reward": trade["Reward"],

                "RR": trade["RR"],

                "Quantity": position["Quantity"],

                "Investment": position["Investment"],

                "Risk Amount": position["Risk Amount"]

            })

        except Exception as e:

            print(f"\nERROR in {symbol}")

            print(e)

            continue

    # ----------------------------------------
    # Sort Results
    # ----------------------------------------

    results = sorted(

        results,

        key=lambda x: x["Score"],

        reverse=True

    )

    # ----------------------------------------
    # Top Trading Opportunities
    # ----------------------------------------

    print("\n")

    print("=" * 150)

    print("TOP TRADING OPPORTUNITIES")

    print("=" * 150)

    print(

        f"{'Rank':<6}"

        f"{'Symbol':<18}"

        f"{'Qty':>6}"

        f"{'Entry':>12}"

        f"{'Stop':>12}"

        f"{'Target':>12}"

        f"{'Invest':>14}"

        f"{'Risk':>10}"

        f"{'Score':>8}"

    )

    print("-" * 150)

    for i, stock in enumerate(results[:10], start=1):

        print(

            f"{i:<6}"

            f"{stock['Symbol']:<18}"

            f"{stock['Quantity']:>6}"

            f"{stock['Entry']:>12.2f}"

            f"{stock['Stop']:>12.2f}"

            f"{stock['Target']:>12.2f}"

            f"{stock['Investment']:>14.2f}"

            f"{stock['Risk Amount']:>10.2f}"

            f"{stock['Score']:>8.1f}"

        )

    print("=" * 150)

    # ----------------------------------------
    # Sell / Wait Candidates
    # ----------------------------------------

    print("\nSELL / WAIT CANDIDATES")

    print("-" * 60)

    sell_list = [

        x for x in results

        if x["Signal"] in ["SELL", "WAIT"]

    ]

    if not sell_list:

        print("No Sell Candidates")

    else:

        for stock in sell_list[:10]:

            print(

                f"{stock['Symbol']:<18}"

                f"Qty {stock['Quantity']:<4}"

                f"Entry ₹{stock['Entry']:<10.2f}"

                f"Stop ₹{stock['Stop']:<10.2f}"

                f"Risk ₹{stock['Risk Amount']:<8.2f}"

                f"Score {stock['Score']:>6.1f}"

            )

    print("\nScan Complete.")

    # ----------------------------------------
    # Best Trade
    # ----------------------------------------

    best_stock = select_best_stock(results)

    if best_stock:

        print("\n")

        print("=" * 60)

        print("BEST TRADE")

        print("=" * 60)

        print(f"Symbol     : {best_stock['Symbol']}")

        print(f"Score      : {best_stock['Score']}")

        print(f"Entry      : ₹{best_stock['Entry']:.2f}")

        print(f"Stop       : ₹{best_stock['Stop']:.2f}")

        print(f"Target     : ₹{best_stock['Target']:.2f}")

        print(f"Quantity   : {best_stock['Quantity']}")

        print(f"Investment : ₹{best_stock['Investment']:.2f}")

        print("=" * 60)

    return results, best_stock


if __name__ == "__main__":

    scan_market()