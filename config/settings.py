"""
Global Configuration
"""

# ======================================
# Capital
# ======================================

CAPITAL = 100000

RISK_PERCENT = 1

# ======================================
# Scanner
# ======================================

MIN_SCORE = 80

SCAN_INTERVAL = 60

MAX_OPEN_TRADES = 5

# ======================================
# Risk Management
# ======================================

USE_TRAILING_STOP = True

TRAILING_ATR = 1.5

# ======================================
# Trading
# ======================================

PAPER_TRADING = True

BROKER = "ZERODHA"

# ======================================
# Strategy
# ======================================

EMA_FAST = 20

EMA_SLOW = 50

RSI_PERIOD = 14

RSI_BUY = 55

RSI_SELL = 45