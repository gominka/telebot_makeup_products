import os

from peewee import *
import datetime
from dotenv import load_dotenv, find_dotenv

DATABASE_NAME = "make_up_bot"
USER = os.getenv("USER_DB")
PASSWORD = os.getenv("PASSWORD_DB")
dbhandle = MySQLDatabase(DATABASE_NAME, user=USER,
                         password=PASSWORD,
                         host='localhost')


class BaseModel(Model):
    """Базовая модель для работы с Peewee"""

    class Meta:
        database = dbhandle


class Category(BaseModel):
    """Класс, для описания таблица в базе"""
    id = PrimaryKeyField(null=False)  # поле автоматического прироста
    name = CharField(max_length=100)  # содержит имя пользователя(еп_шв)

    # поля timestamp, которые определяют настоящее время по умолчанию
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = "categories"
        order_by = ('created_at',)
