"""
atr_trade.py

Creates ATR-based trade levels.
"""


def atr_trade_levels(entry_price, atr):

    stop_loss = entry_price - (1.5 * atr)

    target = entry_price + (3 * atr)

    risk = entry_price - stop_loss

    reward = target - entry_price

    rr_ratio = reward / risk

    return {
        "Entry": round(entry_price, 2),
        "Stop": round(stop_loss, 2),
        "Target": round(target, 2),
        "Risk": round(risk, 2),
        "Reward": round(reward, 2),
        "RR": round(rr_ratio, 2)
    }