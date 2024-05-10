from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from api import get_series
from keyboard.inline.generator_inline import generator_inline
from states.state import GetMovie

router = Router()

result_get_series = []

if not result_get_series:
    result_get_series = get_series.response


@router.message(F.text.lower() == "топ 100 сериалов")
async def choice_key_series(message: types.Message, state: FSMContext):
    inline_keyboard_series = await generator_inline(result_get_series)
    await message.answer('Выбор сериала', reply_markup=inline_keyboard_series)
    await state.set_state(GetMovie.series)


@router.callback_query(GetMovie.series)
async def button_series_click_handler(query: types.CallbackQuery):
    button_text = query.data
    series = result_get_series[int(button_text) - 1]

    await query.message.answer_photo(series['image'])
    await query.message.answer(f"<em>{series['title']}</em>\n\n"
                               f"<b>Description</b>: {series['description']}\n"
                               f"<b>Genre</b>: {', '.join(series['genre'])}\n"
                               f"<b>Rating</b>: {series['rating']}\n"
                               f"<b>Year</b>: {series['year']}", parse_mode=ParseMode.HTML)
