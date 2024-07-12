import asyncio
import logging

from aiogram import Bot
from bot_config import dp, bot, database
from handlers.start import start_router
from handlers.shop import shop_router
from handlers.echo import echo_router
from handlers.pictures import picture_router
from handlers.survey import survey_router


async def on_startup(bot: Bot):
    database.create_tables()


async def main():
    # регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(survey_router)
    dp.include_router(shop_router)
    dp.include_router(picture_router)

    # в самом конце
    dp.include_router(echo_router)
    # при запуске
    dp.startup.register(on_startup)

    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())