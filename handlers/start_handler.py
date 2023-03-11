from config.config import dp
from aiogram.types import Message
from keyboard.keyboard import keyboard
from config.config import menu, space_list


@dp.message_handler(commands=["start"])
async def zodiak_inline_keyboard(message: Message):
    """Функция-приветствие, реагирует на команду старт"""
    await message.answer("Приветствую Вас в Гороскоп боте👋\n\n"
                         "Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n"
                         "Для выбора раздела зайдите в меню", reply_markup=keyboard(1, menu, 6, space_list()))
