from aiogram import F, Router, types

from keyboard.reply.generator_reply import generator_reply

router = Router()


@router.message(F.text == '/start')
async def start_handlers(message: types.Message):
    keyboard = await generator_reply(['Топ 100 фильмов', 'Топ 100 сериалов'], 2)
    await message.answer("Этот бот расскажет Вам про 100 лучших фильмов и сериалов по рейтингу IMDB",
                         reply_markup=keyboard)
