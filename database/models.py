from peewee import (
    CharField,
    IntegerField,
    Model,
    SqliteDatabase
)

from config_data.config import DB_NAME

db = SqliteDatabase(DB_NAME)


class BaseModel(Model):
    """
    Класс, от которого будут наследоваться все таблицы базы данных
    """

    class Meta:
        database = db


class User(BaseModel):
    """
    В классе описываем таблицу в базе данных
    """
    user_id = IntegerField(unique=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)


class History(BaseModel):
    """"
    Модель задачи
    """
    # TODO: продумать

    user_id = IntegerField(null=False)
    brand = CharField(null=True)
    tag = CharField(null=True)
    product_type = CharField(null=True)
    name = CharField(null=True)

    def __str__(self):
        return self.user_id


def create_models():
    db.create_tables(BaseModel.__subclasses__())
