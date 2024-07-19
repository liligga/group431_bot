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


GENRES = ("детектив", "фантастика", "триллер")

@shop_router.message(F.text.lower().in_(GENRES))
async def horror_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = """
        SELECT books.*, genres.name FROM books 
        JOIN genres ON genres.id=books.genre_id
        WHERE genres.name = ?
    """
    genre = message.text.lower()
    print("Genre    ", genre)

    books = database.fetch(
        query=sqlquery,
        params=(genre,)
    )
    print(books)
    if not books:
        await message.answer("К сожалению нет книг этого жанра")

    await message.answer(f"Книги жанра {genre}", reply_markup=kb)
    for book in books:
        photo=types.FSInputFile(book.get('cover'))
        # await message.answer(f"Название:{book.get('name')}\nЦена: {book.get('price')}")
        await message.answer_photo(
            photo=photo,
            caption=f"Название:{book.get('name')}\nЦена: {book.get('price')}"
        )