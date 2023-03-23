from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# function buttons
b1 = KeyboardButton('/Случайное_фото_котика😺')
b2 = KeyboardButton('/Показать_время⌚')
b3 = KeyboardButton('/Курс_валют💵')
b4 = KeyboardButton('/Случайная_шутка😄')
b5 = KeyboardButton('/Получить_стикер🖼️')
b6 = KeyboardButton('/Курс_биткоина🪙️')
b7 = KeyboardButton('/Прислать_рецепт🍲️')
b8 = KeyboardButton('/Игра_угадай_число🎲')
b9 = KeyboardButton('/Топ_фильмов🎥')


kb_client = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
kb_client.row(b2, b3).row(b4, b5).row(b6, b7).row(b1, b9).row(b8)

