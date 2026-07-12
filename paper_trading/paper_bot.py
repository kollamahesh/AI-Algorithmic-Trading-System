from paper_trading.trader import buy_stock
from paper_trading.monitor import check_position

buy_stock(

    symbol="ICICIBANK.NS",

    entry=1401.20,

    stop=1363.14,

    target=1477.31,

    quantity=26

)

print("\nChecking Market...")

check_position(

    symbol="ICICIBANK.NS",

    current_price=1480

)