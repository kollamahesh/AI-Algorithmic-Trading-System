"""
broker/zerodha.py

Single Zerodha Connection
"""

from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("KITE_API_KEY")
ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

if not API_KEY:
    raise ValueError("KITE_API_KEY not found")

if not ACCESS_TOKEN:
    raise ValueError("KITE_ACCESS_TOKEN not found")

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)


def get_kite():
    return kite


def get_ltp(symbol):
    """
    Returns latest market price.
    """

    quote = kite.ltp(f"NSE:{symbol.replace('.NS','')}")

    return quote[f"NSE:{symbol.replace('.NS','')}"]["last_price"]