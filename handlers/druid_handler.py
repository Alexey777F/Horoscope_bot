from aiogram.types import Message, CallbackQuery
from config.config import dp, bot, druid, menu, choice_zodiac, space_list, druid_date_list
from keyboard.paginator import send_page
from keyboard.keyboard import keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.db import return_history


class Druid(StatesGroup):
    zodiac_choice = State()
    zodiac_name = State()
    pagination_page = State()


@dp.callback_query_handler(text=["Гороскоп друидов 🌳"])
async def druid_inline_keyboard(call: CallbackQuery):
    """Колбек-хендлер который ловит кнопку Гороскоп друидов 🌳"""
    await Druid.zodiac_choice.set()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("Выберите интересующий раздел", reply_markup=keyboard(1, choice_zodiac, 2, space_list()))


@dp.message_handler(lambda message: message.text, state=Druid.zodiac_choice)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(state=Druid.zodiac_choice, text=["Определите Мой Знак Зодиака ❓"])
async def what_is_my_zodiac_sign(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку "Определите Мой Знак Зодиака ❓"""
    await state.finish()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("Список знаков зодиака по датам", reply_markup=keyboard(1, druid, 22, druid_date_list()))
    await call.message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                         reply_markup=keyboard(1, menu, 6, space_list()))
    await call.answer()


@dp.callback_query_handler(state=Druid.zodiac_choice, text=["Я знаю Свой Знак Зодиака 💯"])
async def i_know_my_zodiac_sign(call: CallbackQuery, state: FSMContext):
    """Колбек-хендлер который ловит кнопку Я знаю Свой Знак Зодиака 💯"""
    await state.finish()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await Druid.zodiac_name.set()
    await call.message.answer("Выберите ваше древо 🌳", reply_markup=keyboard(3, druid, 22, space_list()))


@dp.message_handler(lambda message: message.text, state=Druid.zodiac_name)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Воспользуйтесь кнопками Выше 📱")


@dp.callback_query_handler(state=Druid.zodiac_name, text=[key for key in druid().keys()])
async def druid_callback(call: CallbackQuery, state: FSMContext):
    tree = call.data
    async with state.proxy() as user_data:
        user_data["Древо"] = druid()[tree]
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(f"Вы выбрали {tree.lower()}")
    await call.message.answer_photo(open(f"photos_light/{user_data['Древо']}.jpeg", "rb"))
    await send_page(return_history(f'{user_data["Древо"]}')[0][0].split("\n"), call.message)
    await Druid.next()
    await call.answer()


@dp.message_handler(lambda message: message.text, state=Druid.pagination_page)
async def check_birthday(message: Message, state: FSMContext):
    """Хендлер который отклоняет введение с клавиатуры"""
    if message.text == "/start":
        await state.finish()
        await message.answer("Узнайте что говорят звёзды и приготовила для Вас судьба✨💫🌟\n\n",
                             reply_markup=keyboard(1, menu, 6, space_list()))
    else:
        await message.reply("Нажмите на кнопку - 'Перейти в главное меню 🌟'")


@dp.callback_query_handler(lambda call: True, state=Druid.pagination_page)
async def pagination_callback(call: CallbackQuery, state: FSMContext):
    if call.data in [str(i) for i in range(1, 12)]:
        page = int(call.data)
        async with state.proxy() as user_data:
            user_data["Пагинация"] = page
        await bot.delete_message(
            call.message.chat.id,
            call.message.message_id
        )
        await send_page(return_history(f'{user_data["Древо"]}')[0][0].split("\n"), call.message,
                        page)
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