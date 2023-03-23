from data.config import JOKE_LINK
import requests

def random_joke():
    while True:
        try:
            request = requests.get(JOKE_LINK)
            request.json()
        except:
            pass
        else:
            break
    return request.json()

joke = random_joke().get('content')

