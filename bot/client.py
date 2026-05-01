from binance.client import Client

API_KEY = "PJNz6i6r9VwvnDmgZyLhwWtQxoW8tiMIymmWJ0ei5bo5TDVi4nIHOBsgBdTXyKQh"
API_SECRET = "q6tb7Aiuc6rHRpHQPpqFwG8HJsGNvIwxCnndAillBSdurrLcnu1dytSnUE1B4aLi"

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
