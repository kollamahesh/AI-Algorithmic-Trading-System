"""
charts.py

Creates performance charts.
"""

import matplotlib.pyplot as plt


def plot_equity_curve(equity):

    plt.figure(figsize=(10, 5))

    plt.plot(
        equity,
        linewidth=2,
        marker="o"
    )

    plt.title("Equity Curve")

    plt.xlabel("Trades")

    plt.ylabel("Capital (₹)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("equity_curve.png")

    plt.close()

    print("\nEquity curve saved as equity_curve.png")