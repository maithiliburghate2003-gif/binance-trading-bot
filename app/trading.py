from app.client import BinanceClient
from app.logger import setup_logger

logger = setup_logger()

class TradingService:
    def __init__(self):
        self.client = BinanceClient()

    def validate_inputs(self, symbol, side, order_type, quantity, price):
        if side not in ["BUY", "SELL"]:
            raise ValueError("Side must be BUY or SELL")

        if order_type not in ["MARKET", "LIMIT"]:
            raise ValueError("Order type must be MARKET or LIMIT")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if order_type == "LIMIT" and price is None:
            raise ValueError("Price required for LIMIT order")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        print("DEBUG: place_order called")
        logger.info("place_order() function called")  # ✅ moved here

        try:
            self.validate_inputs(symbol, side, order_type, quantity, price)

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":
                params.update({
                    "price": price,
                    "timeInForce": "GTC"
                })

            logger.info(f"Request: {params}")

            response = self.client.place_order(**params)

            logger.info(f"Response: {response}")

            return response

        except Exception as e:
            logger.error(f"Error: {str(e)}", exc_info=True)  # better logging
            raise