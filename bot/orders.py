from bot.client import client
import logging
import bot.logging_config 

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        # Normalize inputs
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        # Basic validation
        if side not in ["BUY", "SELL"]:
            raise ValueError("Side must be BUY or SELL")

        if order_type not in ["MARKET", "LIMIT"]:
            raise ValueError("Order type must be MARKET or LIMIT")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        # Place MARKET order
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        # Place LIMIT order
        elif order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders")

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        # Log success
        logging.info(f"Order Success: {order}")

        return {
            "status": "success",
            "orderId": order.get("orderId"),
            "symbol": order.get("symbol"),
            "type": order.get("type"),
            "side": order.get("side")
        }

    except Exception as e:
        logging.error(f"Order Failed: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }