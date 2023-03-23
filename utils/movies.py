import requests
from data.config import KP_TOKEN, KP_LINK


r = requests.get(KP_LINK, headers={'X-API-KEY': KP_TOKEN, 'Content-Type': 'application/json'})
data = r.json()

count = 1
movies_list = []

for i in data['films']:
    one_movie = []
    one_movie.extend((str(count) + '. ', i['nameRu'] + ',', 'Год выпуска: ' + i['year'] + ',',
                      'Рейтинг Кинопоиска: ' + i['rating'] + ',', 'Постер: ' + i['posterUrl']))
    movies_list.append(one_movie)
    count += 1

str_for_bot = ''
for i in movies_list:
    str_for_bot += " ".join(map(str, i)) + ',\n'









