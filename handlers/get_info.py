from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text

from state import FSMteacher
from loader import dp


@dp.message_handler(state="*", commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
async def cancel_state(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('OK')


@dp.message_handler(commands=['register_teacher'], state=None)
async def start_state(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(str(data))
    await FSMteacher.first_name.set()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_button = types.KeyboardButton(text='cancel')
    keyboard.add(cancel_button)
    await message.reply(f'Dear, {message.from_user.username} enter your first name', reply_markup=keyboard)


@dp.message_handler(state=FSMteacher.first_name)
async def get_first_name(message: types.Message, state: FSMContext):
    if len(message.text.split()) > 1:
        await message.answer("Please enter just first name")
    else:
        async with state.proxy() as data:
            data['first_name'] = message.text.strip()
        await FSMteacher.next()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cancel_button = types.KeyboardButton(text='cancel')
        keyboard.add(cancel_button)
        await message.reply('Enter last name', reply_markup=keyboard)


@dp.message_handler(state=FSMteacher.last_name)
async def get_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text.strip()
    await FSMteacher.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_button = types.KeyboardButton(text='cancel')
    keyboard.add(cancel_button)
    await message.reply('Enter quiz title', reply_markup=keyboard)


@dp.message_handler(state=FSMteacher.quiz_title)
async def get_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quiz_title'] = message.text.strip()
        print(data)
    await state.reset_state(with_data=False)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel_button = types.KeyboardButton(text='cancel')
    keyboard.add(cancel_button)
    await message.answer('Thanks', reply_markup=keyboard)
