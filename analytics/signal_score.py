"""
signal_score.py

Calculates a signal strength score (0–100).
"""


def calculate_signal_score(close, ema_fast, ema_slow, rsi):

    score = 0

    # ==========================
    # Trend (30 points)
    # ==========================

    if ema_fast > ema_slow:
        score += 30

    # ==========================
    # RSI (25 points)
    # ==========================

    if 55 <= rsi <= 70:
        score += 25

    elif 50 <= rsi < 55:
        score += 15

    elif 45 <= rsi < 50:
        score += 10

    # ==========================
    # EMA Separation (20 points)
    # ==========================

    separation = abs(ema_fast - ema_slow) / ema_slow * 100

    if separation > 3:
        score += 20

    elif separation > 2:
        score += 15

    elif separation > 1:
        score += 10

    elif separation > 0.5:
        score += 5

    # ==========================
    # Price above EMA20 (15 points)
    # ==========================

    if close > ema_fast:
        score += 15

    # ==========================
    # Strong Momentum (10 points)
    # ==========================

    if rsi > 60:
        score += 10

    return round(score, 2)