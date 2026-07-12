"""
config.py

Central configuration for the trading bot.
"""

# ==========================
# Strategy Parameters
# ==========================

EMA_FAST = 20
EMA_SLOW = 50

RSI_PERIOD = 14

RSI_BUY = 55
RSI_SELL = 45

# ==========================
# Risk Management
# ==========================

RISK_PERCENT = 1

STOP_LOSS_PERCENT = 2

TARGET_PERCENT = 4

# ==========================
# Execution
# ==========================

SLIPPAGE_PERCENT = 0.05

# ==========================
# Trading Costs
# ==========================

BROKERAGE_PERCENT = 0.1

# ==========================
# Capital
# ==========================

INITIAL_CAPITAL = 100000

# ==========================
# Market
# ==========================

SYMBOL = "RELIANCE.NS"

START_DATE = "2024-01-01"

END_DATE = "2025-01-01"