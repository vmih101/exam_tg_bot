import requests
from data.config import BTC_LINK

data = requests.get(BTC_LINK)
rate = data.json()
price = rate['price']
