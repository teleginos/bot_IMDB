from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from api import get_movies
from keyboard.inline.generator_inline import generator_inline
from states.state import GetMovie

router = Router()

result_get_movies = []

if not result_get_movies:
    result_get_movies = get_movies.response


@router.message(F.text.lower() == "топ 100 фильмов")
async def choice_key_movies(message: types.Message, state: FSMContext):
    inline_keyboard_movies = await generator_inline(result_get_movies)
    await message.answer('Выбор фильмов', reply_markup=inline_keyboard_movies)
    await state.set_state(GetMovie.movie)


@router.callback_query(GetMovie.movie)
async def button_movie_click_handler(query: types.CallbackQuery):
    button_text = query.data
    movie = result_get_movies[int(button_text) - 1]

    await query.message.answer_photo(movie['image'])
    await query.message.answer(f"<em>{movie['title']}</em>\n\n"
                               f"<b>Description</b>: {movie['description']}\n"
                               f"<b>Genre</b>: {', '.join(movie['genre'])}\n"
                               f"<b>Rating</b>: {movie['rating']}\n"
                               f"<b>Year</b>: {movie['year']}", parse_mode=ParseMode.HTML)
