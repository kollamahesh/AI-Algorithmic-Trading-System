"""
Global Configuration
"""

# ======================================
# Capital
# ======================================

CAPITAL = 100000

# Backward compatibility
INITIAL_CAPITAL = CAPITAL

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

STOP_LOSS_PERCENT = 2.0

TARGET_PERCENT = 4.0

# ======================================
# Trading Costs
# ======================================

SLIPPAGE_PERCENT = 0.10

BROKERAGE_PERCENT = 0.03

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