from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')

@dp.message_handler(text=['Calories', 'calories', 'Калории', 'калории'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_height(message, state):
    await state.update_data(age = message.text)
    #users_data = await state.get_data()
    await message.answer('Введите свой рост в см:')
    await UserState.height.set()

@dp.message_handler(state = UserState.height)
async def set_weight(message, state):
    await state.update_data(height = message.text)
    #users_data = await state.get_data()
    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()


@dp.message_handler(state = UserState.weight)
async def set_weight(message, state):
    await state.update_data(weight = message.text)
    users_data = await state.get_data()
    calories = 10 * float(users_data["weight"]) + 6.25 * float(users_data["height"]) - 5 * int(users_data["age"]) + 5
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()
@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)