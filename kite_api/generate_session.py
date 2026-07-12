from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("KITE_API_KEY")
api_secret = os.getenv("KITE_API_SECRET")

kite = KiteConnect(api_key=api_key)

request_token = input("Enter Request Token: ").strip()

data = kite.generate_session(
    request_token=request_token,
    api_secret=api_secret
)

print("\nSUCCESS!")
print("Access Token:")
print(data["access_token"])