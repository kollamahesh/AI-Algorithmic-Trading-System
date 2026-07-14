from kite_api.client import kite


def get_live_price(symbol):

    # Convert Yahoo format -> Kite format

    if symbol.endswith(".NS"):

        kite_symbol = "NSE:" + symbol.replace(".NS", "")

    else:

        kite_symbol = symbol

    data = kite.ltp([kite_symbol])

    return data[kite_symbol]["last_price"]