from aiogram.types import CallbackQuery, Message
from keyboard.keyboard import keyboard
from config.config import chinese, dp, bot, menu, choice_zodiac, zodiak_name_list, zodiac_date_list, my_zodiac_year, space_list
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard.paginator import send_page
from database.db import return_history


class Chinese(StatesGroup):
    zodiac_choice = State()
    birtday_choice = State()
    zodiac_name = State()
    pagination_page = State()


@dp.callback_query_handler(text=["Китайский 🈯"])
async def chinese_inline_keyboard(call: CallbackQuery):
    """Колбек-хендлер который ловит кнопку Китайский 🈯"""
    await Chinese.zodiac_choice.set()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("Выберите интересующий раздел", reply_markup=keyboard(1, choice_zodiac, 2, space_list()))


@dp.message_handler(lambda message: message.text, state=Chinese.zodiac_choice)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(state=Chinese.zodiac_choice, text=["Определите Мой Знак Зодиака ❓"])
async def what_is_my_zodiac_sign(call: CallbackQuery):
    """Колбек-хендлер который ловит кнопку "Определите Мой Знак Зодиака ❓"""
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("Введите год Своего Рождения")
    await Chinese.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=Chinese.birtday_choice)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который проверяет являются ли введенные данные числом"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнай что говорят звёзды и приготовила тебе судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Возраст является числом! Введите корректные данные")


@dp.message_handler(lambda message: not 3 < len(message.text) < 5 and message.text.isdigit() or not 1935 < int(message.text) < 2024 and message.text.isdigit(), state=Chinese.birtday_choice)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который проверяет корректность даты рождения"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Вряд ли Вы родились в этом году)")


@dp.message_handler(lambda message: 3 < len(message.text) < 5 and message.text.isdigit() and 1935 < int(message.text) < 2024, state=Chinese.birtday_choice)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который принимает корректную дату рождения"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.answer(f"Вы родились в {my_zodiac_year(message.text, zodiac_date_list(), zodiak_name_list())}")
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                                  reply_markup=keyboard(1, menu, 6, space_list()))


@dp.callback_query_handler(state=Chinese.zodiac_choice, text=["Я знаю Свой Знак Зодиака 💯"])
async def i_know_my_zodiac_sign(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку Я знаю Свой Знак Зодиака 💯"""
    await state.finish()
    await Chinese.zodiac_name.set()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("Выберите тотемное животное 🕉", reply_markup=keyboard(3, chinese, 12, space_list()))


@dp.message_handler(lambda message: message.text, state=Chinese.zodiac_name)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(state=Chinese.zodiac_name, text=[key for key in chinese().keys()])
async def date_inline_keyboard(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку из инлайн клавиатуры с тотемными животными"""
    animal = call.data
    async with state.proxy() as user_data:
        user_data["Тотемное животное"] = chinese()[animal]
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(f"Вы выбрали {animal.lower()}")
    await call.message.answer_photo(open(f"photos_light/{user_data['Тотемное животное']}.jpeg", "rb"))
    await send_page(return_history(f'{user_data["Тотемное животное"]}_chinese')[0][0].split("\n"), call.message)
    await Chinese.next()
    await call.answer()


@dp.message_handler(lambda message: message.text, state=Chinese.pagination_page)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Нажмите на кнопку - 'Перейти в главное меню 🌟'")


@dp.callback_query_handler(lambda call: True, state=Chinese.pagination_page)
async def pagination_callback(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку пагинации из клавиатуры под текстом"""
    if call.data in [str(i) for i in range(1, 12)]:
        page = int(call.data)
        async with state.proxy() as user_data:
            user_data["Пагинация"] = page
        await bot.delete_message(
            call.message.chat.id,
            call.message.message_id
        )
        await send_page(return_history(f'{user_data["Тотемное животное"]}_chinese')[0][0].split("\n"), call.message, page)
        await call.answer()
    elif call.data == "Меню":
        # Удаляем текст с пагинацией
        await bot.delete_message(
            call.message.chat.id,
            message_id=call.message.message_id
        )
        # Завершаем и сбрасываем все состояния машины чтобы можно было переключится на другой раздел или выбрать тот же
        await state.finish()
        await call.message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                                  reply_markup=keyboard(1, menu, 6, space_list()))
        await call.answer()