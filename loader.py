from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2

storage = RedisStorage2()
bot = Bot(token='2043418404:AAHxxpqaVEnboCKIxx7ZtB_sjtB0ccrj8xk', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
