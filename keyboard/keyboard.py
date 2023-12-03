from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard(row, name, number, text=None) -> InlineKeyboardMarkup:
    """Универсальная функция которая присылает клавиатуру"""
    keyboard = InlineKeyboardMarkup(row_width=row)
    btns = [key for key in name().keys()]
    buttons = [InlineKeyboardButton(text=f"{btns[i]} {text[i]}", callback_data=f"{btns[i]}") for i in range(number)]
    keyboard.add(*buttons)
    return keyboard


def menu_button() -> InlineKeyboardMarkup:
    """Функция кнопки клавиатуры меню"""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Перейти в главное меню 🌟", callback_data="Меню"))
    return keyboard

