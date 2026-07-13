"""
backtesting/metrics.py

Professional Performance Metrics
"""


def calculate_metrics(results):

    profits = results["profits"]

    total_profit = results["total_profit"]

    total_trades = results["total_trades"]

    winning = [p for p in profits if p > 0]
    losing = [p for p in profits if p <= 0]

    winning_trades = len(winning)
    losing_trades = len(losing)

    if total_trades > 0:
        win_rate = winning_trades / total_trades * 100
    else:
        win_rate = 0

    gross_profit = sum(winning)

    gross_loss = abs(sum(losing))

    if gross_loss == 0:
        profit_factor = float("inf")
    else:
        profit_factor = gross_profit / gross_loss

    avg_win = gross_profit / winning_trades if winning_trades else 0

    avg_loss = gross_loss / losing_trades if losing_trades else 0

    expectancy = 0

    if total_trades:

        expectancy = (
            (win_rate / 100) * avg_win
            -
            ((100 - win_rate) / 100) * avg_loss
        )

    return {

        "Total Trades": total_trades,

        "Winning Trades": winning_trades,

        "Losing Trades": losing_trades,

        "Win Rate": round(win_rate, 2),

        "Gross Profit": round(gross_profit, 2),

        "Gross Loss": round(gross_loss, 2),

        "Net Profit": round(total_profit, 2),

        "Profit Factor": round(profit_factor, 2)
        if profit_factor != float("inf")
        else "Infinite",

        "Average Win": round(avg_win, 2),

        "Average Loss": round(avg_loss, 2),

        "Expectancy": round(expectancy, 2)
    }