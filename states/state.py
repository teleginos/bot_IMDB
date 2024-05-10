from aiogram.fsm.state import StatesGroup, State


class GetMovie(StatesGroup):
    movie = State()
