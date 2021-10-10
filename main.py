import logging
from aiogram import executor
from handlers import *

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# callbackData = CallbackData('option', 'choosen')
# inline_btn_1 = types.InlineKeyboardButton(text='1', callback_data=callbackData.new(choosen='1'))
# inline_btn_2 = types.InlineKeyboardButton(text='2', callback_data=callbackData.new(choosen='2'))
# inline_btn_3 = types.InlineKeyboardButton(text='3', callback_data=callbackData.new(choosen='3'))
# inline_btn_4 = types.InlineKeyboardButton(text='4', callback_data=callbackData.new(choosen='4'))
# inline_btn_1 = types.InlineKeyboardButton(text='1', callback_data='1')
# inline_btn_2 = types.InlineKeyboardButton(text='2', callback_data='2')
# inline_btn_3 = types.InlineKeyboardButton(text='3', callback_data='3')
# inline_btn_4 = types.InlineKeyboardButton(text='4', callback_data='4')
#
# inline_keyboard_markup = types.InlineKeyboardMarkup(row_width=2,
#                                                     inline_keyboard=[[inline_btn_1, inline_btn_2],
#                                                                      [inline_btn_3, inline_btn_4]])
# answers = ['Kanagat', 'Ainur', 'Symbat', 'Makset']
# correct_ans = 'Makset'
# shuffled_list = random.sample(answers, len(answers))
#
#
# @dp.message_handler(commands=['start'])
# async def starting(message: types.Message):
#     await message.answer(text='if you are ready to start test, then click /test 😇😇😇')
#
#
# @dp.message_handler(commands=['test'])
# async def start_testing(message: types.Message):
#     await message.answer(
#         text=f'1. {shuffled_list[0]}\n'
#              f'2. {shuffled_list[1]}\n'
#              f'3. {shuffled_list[2]}\n'
#              f'4. {shuffled_list[3]}',
#         reply_markup=inline_keyboard_markup
#     )
#
#
# @dp.callback_query_handler(lambda call: call.data in ['1', '2', '3', '4'])
# async def processing_callback(callback: types.CallbackQuery):
#     await callback.message.answer('You have answered')
#     # await bot.send_message(
#     #     chat_id=callback.message.chat.id,
#     #     text=shuffled_list[int(callback.data)-1]
#     # )
