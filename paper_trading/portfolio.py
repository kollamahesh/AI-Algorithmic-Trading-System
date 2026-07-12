"""
paper_trading/portfolio.py

Portfolio Management
"""

from paper_trading.storage import load_portfolio, save_portfolio

# ==========================================
# Load Portfolio
# ==========================================

portfolio = load_portfolio()

capital = portfolio["capital"]

open_positions = portfolio["open_positions"]

closed_positions = portfolio["closed_positions"]


# ==========================================
# Save Portfolio
# ==========================================

def save():

    save_portfolio(

        capital,

        open_positions,

        closed_positions

    )


# ==========================================
# Capital
# ==========================================

def get_capital():

    return capital


def update_capital(new_capital):

    global capital

    capital = new_capital


# ==========================================
# Positions
# ==========================================

def add_position(position):

    open_positions.append(position)


def close_position(position):

    open_positions.remove(position)

    closed_positions.append(position)


# ==========================================
# Dashboard Helpers
# ==========================================

def get_open_positions():

    return open_positions


def get_closed_positions():

    return closed_positions


def get_total_investment():

    return sum(

        position["Investment"]

        for position in open_positions

    )


def get_total_positions():

    return len(open_positions)


# ==========================================
# Save Everything
# ==========================================

def commit():

    save()