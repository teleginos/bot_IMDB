from aiogram import F, Router, types

from keyboard.inline.generator_inline import generator_inline
from api import get_movies
from aiogram.enums import ParseMode


router = Router()

result_get_movies = []

if not result_get_movies:
    result_get_movies = get_movies.response


@router.message(F.text.lower() == "топ 100 фильмов")
async def choice_key_movies(message: types.Message):
    keyboard = await generator_inline(result_get_movies)
    await message.answer('Выбор фильмов', reply_markup=keyboard)


@router.callback_query()
async def button_click_handler(query: types.CallbackQuery):
    button_text = query.data
    movie = result_get_movies[int(button_text) - 1]

    await query.message.answer_photo(movie['image'])
    await query.message.answer(f"<em>{movie['title']}</em>\n\n"
                               f"<b>Description</b>: {movie['description']}\n"
                               f"<b>Genre</b>: {', '.join(movie['genre'])}\n"
                               f"<b>Rating</b>: {movie['rating']}\n"
                               f"<b>Year</b>: {movie['year']}", parse_mode=ParseMode.HTML)



