from aiogram import Dispatcher, types
from datetime import datetime
from utils import get_picture, rate, btc_rate, receipt, str_for_bot, joke, db1
from globals import bot
from keyboard.user_kb import kb_client, inline_kb


async def send_welcome(message: types.Message):
    await message.answer("Привет! Этот простенький бот создан в качестве задания для контрольной работы. Ниже "
                        "перечислены функции, которые он умеет выполнять...", reply_markup=kb_client)


async def send_cat(message: types.Message):
    await message.answer(get_picture(), reply_markup=kb_client)


async def send_time(message: types.Message):
    await message.answer(f"Сейчас {datetime.now().strftime('%H:%M:%S')}", reply_markup=kb_client)


async def send_exchange(message: types.Message):
    await message.answer(f"Актульный курс валют:  Доллар США - {rate.get('USD')}, Евро - {rate.get('EUR')}, "
                        f"Российский рубль - {rate.get('RUB')}", reply_markup=kb_client)


async def send_joke(message: types.Message):
    await message.answer(joke, reply_markup=kb_client)


async def send_btc(message: types.Message):
    await message.answer(f"Курс биткоина - {btc_rate['price']} долларов США", reply_markup=kb_client)


async def send_sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=r"CAACAgIAAxkBAAEIOPZkGe-Pc0KUIDWHy1AKWX-7MFO7JQACzBQAAgrXyUsa7GgoHs1N_y8E",
                           reply_markup=kb_client)


async def send_receipt(message: types.Message):
    await message.answer(receipt.str_for_bot(), reply_markup=kb_client)


async def send_movies(message: types.Message):
    await message.answer(str_for_bot, reply_markup=kb_client)


async def registration(message: types.Message):
    if (str(message.from_user.id),) not in db1.select_user_id():
        await message.answer("Вы успешно зарегистрировались!",
                            db1.insert_user_id(message.from_user.id, datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                            reply_markup=kb_client)
    else:
        await message.answer("Вы уже зарегистрированы!",
                            reply_markup=kb_client)


async def about(message: types.Message):
    await message.answer("Ещё раз привет! Меня зовут Влад Михайлов и я являюсь студентом IT Step по направлению "
                         "'Python WEB'. Ниже прикреплены ссылки на мои соц. сети для связи ⬇️", reply_markup=inline_kb)


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
    dp.register_message_handler(registration, commands=['Регистрация', 'registration'])
    dp.register_message_handler(about, commands=['О_разработчике👨', 'sw'])




