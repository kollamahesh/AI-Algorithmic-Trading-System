from broker.zerodha import get_kite

kite = get_kite()

symbols = [
    "NSE:RELIANCE",
    "NSE:ICICIBANK",
    "NSE:TCS",
    "NSE:INFY"
]

quotes = kite.quote(symbols)

print("=" * 70)
print("LIVE MARKET DATA")
print("=" * 70)

for symbol in symbols:

    q = quotes[symbol]

    print()
    print(symbol)
    print(f"Last Price : ₹{q['last_price']}")
    print(f"Open       : ₹{q['ohlc']['open']}")
    print(f"High       : ₹{q['ohlc']['high']}")
    print(f"Low        : ₹{q['ohlc']['low']}")
    print(f"Close      : ₹{q['ohlc']['close']}")
    print(f"Volume     : {q['volume']:,}")