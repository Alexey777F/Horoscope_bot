from telegram_bot_pagination import InlineKeyboardPaginator, InlineKeyboardButton
from config.config import bot


async def send_page(text, message, page=1):
    """Функция разбивает список текста на страницы"""
    paginator = InlineKeyboardPaginator(
        len(text),
        current_page=page,
        data_pattern='{page}',
    )
    paginator.add_after(InlineKeyboardButton("Перейти в главное меню 🌟", callback_data="Меню"))
    await bot.send_message(
        message.chat.id,
        text[page - 1],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )