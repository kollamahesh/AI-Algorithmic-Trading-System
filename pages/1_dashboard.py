import streamlit as st
import pandas as pd
import os

from paper_trading.portfolio import (
    get_capital,
    get_total_investment,
    get_total_positions
)

from analytics.metrics import calculate_metrics

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Trading Dashboard")

st.markdown("---")

# ==========================================
# Portfolio Summary
# ==========================================

cash = get_capital()
investment = get_total_investment()
portfolio = cash + investment
positions = get_total_positions()

metrics = calculate_metrics()

net_profit = 0
win_rate = 0

if metrics is not None:
    net_profit = metrics["Net Profit"]
    win_rate = metrics["Win Rate"]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Portfolio Value",
    f"₹{portfolio:,.2f}"
)

col2.metric(
    "Available Cash",
    f"₹{cash:,.2f}"
)

col3.metric(
    "Net Profit",
    f"₹{net_profit:,.2f}"
)

col4.metric(
    "Open Positions",
    positions
)

st.markdown("---")

# ==========================================
# Performance
# ==========================================

col1, col2 = st.columns(2)

col1.metric(
    "Win Rate",
    f"{win_rate:.2f}%"
)

if metrics is not None:
    col2.metric(
        "Total Trades",
        metrics["Total Trades"]
    )
else:
    col2.metric(
        "Total Trades",
        0
    )

st.markdown("---")

# ==========================================
# Recent Trades
# ==========================================

st.subheader("📜 Recent Trades")

history_file = "trade_journal/trade_history.csv"

if os.path.exists(history_file):

    df = pd.read_csv(history_file)

    if len(df):

        st.dataframe(

            df.tail(5),

            use_container_width=True,

            hide_index=True

        )

    else:

        st.info("No trades yet.")

else:

    st.info("Trade history not found.")

st.markdown("---")

# ==========================================
# Portfolio Status
# ==========================================

if positions == 0:

    st.success("✅ No Open Positions")

else:

    st.warning(f"⚠ {positions} Position(s) Currently Open")