from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("KITE_API_KEY")
api_secret = os.getenv("KITE_API_SECRET")

kite = KiteConnect(api_key=api_key)


def save_access_token(token):

    env_file = ".env"

    with open(env_file, "r") as file:
        lines = file.readlines()

    with open(env_file, "w") as file:

        for line in lines:

            if line.startswith("KITE_ACCESS_TOKEN="):

                file.write(f"KITE_ACCESS_TOKEN={token}\n")

            else:

                file.write(line)


def generate_access_token(request_token):

    data = kite.generate_session(
        request_token=request_token,
        api_secret=api_secret
    )

    token = data["access_token"]

    save_access_token(token)

    print("\n")
    print("=" * 60)
    print("ACCESS TOKEN SAVED")
    print("=" * 60)

    return token


if __name__ == "__main__":

    request = input("Request Token: ").strip()

    generate_access_token(request)