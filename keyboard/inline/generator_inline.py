import asyncio

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# from api import get_movies, get_series


async def generator_inline(key_list):
    buttons = [[]]
    for move in key_list:
        buttons[-1].append(InlineKeyboardButton(text=f'{move["rank"]} : {move["title"]}',
                                                callback_data=str(move["rank"])))
        buttons.append([])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


# if __name__ == "__main__":
    # print(asyncio.run(generator_inline(result_get_movies)))
