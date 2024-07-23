from aiogram import Router, types
from aiogram.filters.command import Command
from my_parser.mashina_kg import MashinaParser


mashina_router = Router()


@mashina_router.message(Command("show_cars"))
async def show_car_links(message: types.Message):
    mashina_parser = MashinaParser()
    mashina_parser.get_page()
    links = mashina_parser.get_car_links()
    print(links)
    for link in links:
        await message.answer(link)

