def calculate_position_size(
    capital,
    risk_percent,
    entry_price,
    stop_loss_price
):
    """
    Calculate the number of shares to buy based on
    a fixed percentage of account risk.
    """

    # Maximum money we are willing to lose
    max_risk = capital * (risk_percent / 100)

    # Risk on one share
    risk_per_share = entry_price - stop_loss_price

    # Prevent division by zero or invalid stop loss
    if risk_per_share <= 0:
        return 0

    # Number of shares
    quantity = int(max_risk / risk_per_share)

    return quantity