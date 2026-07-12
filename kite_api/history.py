
from datetime import datetime, timedelta
from broker.zerodha import get_kite

kite = get_kite()

instrument = 738561      # RELIANCE instrument token

to_date = datetime.now()
from_date = to_date - timedelta(days=180)

data = kite.historical_data(
    instrument_token=instrument,
    from_date=from_date,
    to_date=to_date,
    interval="day"
)

print("Total candles:", len(data))

print()

print(data[-5:])