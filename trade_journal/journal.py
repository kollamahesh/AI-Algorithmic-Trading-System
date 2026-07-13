"""
trade_journal/journal.py

Professional Trade Journal
"""

import os
import pandas as pd

FILE_NAME = "trade_journal/trade_history.csv"


def save_trade(trade):

    os.makedirs(
        "trade_journal",
        exist_ok=True
    )

    df = pd.DataFrame([trade])

    if os.path.exists(FILE_NAME):

        df.to_csv(
            FILE_NAME,
            mode="a",
            header=False,
            index=False
        )

    else:

        df.to_csv(
            FILE_NAME,
            index=False
        )


def load_trades():

    if not os.path.exists(FILE_NAME):

        return pd.DataFrame()

    return pd.read_csv(FILE_NAME)