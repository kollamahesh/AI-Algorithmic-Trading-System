"""
position_size.py

Professional Position Sizing
"""


def calculate_position_size(capital, risk_percent, entry, stop):

    risk_amount = capital * (risk_percent / 100)

    risk_per_share = abs(entry - stop)

    if risk_per_share == 0:

        quantity = 0

    else:

        quantity = int(risk_amount // risk_per_share)

    investment = quantity * entry

    return {

        "Capital": round(capital, 2),

        "Risk Amount": round(risk_amount, 2),

        "Risk Per Share": round(risk_per_share, 2),

        "Quantity": quantity,

        "Investment": round(investment, 2)

    }