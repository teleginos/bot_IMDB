from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def generator_inline(key_list):
    buttons = [[]]
    for move in key_list:
        buttons[-1].append(InlineKeyboardButton(text=f'{move["rank"]} : {move["title"]}',
                                                callback_data=str(move["rank"])))
        buttons.append([])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard
