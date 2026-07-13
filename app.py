"""
AI Trading Platform
Main Landing Page
"""

import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Trading Platform",
    page_icon="📈",
    layout="wide",
)

# ==========================================
# TITLE
# ==========================================

st.title("📈 AI Trading Platform")

st.markdown("---")

st.markdown(
    """
## Welcome 👋

This platform provides everything required for algorithmic trading and quantitative research.

Use the navigation menu on the left to access the different modules.
"""
)

# ==========================================
# FEATURES
# ==========================================

st.subheader("Available Modules")

col1, col2 = st.columns(2)

with col1:

    st.success("📊 Dashboard")
    st.success("🔍 Market Scanner")
    st.success("📉 Backtesting")

with col2:

    st.success("⚙️ Strategy Optimizer")
    st.success("💼 Portfolio")
    st.success("📈 Analytics")

st.markdown("---")

# ==========================================
# PROJECT STATUS
# ==========================================

st.subheader("Project Status")

status = {
    "Zerodha API": "✅",
    "Historical Data": "✅",
    "Live Market Data": "✅",
    "Scanner": "✅",
    "Risk Management": "✅",
    "Paper Trading": "✅",
    "Portfolio": "✅",
    "Backtesting": "✅",
    "Strategy Optimizer": "✅",
    "Multi-Stock Optimizer": "✅",
    "CSV Export": "✅",
    "Dashboard": "🚧",
    "Analytics": "🚧",
    "Live Trading": "⏳",
    "AI Strategy Ranking": "⏳",
}

for module, state in status.items():
    st.write(f"{state} {module}")

st.markdown("---")

st.info(
    "Select a page from the left sidebar to start using the platform."
)