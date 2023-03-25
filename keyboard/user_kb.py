from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton,  KeyboardButton

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
b10 = KeyboardButton('/Регистрация')
b11 = KeyboardButton('/О_разработчике👨')


kb_client = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
kb_client.row(b10).row(b2, b3).row(b4, b5).row(b6, b7).row(b1, b9).row(b8, b11)


inline_b1 = InlineKeyboardButton(text="GitHub", url="https://github.com/vmih101")
inline_b2 = InlineKeyboardButton(text="LinkedIn", url="https://www.linkedin.com/in/vladislav-mikhailov/")
inline_b3 = InlineKeyboardButton(text="Telegram", url="https://t.me/z_x101")
inline_b4 = InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/vladislav.mikhailov101/")


inline_kb = InlineKeyboardMarkup()
inline_kb.add(inline_b1, inline_b2, inline_b3, inline_b4)

