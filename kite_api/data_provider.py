from broker.zerodha import get_kite
from datetime import datetime, timedelta
from kite_api.instruments import get_token
import pandas as pd


kite = get_kite()


def get_historical_data(symbol, days=180):

    token = get_token(symbol)

    if token is None:
        raise Exception(f"Token not found for {symbol}")

    to_date = datetime.now()
    from_date = to_date - timedelta(days=days)

    data = kite.historical_data(
        instrument_token=token,
        from_date=from_date,
        to_date=to_date,
        interval="day"
    )

    df = pd.DataFrame(data)

    df.rename(
        columns={
            "date": "Date",
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "volume": "Volume"
        },
        inplace=True
    )

    return df


if __name__ == "__main__":

    df = get_historical_data("RELIANCE.NS")

    print(df.tail())