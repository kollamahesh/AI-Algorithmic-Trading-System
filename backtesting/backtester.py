from config.settings import *

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

from journal.trade_journal import add_trade


def run_backtest(df, verbose=True):

    capital = CAPITAL

    position = False

    entry_price = 0
    quantity = 0

    stop_loss_price = 0
    target_price = 0

    profits = []
    equity_curve = [capital]
    for _, row in df.iterrows():

        signal = int(row["Signal"])
        close_price = float(row["Close"])

        # =====================================
        # BUY
        # =====================================

        if signal == 1 and not position:

            expected_entry = close_price

            entry_price = apply_buy_slippage(
                expected_entry
            )

            stop_loss_price = calculate_stop_loss(
                entry_price
            )

            target_price = calculate_target(
                entry_price
            )

            quantity = calculate_position_size(
                capital=CAPITAL,
                risk_percent= RISK_PERCENT,
                entry_price=entry_price,
                stop_loss_price=stop_loss_price
            )

            position = True

            if verbose:

                print("\n===================================")
                print("NEW TRADE")
                print("===================================")

                print(f"Capital        : ₹{capital:.2f}")
                print(f"Expected Buy   : ₹{expected_entry:.2f}")
                print(f"Actual Buy     : ₹{entry_price:.2f}")
                print(f"Stop Loss      : ₹{stop_loss_price:.2f}")
                print(f"Target Price   : ₹{target_price:.2f}")
                print(f"Quantity       : {quantity}")

        # =====================================
        # STOP LOSS
        # =====================================

        elif position and check_stop_loss(
            close_price,
            stop_loss_price
        ):

            expected_exit = stop_loss_price

            exit_price = apply_sell_slippage(
                expected_exit
            )

            gross_profit = (
                exit_price - entry_price
            ) * quantity

            brokerage = calculate_brokerage(
                quantity,
                entry_price,
                exit_price
            )

            net_profit = gross_profit - brokerage

            capital += net_profit
            
            equity_curve.append(capital)

            profits.append(net_profit)

            add_trade(
                symbol="RELIANCE.NS",
                entry_price=entry_price,
                exit_price=exit_price,
                quantity=quantity,
                stop_loss=stop_loss_price,
                target=target_price,
                gross_profit=gross_profit,
                brokerage=brokerage,
                net_profit=net_profit,
                exit_reason="..."
            )

            if verbose:

                print("\nSTOP LOSS HIT!")

                print(f"Expected Exit : ₹{expected_exit:.2f}")
                print(f"Actual Exit   : ₹{exit_price:.2f}")
                print(f"Gross Profit  : ₹{gross_profit:.2f}")
                print(f"Brokerage     : ₹{brokerage:.2f}")
                print(f"Net Profit    : ₹{net_profit:.2f}")
                print(f"Capital       : ₹{capital:.2f}")

            position = False
                    # =====================================
        # TARGET HIT
        # =====================================

                # =====================================
        # TARGET HIT
        # =====================================

        elif position and close_price >= target_price:

            expected_exit = target_price

            exit_price = apply_sell_slippage(
                expected_exit
            )

            gross_profit = (
                exit_price - entry_price
            ) * quantity

            brokerage = calculate_brokerage(
                quantity,
                entry_price,
                exit_price
            )

            net_profit = gross_profit - brokerage

            capital += net_profit
            
            equity_curve.append(capital)

            profits.append(net_profit)

            add_trade(
                symbol="RELIANCE.NS",
                entry_price=entry_price,
                exit_price=exit_price,
                quantity=quantity,
                stop_loss=stop_loss_price,
                target=target_price,
                gross_profit=gross_profit,
                brokerage=brokerage,
                net_profit=net_profit,
                exit_reason="..."
            )

            if verbose:

                print("\nTARGET HIT!")

                print(f"Expected Exit : ₹{expected_exit:.2f}")
                print(f"Actual Exit   : ₹{exit_price:.2f}")
                print(f"Gross Profit  : ₹{gross_profit:.2f}")
                print(f"Brokerage     : ₹{brokerage:.2f}")
                print(f"Net Profit    : ₹{net_profit:.2f}")
                print(f"Capital       : ₹{capital:.2f}")

            position = False

        # =====================================
        # SELL SIGNAL
        # =====================================

        elif signal == -1 and position:

            expected_exit = close_price

            exit_price = apply_sell_slippage(
                expected_exit
            )

            gross_profit = (
                exit_price - entry_price
            ) * quantity

            brokerage = calculate_brokerage(
                quantity,
                entry_price,
                exit_price
            )

            net_profit = gross_profit - brokerage

            capital += net_profit
            
            equity_curve.append(capital)

            profits.append(net_profit)

            add_trade(
                symbol="RELIANCE.NS",
                entry_price=entry_price,
                exit_price=exit_price,
                quantity=quantity,
                stop_loss=stop_loss_price,
                target=target_price,
                gross_profit=gross_profit,
                brokerage=brokerage,
                net_profit=net_profit,
                exit_reason="..."
            )

            if verbose:

                print("\nSELL SIGNAL!")

                print(f"Expected Exit : ₹{expected_exit:.2f}")
                print(f"Actual Exit   : ₹{exit_price:.2f}")
                print(f"Gross Profit  : ₹{gross_profit:.2f}")
                print(f"Brokerage     : ₹{brokerage:.2f}")
                print(f"Net Profit    : ₹{net_profit:.2f}")
                print(f"Capital       : ₹{capital:.2f}")

            position = False

    # =====================================
    # PERFORMANCE SUMMARY
    # =====================================

    total_profit = sum(profits)

    total_trades = len(profits)

    winning_trades = len(
        [p for p in profits if p > 0]
    )

    losing_trades = len(
        [p for p in profits if p <= 0]
    )

    if total_trades > 0:
        win_rate = (
            winning_trades / total_trades
        ) * 100
    else:
        win_rate = 0

    results = {

        "profits": profits,
        
        "equity_curve": equity_curve,

        "total_profit": total_profit,

        "final_capital": capital,

        "total_trades": total_trades,

        "winning_trades": winning_trades,

        "losing_trades": losing_trades,

        "win_rate": round(win_rate, 2)

    }
    
    from analytics.equity_curve import build_equity_curve

    results["equity_curve"] = build_equity_curve(results["profits"])
    from backtesting.metrics import calculate_metrics
    from backtesting.report import print_report

    metrics = calculate_metrics(results)

    if verbose:
        print_report(results)
    return results