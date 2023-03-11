from config.config import dp
from aiogram.types import Message


@dp.message_handler(state=None)
async def bot_echo(message: Message) -> None:
    """Эхо хендлер который ловит сообщения без команд"""
    await message.answer("Я Вас не понимаю, воспользуйтесь кнопками📱")