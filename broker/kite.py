"""
broker/kite.py

Live Trading Broker
"""

from kite_api.client import kite


class KiteBroker:

    # ==========================================
    # BUY
    # ==========================================

    def buy(self, trade):

        try:

            order_id = kite.place_order(

                variety="regular",

                exchange="NSE",

                tradingsymbol=trade["Symbol"].replace(".NS", ""),

                transaction_type="BUY",

                quantity=trade["Quantity"],

                order_type="MARKET",

                product="CNC",

                validity="DAY"

            )

            return True, f"BUY Order Placed\nOrder ID : {order_id}"

        except Exception as e:

            return False, str(e)

    # ==========================================
    # SELL
    # ==========================================

    def sell(self, symbol, quantity):

        try:

            order_id = kite.place_order(

                variety="regular",

                exchange="NSE",

                tradingsymbol=symbol.replace(".NS", ""),

                transaction_type="SELL",

                quantity=quantity,

                order_type="MARKET",

                product="CNC",

                validity="DAY"

            )

            return True, f"SELL Order Placed\nOrder ID : {order_id}"

        except Exception as e:

            return False, str(e)