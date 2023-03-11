from aiogram.types import Message, CallbackQuery
from config.config import dp, bot, menu, gender, space_list, zodiaks, zodiaks_compability
from keyboard.paginator import send_page
from keyboard.keyboard import keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.db import return_history


class Compatibility(StatesGroup):
    gender_choice = State()
    #Для мужчин
    first_zodiac_name = State()
    second_zodiac_name = State()
    pagination_page = State()
    #Для женщин
    w_first_zodiac_name = State()
    w_second_zodiac_name = State()
    w_pagination_page = State()


@dp.callback_query_handler(text=["Гороскоп совместимости 🎎"])
async def druid_inline_keyboard(call: CallbackQuery):
    """Колбек-хендлер который ловит кнопку Гороскоп совместимости 🎎"""
    await Compatibility.gender_choice.set()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("Гороскоп совместимости по знакам Зодиака 🕉\n\n" \
                                "Астрология совместимости всегда вызывает огромный интерес. " \
                                "Знание основных принципов, согласно которым складываются отношения " \
                                "в паре, поможет понять, что чувствует любимый человек, как себя вести, " \
                                "чтобы удовольствие от общения было взаимным 💫\n\nСовместимость по знакам " \
                                "Зодиака не гарантирует любви в паре; но именно благодаря ей влюбленные " \
                                "достигают гармонии 🌟\n\nПроверка совместимости по знакам Зодиака позволяет " \
                                "определить, в чем кроются истинные проблемы пары, найти пути их решения и " \
                                "сохранить силу чувств 💞")
    await call.message.answer("Выберите Ваш пол", reply_markup=keyboard(2, gender, 2, space_list()))


@dp.message_handler(lambda message: message.text, state=Compatibility.gender_choice)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(state=Compatibility.gender_choice, text=["Мужчина👨‍🦱"])
async def what_is_my_zodiac_sign(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку Мужчина👨‍🦱"""
    gender = call.data
    async with state.proxy() as user_data:
        user_data["1й Пол"] = gender
    async with state.proxy() as user_data:
        user_data["2й Пол"] = "Женщина👩🏻"
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await Compatibility.next()
    await call.message.answer("Выберите знак зодиака для Мужчины👨‍🦱", reply_markup=keyboard(3, zodiaks, 12, space_list()))
    await call.answer()


@dp.message_handler(lambda message: message.text, state=Compatibility.first_zodiac_name)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(state=Compatibility.first_zodiac_name, text=[key for key in zodiaks().keys()])
async def date_inline_keyboard(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку из инлайн клавиатуры со знаками зодиака"""
    # Ловим колбэк от нажатия кнопки
    zodiak_sign = call.data
    # Сохраняем в машину состояний данные
    async with state.proxy() as user_data:
        user_data["1й Знак зодиака"] = zodiaks_compability()[zodiak_sign]
    async with state.proxy() as user_data:
        user_data["1й Zod"] = zodiak_sign
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    # Переключаемся на следующее состояние
    await Compatibility.next()
    await call.message.answer("Выберите знак зодиака для Женщины👩🏻", reply_markup=keyboard(3, zodiaks, 12, space_list()))
    await call.answer()


@dp.message_handler(lambda message: message.text, state=Compatibility.second_zodiac_name)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(state=Compatibility.second_zodiac_name, text=[key for key in zodiaks().keys()])
async def date_inline_keyboard(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку из инлайн клавиатуры со знаками зодиака"""
    zodiak_sign = call.data
    async with state.proxy() as user_data:
        user_data["2й Знак зодиака"] = zodiaks_compability()[zodiak_sign]
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(f"Вы выбрали:\n\nМужчина - {user_data['1й Zod']}\nЖенщина - {zodiak_sign}")
    await send_page(return_history(f'{user_data["2й Знак зодиака"]}_{user_data["1й Знак зодиака"]}')[0][0].split("\n"), call.message)
    await Compatibility.next()
    await call.answer()


@dp.message_handler(lambda message: message.text, state=Compatibility.pagination_page)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(lambda call: True, state=Compatibility.pagination_page)
async def pagination_callback(call: CallbackQuery, state: FSMContext):
    if call.data in [str(i) for i in range(1, 12)]:
        page = int(call.data)
        async with state.proxy() as user_data:
            user_data["Пагинация"] = page
        await bot.delete_message(
            call.message.chat.id,
            call.message.message_id
        )
        await send_page(return_history(f'{user_data["2й Знак зодиака"]}_{user_data["1й Знак зодиака"]}')[0][0].split("\n"), call.message, page)
        await call.answer()
    elif call.data == "Меню":
        # Удаляем текст с пагинацией
        await bot.delete_message(
            call.message.chat.id,
            message_id=call.message.message_id
        )
        # Завершаем и сбрасываем все состояния машины чтобы можно было переключится на другой раздел или выбрать тот же
        await state.finish()
        await call.message.answer("Узнай что говорят звёзды и приготовила тебе судьба✨💫🌟\n\n",
                                  reply_markup=keyboard(1, menu, 6, space_list()))
        await call.answer()


@dp.callback_query_handler(state=Compatibility.gender_choice, text=["Женщина👩🏻"])
async def what_is_my_zodiac_sign(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку Женщина👩🏻"""
    await state.finish()
    gender = call.data
    async with state.proxy() as user_data:
        user_data["1й Пол"] = gender
    async with state.proxy() as user_data:
        user_data["2й Пол"] = "Мужчина👨‍🦱"
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await Compatibility.w_first_zodiac_name.set()
    await call.message.answer("Выберите знак зодиака для Женщины👩🏻", reply_markup=keyboard(3, zodiaks, 12, space_list()))
    await call.answer()


@dp.message_handler(lambda message: message.text, state=Compatibility.w_first_zodiac_name)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(state=Compatibility.w_first_zodiac_name, text=[key for key in zodiaks().keys()])
async def date_inline_keyboard(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку из инлайн клавиатуры со знаками зодиака"""
    # Ловим колбэк от нажатия кнопки
    zodiak_sign = call.data
    # Сохраняем в машину состояний данные
    async with state.proxy() as user_data:
        user_data["1й Знак зодиака"] = zodiaks_compability()[zodiak_sign]
    async with state.proxy() as user_data:
        user_data["1й Zod"] = zodiak_sign
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    # Переключаемся на следующее состояние
    await Compatibility.w_second_zodiac_name.set()
    await call.message.answer("Выберите знак зодиака для Мужчины👨‍🦱", reply_markup=keyboard(3, zodiaks, 12, space_list()))
    await call.answer()


@dp.message_handler(lambda message: message.text, state=Compatibility.w_second_zodiac_name)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(state=Compatibility.w_second_zodiac_name, text=[key for key in zodiaks().keys()])
async def date_inline_keyboard(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку из инлайн клавиатуры со знаками зодиака"""
    zodiak_sign = call.data
    async with state.proxy() as user_data:
        user_data["2й Знак зодиака"] = zodiaks_compability()[zodiak_sign]
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(f"Вы выбрали:\n\nЖенщина - {user_data['1й Zod']}\nМужчина - {zodiak_sign}")
    await send_page(
        return_history(f'{user_data["1й Знак зодиака"]}_{user_data["2й Знак зодиака"]}')[0][0].split("\n"),
        call.message)
    await Compatibility.w_pagination_page.set()
    await call.answer()


@dp.message_handler(lambda message: message.text, state=Compatibility.w_pagination_page)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(lambda call: True, state=Compatibility.w_pagination_page)
async def pagination_callback(call: CallbackQuery, state: FSMContext):
    if call.data in [str(i) for i in range(1, 12)]:
        page = int(call.data)
        async with state.proxy() as user_data:
            user_data["Пагинация"] = page
        await bot.delete_message(
            call.message.chat.id,
            call.message.message_id
        )
        await send_page(
            return_history(f'{user_data["1й Знак зодиака"]}_{user_data["2й Знак зодиака"]}')[0][0].split("\n"),
            call.message, page)
        await call.answer()
    elif call.data == "Меню":
        # Удаляем текст с пагинацией
        await bot.delete_message(
            call.message.chat.id,
            message_id=call.message.message_id
        )
        # Завершаем и сбрасываем все состояния машины чтобы можно было переключится на другой раздел или выбрать тот же
        await state.finish()
        await call.message.answer("Узнай что говорят звёзды и приготовила тебе судьба✨💫🌟\n\n",
                                  reply_markup=keyboard(1, menu, 6, space_list()))
        await call.answer()