from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    # print(message.from_user)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
            ],
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/geeks.kg"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us"),
            ],
            [
                types.InlineKeyboardButton(text="Пожертвуйте нам", callback_data="donate_us"),
            ]
        ]
    )
    await message.answer(
        text=f"Привет, {message.from_user.first_name},  я бот, который поможет вам выбрать и купить книгу в нашем магазине.", 
        reply_markup=kb
    )


@start_router.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.message.answer("О нас")


@start_router.callback_query(F.data == "donate_us")
async def donate_us(callback: types.CallbackQuery):
    await callback.message.answer("Спасибо за поддержку! ")