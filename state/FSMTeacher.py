from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMteacher(StatesGroup):
    first_name = State()
    last_name = State()
    quiz_title = State()
