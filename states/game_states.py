from aiogram.dispatcher.filters.state import State, StatesGroup


class GameAttempts(StatesGroup):
    A1 = State()
    A2 = State()
    A3 = State()