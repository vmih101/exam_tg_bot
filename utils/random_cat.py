from data.config import CATS_LINK
import requests


def get_picture():
    r = requests.get(CATS_LINK)
    data = r.json()
    return data[0]['url']