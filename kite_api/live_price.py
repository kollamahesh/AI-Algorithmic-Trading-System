from kite_api.client import kite


def get_live_price(symbol):
    """
    Returns latest live market price.
    """

    # Convert RELIANCE.NS -> NSE:RELIANCE
    kite_symbol = "NSE:" + symbol.replace(".NS", "")

    data = kite.ltp([kite_symbol])

    return data[kite_symbol]["last_price"]