from aiogram.fsm.state import State, StatesGroup


class GetMovie(StatesGroup):
    movie = State()
    series = State()
