import streamlit as st
import pandas as pd

from scanner.scanner import scan_stock
from backtesting.backtester import run_backtest

st.set_page_config(
    page_title="Backtesting",
    page_icon="📉",
    layout="wide"
)

st.title("📉 Strategy Backtester")

st.markdown("---")

symbol = st.text_input(
    "Stock Symbol",
    value="RELIANCE.NS"
)

if st.button(
    "▶ Run Backtest",
    use_container_width=True
):

    with st.spinner("Running Backtest..."):

        df = scan_stock(symbol)

        results = run_backtest(
            df,
            verbose=False
        )

    st.success("Backtest Complete!")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Final Capital",
        f"₹{results['final_capital']:,.2f}"
    )

    col2.metric(
        "Net Profit",
        f"₹{results['total_profit']:,.2f}"
    )

    col3.metric(
        "Win Rate",
        f"{results['win_rate']}%"
    )

    st.markdown("---")

    st.subheader("Equity Curve")

    equity = pd.DataFrame({
        "Capital": results["equity_curve"]
    })

    st.line_chart(equity)