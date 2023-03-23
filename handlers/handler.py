from aiogram import Dispatcher, types
from datetime import datetime
from utils.random_cat import get_picture
from utils.exchange_rate import rate
from utils.btc_rate import rate as btc_rate
from utils.random_receipt import receipt
from utils.movies import str_for_bot
from utils.random_joke import joke
from globals import bot
from keyboard.user_kb import kb_client


async def send_welcome(message: types.Message):
    await message.reply("Привет! Этот простенький бот создан в качестве задания для контрольной работы. Ниже "
                        "перечислены функции, которые он умеет выполнять...", reply_markup=kb_client)


async def send_cat(message: types.Message):
    await message.reply(get_picture(), reply_markup=kb_client)


async def send_time(message: types.Message):
    await message.reply(f"Сейчас {datetime.now().strftime('%H:%M:%S')}", reply_markup=kb_client)


async def send_exchange(message: types.Message):
    await message.reply(f"Актульный курс валют:  Доллар США - {rate.get('USD')}, Евро - {rate.get('EUR')}, "
                        f"Российский рубль - {rate.get('RUB')}", reply_markup=kb_client)


async def send_joke(message: types.Message):
    await message.reply(joke, reply_markup=kb_client)


async def send_btc(message: types.Message):
    await message.reply(f"Курс биткоина - {btc_rate['price']} долларов США", reply_markup=kb_client)


async def send_sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=r"CAACAgIAAxkBAAEIOPZkGe-Pc0KUIDWHy1AKWX-7MFO7JQACzBQAAgrXyUsa7GgoHs1N_y8E",
                           reply_markup=kb_client)


async def send_receipt(message: types.Message):
    await message.reply(receipt.str_for_bot(), reply_markup=kb_client)


async def send_movies(message: types.Message):
    await message.reply(str_for_bot, reply_markup=kb_client)


def register_user_handlers(dp:Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 's'])
    dp.register_message_handler(send_cat, commands=['Случайное_фото_котика😺', 'cat'])
    dp.register_message_handler(send_time, commands=['Показать_время⌚', 'time'])
    dp.register_message_handler(send_exchange, commands=['Курс_валют💵', 'course'])
    dp.register_message_handler(send_joke, commands=['Случайная_шутка😄', 'joke'])
    dp.register_message_handler(send_sticker, commands=['Получить_стикер🖼️', 'sticker'])
    dp.register_message_handler(send_btc, commands=['Курс_биткоина🪙️', 'btc'])
    dp.register_message_handler(send_receipt, commands=['Прислать_рецепт🍲️', 'food'])
    dp.register_message_handler(send_movies, commands=['Топ_фильмов🎥', 'movies'])




