from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.client = Client(
            api_key=os.getenv("API_KEY"),
            api_secret=os.getenv("API_SECRET")
        )

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **params):
        return self.client.futures_create_order(**params)
        print("Client file loaded successfully")

    def get_open_orders(self, symbol):
        return self.client.futures_get_open_orders(symbol=symbol)