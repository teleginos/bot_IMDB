import asyncio

from handlers import handlers_movies, handlers_series, start_and_help
from loader import bot, dp


async def main():
    dp.include_router(start_and_help.router)
    dp.include_router(handlers_movies.router)
    dp.include_router(handlers_series.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
