import pandas as pd
from ta.momentum import RSIIndicator

import config


def generate_signals(df):

    # EMA
    df["EMA_FAST"] = df["Close"].ewm(
        span=config.EMA_FAST,
        adjust=False
    ).mean()

    df["EMA_SLOW"] = df["Close"].ewm(
        span=config.EMA_SLOW,
        adjust=False
    ).mean()

    # RSI
    df["RSI"] = RSIIndicator(
        close=df["Close"],
        window=config.RSI_PERIOD
    ).rsi()

    df["Signal"] = 0

    # Previous values
    df["Prev_EMA_FAST"] = df["EMA_FAST"].shift(1)
    df["Prev_EMA_SLOW"] = df["EMA_SLOW"].shift(1)

    # BUY
    buy_condition = (
        (df["Prev_EMA_FAST"] <= df["Prev_EMA_SLOW"]) &
        (df["EMA_FAST"] > df["EMA_SLOW"]) &
        (df["RSI"] > config.RSI_BUY)
    )

    # SELL
    sell_condition = (
        (df["Prev_EMA_FAST"] >= df["Prev_EMA_SLOW"]) &
        (df["EMA_FAST"] < df["EMA_SLOW"]) &
        (df["RSI"] < config.RSI_SELL)
    )

    df.loc[buy_condition, "Signal"] = 1
    df.loc[sell_condition, "Signal"] = -1

    return df