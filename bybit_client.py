# bybit_client.py
import os
from pybit.unified_trading import HTTP

def place_order(direction, entry, sl, tp):
    session = HTTP(
        testnet=True,
        api_key=os.getenv("BYBIT_API_KEY"),
        api_secret=os.getenv("BYBIT_API_SECRET")
    )

    side = "Buy" if direction.upper() == "LONG" else "Sell"
    session.place_order(
        category="linear",
        symbol="SOLUSDT",
        side=side,
        order_type="Market",
        qty=1,
        take_profit=tp,
        stop_loss=sl
    )
