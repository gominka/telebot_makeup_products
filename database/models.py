from peewee import (
    CharField,
    IntegerField,
    Model,
    SqliteDatabase
)

from config_data.config import DB_NAME

db = SqliteDatabase(DB_NAME)


class BaseModel(Model):
    """Базования модель"""

    class Meta:
        database = db


class User(BaseModel):
    """Класс описывающий, таблицу о пользователе в базе данных"""

    user_id = IntegerField(unique=True)
    username = CharField()
    first_name = CharField()

    def __str__(self):
        return self.user_id


class Favourity(BaseModel):
    """Модель избранных товаров или условию"""

    user_id = IntegerField(null=False)
    brand = CharField(null=True)
    product_tag = CharField(null=True)
    product_type = CharField(null=True)
    id_product = CharField(null=True)


def create_models():
    db.create_tables(BaseModel.__subclasses__())
