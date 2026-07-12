from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("KITE_API_KEY")

kite = KiteConnect(api_key=api_key)


def get_login_url():
    return kite.login_url()


if __name__ == "__main__":

    print("\n")
    print("=" * 60)
    print("ZERODHA LOGIN")
    print("=" * 60)

    print()

    print(get_login_url())