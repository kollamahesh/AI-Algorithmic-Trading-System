from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

kite = KiteConnect(api_key=os.getenv("KITE_API_KEY"))
kite.set_access_token(os.getenv("KITE_ACCESS_TOKEN"))

CSV_FILE = "data/instruments.csv"


def download_instruments():

    instruments = kite.instruments("NSE")

    df = pd.DataFrame(instruments)

    df.to_csv(CSV_FILE, index=False)

    return df


def load_instruments():

    if not os.path.exists(CSV_FILE):

        download_instruments()

    return pd.read_csv(CSV_FILE)


def get_token(symbol):

    df = load_instruments()

    symbol = symbol.replace(".NS", "")

    row = df[df["tradingsymbol"] == symbol]

    if row.empty:

        return None

    return int(row.iloc[0]["instrument_token"])


if __name__ == "__main__":

    print()

    print("RELIANCE")

    print(get_token("RELIANCE.NS"))

    print()

    print("ICICIBANK")

    print(get_token("ICICIBANK.NS"))

    print()

    print("TCS")

    print(get_token("TCS.NS"))