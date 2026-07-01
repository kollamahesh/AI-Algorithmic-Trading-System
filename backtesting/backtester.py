from risk.risk_manager import calculate_position_size


def run_backtest(df):

    # Initial Capital
    capital = 100000

    # Trade Variables
    position = False
    entry_price = 0
    quantity = 0
    stop_loss_price = 0

    profits = []

    for _, row in df.iterrows():

        signal = int(row["Signal"])
        close_price = float(row["Close"])

        # ==========================
        # BUY
        # ==========================
        if signal == 1 and not position:

            entry_price = close_price

            # Fixed 2% Stop Loss
            stop_loss_price = entry_price * 0.98

            # Position Size from Risk Manager
            quantity = calculate_position_size(
                capital=capital,
                risk_percent=1,
                entry_price=entry_price,
                stop_loss_price=stop_loss_price
            )

            position = True

            print("\n===================================")
            print("NEW TRADE")
            print("===================================")
            print(f"Capital      : ₹{capital:.2f}")
            print(f"Entry Price  : ₹{entry_price:.2f}")
            print(f"Stop Loss    : ₹{stop_loss_price:.2f}")
            print(f"Quantity     : {quantity}")

        # ==========================
        # SELL
        # ==========================
        elif signal == -1 and position:

            exit_price = close_price

            trade_profit = (
                exit_price - entry_price
            ) * quantity

            capital += trade_profit

            profits.append(trade_profit)

            print("\nTRADE CLOSED")
            print(f"Exit Price   : ₹{exit_price:.2f}")
            print(f"P&L          : ₹{trade_profit:.2f}")
            print(f"Capital      : ₹{capital:.2f}")

            position = False

    return profits