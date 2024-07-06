from aiogram import Router, types
from aiogram.filters.command import Command


picture_router = Router()


@picture_router.message(Command("picture"))
async def picture_handler(message: types.Message):
    image = types.FSInputFile("images/book1.jpg")
    await message.answer_photo(
        photo=image,
        caption="Интереснейшая книга"
    )