import streamlit as st
import pandas as pd

from streamlit_autorefresh import st_autorefresh

from kite_api.live_price import get_live_price

from paper_trading.monitor import monitor_positions
from paper_trading.execution import close_paper_trade

from paper_trading.portfolio import (
    get_capital,
    get_total_investment,
    get_total_positions,
    get_open_positions,
    get_closed_positions,
)

# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="Portfolio",
    page_icon="💼",
    layout="wide",
)

# Refresh every 5 seconds
st_autorefresh(interval=5000, key="portfolio_refresh")

st.title("💼 Portfolio")

# ==========================================
# Auto Monitor
# ==========================================

messages = monitor_positions()

for message in messages:
    st.success(message)

st.markdown("---")

# ==========================================
# Portfolio Summary
# ==========================================

cash = get_capital()
investment = get_total_investment()
portfolio = cash + investment
positions = get_total_positions()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Portfolio Value", f"₹{portfolio:,.2f}")
c2.metric("Available Cash", f"₹{cash:,.2f}")
c3.metric("Invested Amount", f"₹{investment:,.2f}")
c4.metric("Open Positions", positions)

st.markdown("---")

# ==========================================
# Open Positions
# ==========================================

st.subheader("📈 Open Positions")

open_positions = get_open_positions()

if not open_positions:

    st.info("No open positions.")

else:

    rows = []
    total_pl = 0

    for position in open_positions:

        live = get_live_price(position["Symbol"])

        current = live * position["Quantity"]

        profit = current - position["Investment"]

        pct = (profit / position["Investment"]) * 100

        total_pl += profit

        rows.append({

            "Symbol": position["Symbol"],

            "Buy": round(position["Entry"],2),

            "Live": round(live,2),

            "Qty": position["Quantity"],

            "Investment": round(position["Investment"],2),

            "Current Value": round(current,2),

            "P/L ₹": round(profit,2),

            "P/L %": round(pct,2),

            "Target": position["Target"],

            "Stop": position["Stop"]

        })

    st.dataframe(
        pd.DataFrame(rows),
        use_container_width=True,
        hide_index=True
    )

    st.success(f"Live Unrealized P/L : ₹{total_pl:,.2f}")

    st.markdown("### Manual Exit")

    for position in open_positions:

        if st.button(
            f"🔴 Sell {position['Symbol']}",
            key=position["Symbol"]
        ):

            success, message = close_paper_trade(
                position["Symbol"]
            )

            if success:

                st.success(message)

                st.rerun()

            else:

                st.error(message)

st.markdown("---")

# ==========================================
# Closed Positions
# ==========================================

st.subheader("📜 Closed Positions")

closed = get_closed_positions()

if not closed:

    st.info("No closed positions.")

else:

    st.dataframe(

        pd.DataFrame(closed),

        use_container_width=True,

        hide_index=True

    )