from kiteconnect import KiteTicker
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("KITE_API_KEY")
ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

kws = KiteTicker(API_KEY, ACCESS_TOKEN)


def on_ticks(ws, ticks):

    print()

    print("=" * 60)
    print("LIVE TICKS")
    print("=" * 60)

    for tick in ticks:

        print(
            f"Token: {tick['instrument_token']} | "
            f"Price: ₹{tick['last_price']} | "
            f"Time: {tick['exchange_timestamp']}"
        )


def on_connect(ws, response):

    print("Connected Successfully!")

    ws.subscribe([
        738561,      # RELIANCE
        1270529      # ICICIBANK
    ])

    ws.set_mode(
        ws.MODE_FULL,
        [
            738561,
            1270529
        ]
    )


def on_close(ws, code, reason):

    print("Connection Closed")


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()