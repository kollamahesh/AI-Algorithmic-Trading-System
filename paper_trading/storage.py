"""
paper_trading/storage.py

Save and Load Portfolio
"""

import json
import os


FILE_NAME = "paper_portfolio.json"


def save_portfolio(capital, open_positions, closed_positions):

    data = {

        "capital": capital,

        "open_positions": open_positions,

        "closed_positions": closed_positions

    }

    with open(FILE_NAME, "w") as file:

        json.dump(data, file, indent=4, default=str)

    print("\nPortfolio saved.")


def load_portfolio():

    if not os.path.exists(FILE_NAME):

        return {

            "capital": 100000,

            "open_positions": [],

            "closed_positions": []

        }

    with open(FILE_NAME, "r") as file:

        return json.load(file)