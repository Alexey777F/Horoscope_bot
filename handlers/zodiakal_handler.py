from aiogram.types import CallbackQuery, Message
from keyboard.keyboard import keyboard, menu_button
from config.config import zodiaks, dates, dp, bot, menu, space_list
from request.request import get_url, get_data, get_response
# from photos_dark.photo_redactor import abs_path, image_redactor
# import asyncio
from keyboard.paginator import send_page
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Zodiacal(StatesGroup):
    zodiac_name = State()
    date_name = State()
    pagination_page = State()


@dp.callback_query_handler(text=["Зодиакальный 🕉"])
async def zodiak_inline_keyboard(call: CallbackQuery):
    """Колбек-хендлер который ловит кнопку Зодиакальный 🕉"""
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await Zodiacal.zodiac_name.set()
    await call.message.answer("Выберите знак зодиака 💟", reply_markup=keyboard(3, zodiaks, 12, space_list()))


@dp.message_handler(lambda message: message.text, state=Zodiacal.zodiac_name)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                                  reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Выберите знак зодиака кнопкой 📱")


@dp.callback_query_handler(state=Zodiacal.zodiac_name, text=[key for key in zodiaks().keys()])
async def date_inline_keyboard(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку из инлайн клавиатуры со знаками зодиака"""
    # Ловим колбэк от нажатия кнопки
    zodiak_sign = call.data
    # Сохраняем в машину состояний данные
    async with state.proxy() as user_data:
        user_data["Знак зодиака"] = zodiaks()[zodiak_sign]
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    # Переключаемся на следующее состояние
    await Zodiacal.next()
    # Отправляем клавиатуру с датами
    await call.message.answer(zodiak_sign, reply_markup=keyboard(1, dates, 5, space_list()))
    await call.answer()


@dp.message_handler(lambda message: message.text, state=Zodiacal.date_name)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Выберите дату кнопкой 📱")

@dp.callback_query_handler(state=Zodiacal.date_name, text=["Сегодня 📆", "Завтра 📆", "Неделя 📆"])
async def request_answer(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку из инлайн клавиатуры с выбором периода"""
    # Ловим колбэк от нажатия кнопки
    date = call.data
    # Сохраняем в машину состояний данные
    async with state.proxy() as user_data:
        user_data["Дата"] = dates()[date]
    # Получаем url для передачи в запрос
    url = get_url("prediction", user_data["Знак зодиака"], user_data["Дата"])
    # Получаем запрос(список с нашим текстом из сайта)
    request = get_data(get_response(url))
    await bot.edit_message_reply_markup(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    await call.message.answer(f"Вы выбрали {date.lower()}")
    # вариант отправки отдельно картинки и отдельно текст
    # показался мне более читабельным по сравнению со вторым
    # Отправляем картинку из папки
    await call.message.answer_photo(open(f"photos_light/{user_data['Знак зодиака']}.jpeg", "rb"))
    # Отправляем страницу текста с пагинацией
    await call.message.answer("\n".join(request).replace("&ndash;", " ").replace("&nbsp;", " "), reply_markup=menu_button())
    # Переключаемся на следующее состояние
    await Zodiacal.next()
    await call.answer()


@dp.callback_query_handler(state=Zodiacal.date_name, text=["Месяц 📆", "Год 📆"])
async def request_answer(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку из инлайн клавиатуры с выбором периода"""
    # Ловим колбэк от нажатия кнопки
    date = call.data
    # Сохраняем в машину состояний данные
    async with state.proxy() as user_data:
        user_data["Дата"] = dates()[date]
    # Получаем url для передачи в запрос
    url = get_url("prediction", user_data["Знак зодиака"], user_data["Дата"])
    # Получаем запрос(список с нашим текстом из сайта)
    request = get_data(get_response(url))
    request_filtred = "\n".join(request).replace("&ndash;", " ").replace("&nbsp;", " ").split("\n")
    await bot.edit_message_reply_markup(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    await call.message.answer(f"Вы выбрали {date.lower()}")
    # вариант отправки отдельно картинки и отдельно текст
    # показался мне более читабельным по сравнению со вторым
    # Отправляем картинку из папки
    await call.message.answer_photo(open(f"photos_light/{user_data['Знак зодиака']}.jpeg", "rb"))
    # Отправляем страницу текста с пагинацией
    await send_page(request_filtred, call.message)
    # Переключаемся на следующее состояние
    await Zodiacal.next()
    await call.answer()
    # for i in range(len(data)):
    #     await call.message.answer(data[i].replace("&ndash;", "").replace("&nbsp;", ""))
    # вариант отправки картинки с текстом, подключаем модуль photo_redactor
    # image_redactor(abs_path, user_data["Знак зодиака"], data, 20)
    # await asyncio.sleep(0.5)
    # await call.message.answer_photo(open(f"photo_with_text/{user_data['Знак зодиака']}.jpeg", "rb"))
    # await Zodiacal.next()
    # await call.answer()


@dp.message_handler(lambda message: message.text, state=Zodiacal.pagination_page)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Нажмите на кнопку - 'Перейти в главное меню 🌟'")


@dp.callback_query_handler(lambda call: True, state=Zodiacal.pagination_page)
async def pagination_callback(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку пагинации из клавиатуры под текстом"""
    # Ловим наши цифры от кнопок пагинации
    if call.data in [str(i) for i in range(1, 12)]:
        page = int(call.data)
        # Сохраняем данные в машину состояний
        async with state.proxy() as user_data:
            user_data["Пагинация"] = page
        url = get_url("prediction", user_data["Знак зодиака"], user_data["Дата"])
        request = get_data(get_response(url))
        request_filtred = "\n".join(request).replace("&ndash;", " ").replace("&nbsp;", " ").split("\n")
        # Удаляет предыдущую страницу выдачи информации(страничка пагинации)
        # чтобы текст заменялся, а не присылался следующим сообщением
        await bot.delete_message(
            call.message.chat.id,
            message_id=call.message.message_id
        )
        # Отправляем следующую страницу пагинации
        await send_page(request_filtred, call.message, page)
        await call.answer()
    # Отлавливаем команду "Завершить просмотр", чтобы завершить машинное состояние в данном разделе
    # и чтобы мы могли переключиться на другой раздел
    elif call.data == "Меню":
        # Завершаем и сбрасываем все состояния машины чтобы можно было переключится на другой раздел или выбрать тот же
        await state.finish()
        await call.message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                                  reply_markup=keyboard(1, menu, 6, space_list()))
        await call.answer()
