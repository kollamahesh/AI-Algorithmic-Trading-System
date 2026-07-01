import pandas as pd
from ta.momentum import RSIIndicator


def generate_signals(df):

    df["EMA20"] = df["Close"].ewm(
        span=20,
        adjust=False
    ).mean()

    df["EMA50"] = df["Close"].ewm(
        span=50,
        adjust=False
    ).mean()

    df["RSI"] = RSIIndicator(
        close=df["Close"],
        window=14
    ).rsi()

    df["Signal"] = 0

    df.loc[
        (df["EMA20"] > df["EMA50"]) &
        (df["RSI"] > 50),
        "Signal"
    ] = 1

    df.loc[
        (df["EMA20"] < df["EMA50"]) &
        (df["RSI"] < 50),
        "Signal"
    ] = -1

    return df