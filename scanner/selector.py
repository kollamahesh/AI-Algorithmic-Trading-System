"""
selector.py

Select the best trading opportunity.
"""


def select_best_stock(results):

    if len(results) == 0:
        return None

    buy_candidates = [

        stock

        for stock in results

        if stock["Signal"] in ["BUY", "HOLD"]

    ]

    if len(buy_candidates) == 0:
        return None

    buy_candidates.sort(

        key=lambda x: x["Score"],

        reverse=True

    )

    return buy_candidates[0]