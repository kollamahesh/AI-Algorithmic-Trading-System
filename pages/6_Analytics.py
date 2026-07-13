import streamlit as st
import pandas as pd

from analytics.metrics import calculate_metrics
from analytics.equity_curve import build_equity_curve
from analytics.drawdown import calculate_max_drawdown
from analytics.sharpe_ratio import calculate_sharpe_ratio

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Analytics Dashboard")

st.markdown("---")

metrics = calculate_metrics()

if metrics is None:

    st.info("No completed trades yet.")

    st.stop()

# ==========================================
# Read Trade History
# ==========================================

df = pd.read_csv("trade_journal/trade_history.csv")

profits = df["Profit"].tolist()

equity = build_equity_curve(profits)

sharpe = calculate_sharpe_ratio(profits)

drawdown = calculate_max_drawdown(equity)

# ==========================================
# Top Metrics
# ==========================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Win Rate",
    f"{metrics['Win Rate']:.2f}%"
)

col2.metric(
    "Sharpe Ratio",
    round(sharpe,2)
)

col3.metric(
    "Max Drawdown",
    f"{drawdown:.2f}%"
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Win",
    f"₹{metrics['Average Win']:,.2f}"
)

col2.metric(
    "Average Loss",
    f"₹{metrics['Average Loss']:,.2f}"
)

col3.metric(
    "Profit Factor",
    round(metrics["Profit Factor"],2)
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Trades",
    metrics["Total Trades"]
)

col2.metric(
    "Winning Trades",
    metrics["Winning Trades"]
)

col3.metric(
    "Losing Trades",
    metrics["Losing Trades"]
)

st.metric(
    "Net Profit",
    f"₹{metrics['Net Profit']:,.2f}"
)

st.markdown("---")

# ==========================================
# Equity Curve
# ==========================================

st.subheader("📈 Equity Curve")

equity_df = pd.DataFrame({

    "Capital": equity

})

st.line_chart(equity_df)

# ==========================================
# Trade History
# ==========================================

st.markdown("---")

st.subheader("📋 Completed Trades")

st.dataframe(

    df,

    use_container_width=True,

    hide_index=True

)