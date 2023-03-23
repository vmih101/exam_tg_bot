from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from states.game_states import GameAttempts
from utils.random_number import random_number
from random import randint


async def start_guess_number(message: types.Message):
    await message.reply("Давай сыграем. Я загадал число от одного до десяти. Попробуй угадать с трёх попыток."
                        " Попытка номер 1...")
    global random_number
    random_number = str(randint(1, 10))
    print(random_number)
    await GameAttempts.A1.set()


async def handle_a1_answer(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == random_number:
        await message.answer("🎉 Cупер! Ты отгадал с первой попытки! Чем займёмся дальше?")
        await state.finish()
    else:
        await message.answer("🥲 Пока мимо. Пробуем дальше. Попытка номер 2...")
        await GameAttempts.A2.set()


async def handle_a2_answer(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == random_number:
        await message.answer("🎉 Абсолютно верно! Чем займёмся дальше?")
        await state.finish()
    else:
        await message.answer("🥲 Не верно. Не отчаивайся, у тебя осталась ещё одна попытка. Попытка номер 3...")
        await GameAttempts.A3.set()


async def handle_a3_answer(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == random_number:
        await message.answer("🎊 🎊 🎊 Поздравляю, ты всё таки угадал! Чем займёмся дальше?")
        await state.finish()
    else:
        await message.answer("🥲 К сожалению снова не верно. Ничего, в следующий раз обязательно повезёт. Выбери "
                             "другую функцию...")
        await state.finish()


def register_game_handlers(dp: Dispatcher):
    dp.register_message_handler(start_guess_number, commands=['Игра_угадай_число🎲'])
    dp.register_message_handler(handle_a1_answer, state=GameAttempts.A1)
    dp.register_message_handler(handle_a2_answer, state=GameAttempts.A2)
    dp.register_message_handler(handle_a3_answer, state=GameAttempts.A3)




