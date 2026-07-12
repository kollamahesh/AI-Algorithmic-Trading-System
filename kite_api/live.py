from broker.zerodha import get_kite

kite = get_kite()

profile = kite.profile()

print("=" * 50)
print("CONNECTED TO ZERODHA")
print("=" * 50)

print(f"User Name : {profile['user_name']}")
print(f"User ID   : {profile['user_id']}")
print(f"Email     : {profile['email']}")
print(f"Broker    : {profile['broker']}")