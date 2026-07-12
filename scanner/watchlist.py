import pandas as pd


def load_watchlist():

    df = pd.read_csv("data/nifty50.csv")

    return df["Symbol"].tolist()