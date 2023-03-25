import requests
from data.config import BTC_LINK

r = requests.get(BTC_LINK)
data = r.json()
btc_rate = data['price']
