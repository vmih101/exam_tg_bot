from data.config import EXCHANGE_LINK
import requests


def get_exchange():
    r = requests.get(EXCHANGE_LINK)
    data = r.json()
    currency = {}
    for i in data:
        if i['Cur_Abbreviation'] in ('USD', 'EUR', 'RUB'):
            currency[i['Cur_Abbreviation']] = i['Cur_OfficialRate']
    return currency

rate = get_exchange()
