"""
broker/paper.py
"""

from paper_trading.execution import (
    execute_paper_trade,
    close_paper_trade
)


class PaperBroker:

    def buy(self, trade):

        return execute_paper_trade(trade)

    def sell(self, symbol):

        return close_paper_trade(symbol)