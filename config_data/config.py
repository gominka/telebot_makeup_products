import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

DB_NAME = os.getenv("DB_NAME")
BOT_TOKEN = os.getenv("BOT_TOKEN")

DEFAULT_COMMANDS = (
    ("start", "Начать поиск сначала"),
    ("brand", "Выбор бренда"),
    ("product_tag", "Поиск по тэгам"),
    ("product_type", "Поиск по типу продукта"),
    ("help", "Вывести справку")
)

ADDITIONAL_COMMANDS = (
    ("history", "Посмотреть историю"),
    ("favourites", "Посмотреть избранное"),
    ("name", "Вывести список продуктов"),
)

CUSTOM_COMMANDS = (
    ("low", "Сравнение товаров"),
    ("high", "Сравнение товаров"),
    ("custom", "Сортировка по рейтингу/цене"),
)

