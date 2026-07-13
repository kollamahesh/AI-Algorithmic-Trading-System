import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Trade History",
    page_icon="📒",
    layout="wide"
)

st.title("📒 Trade History")

FILE = "trade_journal/trade_history.csv"

if not os.path.exists(FILE):

    st.info("No trades yet.")

    st.stop()

df = pd.read_csv(FILE)

# -------------------------
# Summary
# -------------------------

total = len(df)

wins = len(df[df["Profit"] > 0])

losses = len(df[df["Profit"] <= 0])

net = df["Profit"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Trades", total)

col2.metric("Winning Trades", wins)

col3.metric("Losing Trades", losses)

col4.metric("Net Profit", f"₹{net:,.2f}")

st.markdown("---")

# -------------------------
# Search
# -------------------------

symbols = ["All"] + sorted(df["Symbol"].unique().tolist())

selected = st.selectbox(
    "Filter Symbol",
    symbols
)

if selected != "All":

    df = df[df["Symbol"] == selected]

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.download_button(
    "📥 Download CSV",
    df.to_csv(index=False),
    "trade_history.csv",
    "text/csv"
)