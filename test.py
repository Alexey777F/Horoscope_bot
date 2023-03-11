# from aiogram.types import Message, CallbackQuery
# from keyboard.keyboard import keyboard
# from config.config import zodiaks, dates, dp, bot
# from request.request import get_url, get_data, get_response
# # from photos_dark.photo_redactor import abs_path, image_redactor
# # import asyncio
# from keyboard.paginator import send_page
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text
# from aiogram.dispatcher.filters.state import State, StatesGroup
from typing import Dict, List
#
# class Zodiacal(StatesGroup):
#     chapter_name = State()
#     zodiac_name = State()
#     date_name = State()
#
#
# @dp.message_handler(commands=["zodiac"])
# async def zodiak_inline_keyboard(message: Message):
#     await message.answer("Выберите знак зодиака 💟", reply_markup=keyboard(3, zodiaks, 12))
#
#
# user_data = dict()
#
#
# @dp.callback_query_handler(text=[key for key in zodiaks().keys()])
# async def date_inline_keyboard(call: CallbackQuery):
#     zodiak_sign = call.data
#     user_data["Знак зодиака"] = zodiaks()[zodiak_sign]
#     await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
#                                         reply_markup=None)
#     await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
#     await call.message.answer(zodiak_sign, reply_markup=keyboard(1, dates, 5))
#     await call.answer()
#
#
# @dp.callback_query_handler(text=[key for key in dates().keys()])
# async def request_answer(call: CallbackQuery):
#     date = call.data
#     user_data["Дата"] = dates()[date]
#     url = get_url("prediction", user_data["Знак зодиака"], user_data["Дата"])
#     data = get_data(get_response(url))
#     await bot.edit_message_reply_markup(
#         chat_id=call.from_user.id,
#         message_id=call.message.message_id,
#         reply_markup=None
#     )
#     await call.message.answer(f"Вы выбрали {date.lower()}")
#     # вариант отправки отдельно картинки и отдельно текст
#     # показался мне более читабельным по сравнению со вторым
#     await call.message.answer_photo(open(f"photos_light/{user_data['Знак зодиака']}.jpeg", "rb"))
#     await send_page(data, call.message)
#
#     # for i in range(len(data)):
#     #     await call.message.answer(data[i].replace("&ndash;", "").replace("&nbsp;", ""))
#     # вариант отправки картинки с текстом, подключаем модуль photo_redactor
#     # image_redactor(abs_path, user_data["Знак зодиака"], data, 20)
#     # await asyncio.sleep(0.5)
#     # await call.message.answer_photo(open(f"photo_with_text/{user_data['Знак зодиака']}.jpeg", "rb"))
#     await call.answer()
#
#
# @dp.callback_query_handler()
# async def characters_page_callback(call: CallbackQuery):
#     url = get_url("prediction", user_data["Знак зодиака"], user_data["Дата"])
#     data = get_data(get_response(url))
#     page = int(call.data.split('#')[1])
#     await bot.delete_message(
#         call.message.chat.id,
#         call.message.message_id
#     )
#     await send_page(data, call.message, page)
#     await call.answer()
