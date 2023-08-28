import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("info", "Вывести справку"),
)

CUSTOM_COMMANDS = (
    ("brand", "Вывести cписок брендов"),
    ("name", "Вывести список продуктов"),
    ("tag", "Вывести список тэгов"),
)

ADDITIONAL_COMMANDS = (
    ("low", "Сравнение товаров"),
    ("high", "Сравнение товаров"),
    ("history", "Посмотреть историю запросов"),
    ("favourites", "Добавить в избранное"),
)