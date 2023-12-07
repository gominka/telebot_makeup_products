import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

DB_NAME = os.getenv("DB_NAME")
BOT_TOKEN = os.getenv("BOT_TOKEN")

DEFAULT_COMMANDS = (
    ("start", "Начать поиск"),
    ("brand", "Выбор бренда"),
    ("product_tag", "Поиск по тэгам"),
    ("product_type", "Поиск по типу продукта"),
    ("start_again", "Начать поиск сначала")
)

ADDITIONAL_COMMANDS = (
    ("history", "Посмотреть историю"),
    ("my_favorites", "Посмотреть избранное"),
    ("name", "Вывести список продуктов"),
)

CUSTOM_COMMANDS = (
    ("low", "Сравнение товаров"),
    ("high", "Сравнение товаров"),
    ("custom", "Сортировка по рейтингу/цене"),
)

