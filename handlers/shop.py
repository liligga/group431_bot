from aiogram import Router, F, types


shop_router = Router()


@shop_router.message(F.text == "хоррор")
async def horror_handler(message: types.Message):
    await message.answer("Книги жанра хоррор")


@shop_router.message(F.text == "фантастика")
async def fantasy_handler(message: types.Message):
    await message.answer("Книги жанра фантастика")