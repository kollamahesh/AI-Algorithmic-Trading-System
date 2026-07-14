"""
trade_manager/manager.py

Professional Trade Manager
"""

from paper_trading.monitor import monitor_positions


class TradeManager:

    def __init__(self):

        pass

    # ==========================================
    # Monitor Open Trades
    # ==========================================

    def monitor(self):

        return monitor_positions()

    # ==========================================
    # Future Features
    # ==========================================

    def trailing_stop(self):

        pass

    def partial_exit(self):

        pass

    def time_exit(self):

        pass

    def market_close_exit(self):

        pass

    def risk_management(self):

        pass