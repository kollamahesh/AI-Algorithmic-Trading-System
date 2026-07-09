from journal.trade_journal import (
    add_trade,
    get_trade_history
)

add_trade(
    entry_price=1463.34,
    exit_price=1433.35,
    quantity=34,
    exit_reason="Stop Loss",
    profit=-1118.15
)

add_trade(
    entry_price=1493.07,
    exit_price=1462.48,
    quantity=33,
    exit_reason="Stop Loss",
    profit=-1107.00
)

print(get_trade_history())