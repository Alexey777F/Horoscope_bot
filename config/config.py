from typing import Dict, List
from dotenv import load_dotenv, find_dotenv
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot_token = "6150164873:AAHr7sGYxOZTVnUTK4MFfdvsSuA22v55eus"
bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()


def menu() -> Dict:
    """Функция-словарь для клавиатуры"""
    menu_btns = {"Зодиакальный 🕉": "zodiak", "Китайский 🈯": "chinese", "Японский 🈴": "japanese",
                 "Гороскоп друидов 🌳": "druids", "Гороскоп совместимости 🎎": "compatibility", "Помощь ❓": "help"}
    return menu_btns


def zodiaks() -> Dict:
    """Функция-словарь для клавиатуры"""
    zodiak = {"♈️Овен": "aries", "♉️Телец": "taurus", "♊️Близнецы": "gemini", "♋️Рак": "cancer",
              "♌️Лев": "leo", "♍️Дева": "virgo", "♎️Весы": "libra", "♏️Скорпион": "scorpio",
              "♐️Стрелец": "sagittarius", "♑️Козерог": "capricorn", "♒️Водолей": "aquarius", "♓️Рыбы": "pisces"}
    return zodiak


def zodiaks_compability() -> Dict:
    """Функция-словарь для клавиатуры"""
    zodiak = {"♈️Овен": "oven", "♉️Телец": "telets", "♊️Близнецы": "bliznetsy", "♋️Рак": "rak",
              "♌️Лев": "lev", "♍️Дева": "deva", "♎️Весы": "vesy", "♏️Скорпион": "scorpion",
              "♐️Стрелец": "strelets", "♑️Козерог": "kozerog", "♒️Водолей": "vodoley", "♓️Рыбы": "ruby"}
    return zodiak


def chinese() -> Dict:
    """Функция-словарь для клавиатуры"""
    animal = {"🐁Крыса": "rat", "🐃Бык": "bull", "🐯Тигр": "tiger", "🐰Кролик": "rabbit",
              "🐉Дракон": "dragon", "🐍Змея": "snake", "🐴Лошадь": "horse", "🐑Овца": "sheep",
              "🐵Обезьяна": "monkey", "🐔Петух": "cock", "🐕Собака": "dog", "🐷Свинья": "pig"}
    return animal


def zodiak_name_list() -> List:
    """Функция-список с названиями годов гороскопа"""
    zodiac_list = ["год Крысы 🐁", "год Быка 🐃", "год Тигра 🐯", "год Кролика 🐰", "год Дракона 🐉", "год Змеи 🐍",
                   "год Лошади 🐴", "год Овцы 🐑", "год Обезьяны 🐵", "год Петуха 🐔", "год Собаки 🐕", "год Свиньи 🐷"]
    return zodiac_list


def choice_zodiac() -> Dict:
    buttons = {"Определите Мой Знак Зодиака ❓": "what is my zodiac sign",
               "Я знаю Свой Знак Зодиака 💯": "i know my zodiac sign"}
    return buttons


def dates() -> Dict:
    """Функция-словарь для клавиатуры"""
    date = {"Сегодня 📆": "today", "Завтра 📆": "tomorrow", "Неделя 📆": "week",
            "Месяц 📆": "month", "Год 📆": "year"}
    return date


def gender() -> Dict:
    """Функция-словарь для клавиатуры"""
    gen = {"Мужчина👨‍🦱": "man", "Женщина👩🏻": "woman"}
    return gen


def druid() -> Dict:
    """Функция-словарь для клавиатуры"""
    druids = {"🍏Яблоня": "druid_apple", "🌿Пихта": "druid_fir", "🍃Вяз": "druid_elm", "🪴Кипарис": "druid_cypress",
              "🌳Тополь": "druid_poplar", "🪴Картас": "druid_kartas", "🌲Сосна": "druid_pine", "🌿Ива": "druid_willow",
              "🍃Липа": "druid_linden", "🥜Орешник": "druid_hazel", "🌳Рябина": "druid_rowan", "🍁Клён": "druid_maple",
              "🌰Орех": "druid_nut", "☘Жасмин": "druid_jasmine", "🌱Каштан": "druid_chestnut", "🌳Ясень": "druid_ash",
              "🌳Граб": "druid_hornbeam", "🌿Инжир": "druid_figs", "🌳Дуб": "druid_oak",  "🍃Берёза": "druid_birch",
              "🌿Маслина": "druid_olive", "🌳Бук": "druid_beech"}
    return druids


def druid_date_list() -> List:
    """Функция-список с датами для гороскопа друидов"""
    druid_list = ["23.12 - 01.01 | 25.06 - 04.07", "02.01-11.01 | 05.07-14.07", "12.01 - 24.01 | 15.07 - 25.07",
                  "25.01 - 03.02 | 26.07 - 04.08", "04.02 - 08.02 | 05.08 - 13.08", "09.02 - 18.02 | 14.08 - 23.08",
                  "19.02 - 28-29.02 | 24. 08 - 02.09", "01.03 - 10.03 | 03.09 - 12.09", "11.03 - 20.03 | 13.09 - 22.09",
                  "22.03 - 31.03 | 24.09 - 03.10", "01.04 - 10.04 | 04.10 - 13.10", "11.04 - 20.04 | 14.10 - 23.10",
                  "21.04 - 30.04 | 24.10 - 02.11", "01.05 - 14.05 | 03.11 - 11.11", "15. 05 - 24.05 | 12.11 - 21.11",
                  "23.05 - 03.06 | 22.11 - 01.12", "04.06 - 13.06 | 02.12 - 11.12", "14.06 - 23.06 | 12.12 - 21.12",
                  "21.03 - весеннее равноденствие", "24.06 - летнее солнцестояние", "23.09 - осеннее равноденствие",
                  "21.12 - 22.12 - зимнее солнцестояние"]
    return druid_list


def zodiac_date_list() -> List:
    """Функция-список с годами рождения"""
    zodiac_list = [[str(i) for i in range(1936, 2021, 12)], [str(i) for i in range(1937, 2022, 12)],
                   [str(i) for i in range(1938, 2023, 12)], [str(i) for i in range(1939, 2024, 12)],
                   [str(i) for i in range(1940, 2025, 12)], [str(i) for i in range(1941, 2026, 12)],
                   [str(i) for i in range(1942, 2027, 12)], [str(i) for i in range(1943, 2028, 12)],
                   [str(i) for i in range(1944, 2029, 12)], [str(i) for i in range(1945, 2030, 12)],
                   [str(i) for i in range(1946, 2031, 12)], [str(i) for i in range(1947, 2032, 12)]]
    return zodiac_list


def my_zodiac_year(*args) -> str:
    """Функция для определения в год какого животного родился"""
    result = [args[2][index] for index, value in enumerate(args[1]) if args[0] in value]
    return result[0]


def space_list():
    space = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    return space
