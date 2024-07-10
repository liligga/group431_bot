from aiogram import Router, F, types
from aiogram.filters.command import Command


shop_router = Router()


@shop_router.message(Command("shop"))
async def show_genres(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Фантастика")
            ],
            [
                types.KeyboardButton(text="Хоррор"),
                types.KeyboardButton(text="Драма")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(
        text="Выберите жанр книг",
        reply_markup=kb
    )


@shop_router.message(F.text.lower() == "хоррор")
async def horror_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Книги жанра хоррор", reply_markup=kb)


@shop_router.message(F.text.lower() == "фантастика")
async def fantasy_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Книги жанра фантастика", reply_markup=kb)