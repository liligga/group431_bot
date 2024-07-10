from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


survey_router = Router()


# FSM - Finite State Machine
class BookSurvey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    genre = State()


@survey_router.message(Command("opros"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.name)
    await message.answer("Как Вас зовут?")


@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    print(message.text)
    await state.update_data(name=message.text)
    await state.set_state(BookSurvey.age)
    await message.answer("Сколько Вам лет?")


@survey_router.message(BookSurvey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Вводите только цифры")
        return
    age = int(age)
    if age < 12 or age > 90:
        await message.answer("Некорректный возраст")
        return
    await state.set_state(BookSurvey.gender)
    await state.update_data(age=message.text)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Мужской"),
                types.KeyboardButton(text="Женский")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Укажите Ваш пол?", reply_markup=kb)


@survey_router.message(BookSurvey.gender)
async def process_gender(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    await state.set_state(BookSurvey.genre)
    await state.update_data(gender=message.text)
    await message.answer("Укажите Ваш любимый жанр?", reply_markup=kb)


@survey_router.message(BookSurvey.genre)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    data = await state.get_data()
    print(data)
    await state.clear()
    await message.answer("Спасибо за пройденный опрос")