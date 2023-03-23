import logging
from globals import dp, executor
from handlers import handler, game_handler


handler.register_user_handlers(dp)
game_handler.register_game_handlers(dp)
logging.basicConfig(level = logging.INFO)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)