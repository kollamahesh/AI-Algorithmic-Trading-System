import streamlit as st
import pandas as pd

from scanner.scanner import scan_market
from broker.broker import Broker

st.set_page_config(
    page_title="Scanner",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Market Scanner")

st.markdown("---")

# ==========================================
# Initialize Broker
# ==========================================

broker = Broker()

# ==========================================
# Session State
# ==========================================

if "scan_results" not in st.session_state:
    st.session_state.scan_results = None

if "best_stock" not in st.session_state:
    st.session_state.best_stock = None

# ==========================================
# Run Scanner
# ==========================================

if st.button("▶ Run Scanner", use_container_width=True):

    with st.spinner("Scanning NIFTY 50..."):

        results, best_stock = scan_market()

    st.session_state.scan_results = results
    st.session_state.best_stock = best_stock

    st.success("Scan Complete!")

# ==========================================
# Display Results
# ==========================================

if st.session_state.scan_results is not None:

    results = st.session_state.scan_results
    best_stock = st.session_state.best_stock

    st.markdown("---")

    st.subheader("🏆 Best Trade")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Symbol", best_stock["Symbol"])
    col2.metric("Entry", f"₹{best_stock['Entry']:.2f}")
    col3.metric("Target", f"₹{best_stock['Target']:.2f}")
    col4.metric("Stop", f"₹{best_stock['Stop']:.2f}")

    st.markdown("### Trading")

    if st.button("🛒 Buy Best Trade"):

        success, message = broker.buy(best_stock)

        if success:
            st.success(message)
        else:
            st.error(message)

    st.markdown("---")

    st.subheader("📋 Top Opportunities")

    df = pd.DataFrame(results)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )