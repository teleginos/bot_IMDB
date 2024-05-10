from aiogram import F, Router, types


router = Router()


@router.message(F.text.lower() == "топ 100 сериалов")
async def choice_key_series(message: types.Message):
    await message.answer('Выбор сериала')
