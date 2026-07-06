from risk.risk_manager import calculate_position_size

from risk.stop_loss import (
    calculate_stop_loss,
    calculate_target,
    check_stop_loss
)

from costs.brokerage import calculate_brokerage

from execution.slippage import (
    apply_buy_slippage,
    apply_sell_slippage
)


def run_backtest(df):

    capital = 100000

    position = False

    entry_price = 0
    quantity = 0
    stop_loss_price = 0
    target_price = 0

    profits = []

    for _, row in df.iterrows():

        signal = int(row["Signal"])
        close_price = float(row["Close"])

        # ==================================================
        # BUY
        # ==================================================
        if signal == 1 and not position:

            expected_entry = close_price

            # Apply Buy Slippage
            entry_price = apply_buy_slippage(expected_entry)

            stop_loss_price = calculate_stop_loss(entry_price)
            target_price = calculate_target(entry_price)

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

            print(f"Capital        : ₹{capital:.2f}")
            print(f"Expected Buy   : ₹{expected_entry:.2f}")
            print(f"Actual Buy     : ₹{entry_price:.2f}")
            print(f"Stop Loss      : ₹{stop_loss_price:.2f}")
            print(f"Target Price   : ₹{target_price:.2f}")
            print(f"Quantity       : {quantity}")

        # ==================================================
        # STOP LOSS
        # ==================================================
        elif position and check_stop_loss(close_price, stop_loss_price):

            expected_exit = stop_loss_price

            exit_price = apply_sell_slippage(expected_exit)

            gross_profit = (
                exit_price - entry_price
            ) * quantity

            brokerage = calculate_brokerage(
                quantity,
                entry_price,
                exit_price
            )

            trade_profit = gross_profit - brokerage

            capital += trade_profit

            profits.append(trade_profit)

            print("\nSTOP LOSS HIT!")

            print(f"Expected Exit : ₹{expected_exit:.2f}")
            print(f"Actual Exit   : ₹{exit_price:.2f}")
            print(f"Gross Profit  : ₹{gross_profit:.2f}")
            print(f"Brokerage     : ₹{brokerage:.2f}")
            print(f"Net Profit    : ₹{trade_profit:.2f}")
            print(f"Capital       : ₹{capital:.2f}")

            position = False

        # ==================================================
        # TARGET HIT
        # ==================================================
        elif position and close_price >= target_price:

            expected_exit = target_price

            exit_price = apply_sell_slippage(expected_exit)

            gross_profit = (
                exit_price - entry_price
            ) * quantity

            brokerage = calculate_brokerage(
                quantity,
                entry_price,
                exit_price
            )

            trade_profit = gross_profit - brokerage

            capital += trade_profit

            profits.append(trade_profit)

            print("\nTARGET HIT!")

            print(f"Expected Exit : ₹{expected_exit:.2f}")
            print(f"Actual Exit   : ₹{exit_price:.2f}")
            print(f"Gross Profit  : ₹{gross_profit:.2f}")
            print(f"Brokerage     : ₹{brokerage:.2f}")
            print(f"Net Profit    : ₹{trade_profit:.2f}")
            print(f"Capital       : ₹{capital:.2f}")

            position = False

        # ==================================================
        # SELL SIGNAL
        # ==================================================
        elif signal == -1 and position:

            expected_exit = close_price

            exit_price = apply_sell_slippage(expected_exit)

            gross_profit = (
                exit_price - entry_price
            ) * quantity

            brokerage = calculate_brokerage(
                quantity,
                entry_price,
                exit_price
            )

            trade_profit = gross_profit - brokerage

            capital += trade_profit

            profits.append(trade_profit)

            print("\nSELL SIGNAL")

            print(f"Expected Exit : ₹{expected_exit:.2f}")
            print(f"Actual Exit   : ₹{exit_price:.2f}")
            print(f"Gross Profit  : ₹{gross_profit:.2f}")
            print(f"Brokerage     : ₹{brokerage:.2f}")
            print(f"Net Profit    : ₹{trade_profit:.2f}")
            print(f"Capital       : ₹{capital:.2f}")

            position = False

    return profits