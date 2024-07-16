from aiogram import Router, F, types
from aiogram.filters.command import Command

from bot_config import database

shop_router = Router()


@shop_router.message(Command("shop"))
async def show_genres(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Детектив")
            ],
            [
                types.KeyboardButton(text="фантастика"),
                types.KeyboardButton(text="триллер")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(
        text="Выберите жанр книг",
        reply_markup=kb
    )


@shop_router.message(F.text.lower() == "детектив")
async def horror_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = """
        SELECT books.*, genres.name FROM books 
        JOIN genres ON genres.id=books.genre_id
        WHERE genres.name = ?
    """
    genre = 'детектив'

    books = database.fetch(
        query=sqlquery,
        params=(genre,)
    )
    print(books)
    await message.answer("Книги жанра детектив", reply_markup=kb)
    for book in books:
        await message.answer(f"Название: book[1]\nЦена: book[2")

@shop_router.message(F.text.lower() == "фантастика")
async def fantasy_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Книги жанра фантастика", reply_markup=kb)