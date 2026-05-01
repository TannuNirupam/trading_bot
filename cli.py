from bot.orders import place_order

symbol = input("Enter symbol (e.g. BTCUSDT): ")
side = input("BUY or SELL: ")
order_type = input("MARKET or LIMIT: ")
quantity = float(input("Quantity: "))

price = None
if order_type == "LIMIT":
    price = float(input("Price: "))

result = place_order(symbol, side, order_type, quantity, price)

print("Result:", result)