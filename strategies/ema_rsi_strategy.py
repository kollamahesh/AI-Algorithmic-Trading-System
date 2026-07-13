"""
EMA + RSI Strategy
"""

import pandas as pd
from ta.momentum import RSIIndicator

from config.settings import (
    EMA_FAST,
    EMA_SLOW,
    RSI_PERIOD,
    RSI_BUY,
    RSI_SELL,
)


def generate_signals(
    df,
    ema_fast=EMA_FAST,
    ema_slow=EMA_SLOW,
    rsi_buy=RSI_BUY,
    rsi_sell=RSI_SELL
):

    # ----------------------------------
    # Fix MultiIndex columns
    # ----------------------------------

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    close = df["Close"]

    # If Close is still a DataFrame, convert to Series
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    # ----------------------------------
    # EMA
    # ----------------------------------

    df["EMA_FAST"] = close.ewm(
        span=ema_fast,
        adjust=False
    ).mean()

    df["EMA_SLOW"] = close.ewm(
        span=ema_slow,
        adjust=False
    ).mean()

    # ----------------------------------
    # RSI
    # ----------------------------------

    df["RSI"] = RSIIndicator(
        close=close,
        window=RSI_PERIOD
    ).rsi()

    # ----------------------------------
    # Signals
    # ----------------------------------

    df["Signal"] = 0

    df["Prev_EMA_FAST"] = df["EMA_FAST"].shift(1)
    df["Prev_EMA_SLOW"] = df["EMA_SLOW"].shift(1)

    buy_condition = (
        (df["Prev_EMA_FAST"] <= df["Prev_EMA_SLOW"])
        & (df["EMA_FAST"] > df["EMA_SLOW"])
        & (df["RSI"] > rsi_buy)
    )

    sell_condition = (
        (df["Prev_EMA_FAST"] >= df["Prev_EMA_SLOW"])
        & (df["EMA_FAST"] < df["EMA_SLOW"])
        & (df["RSI"] < rsi_sell)
    )

    df.loc[buy_condition, "Signal"] = 1
    df.loc[sell_condition, "Signal"] = -1

    return df