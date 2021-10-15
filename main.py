import logging
from aiogram import executor
from handlers import *
from db.services import create_db

logging.basicConfig(level=logging.INFO)


async def on_startup(dp):
    """ Данный код исполняется после запуска """
    create_db()
    print('[-] Database created [-]')


async def on_shutdown(dp):
    """ Данный код исполняется перед падением """
    await dp.storage.close()
    await dp.storage.wait_closed()
    print('[-] Bot was shutdown [-]')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
