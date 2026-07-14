"""
broker/broker.py

Broker Manager
"""

from config.settings import PAPER_TRADING

from broker.paper import PaperBroker
from broker.kite import KiteBroker


class Broker:

    def __init__(self):

        if PAPER_TRADING:
            self.engine = PaperBroker()
        else:
            self.engine = KiteBroker()

    # ==========================================
    # BUY
    # ==========================================

    def buy(self, trade):

        return self.engine.buy(trade)

    # ==========================================
    # SELL
    # ==========================================

    def sell(self, symbol, quantity=None):

        if quantity is None:
            return self.engine.sell(symbol)

        return self.engine.sell(symbol, quantity)