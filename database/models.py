from peewee import (
    CharField,
    IntegerField,
    Model,
    SqliteDatabase,
    AutoField,
    ForeignKeyField
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
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)


class Conditions(BaseModel):
    """"
    Модель задачи
    """
    cond_id = AutoField()
    user = ForeignKeyField(User, backref="conditions")
    brand = CharField()
    tag = CharField()
    product_type = CharField()


def create_models():
    db.create_tables(BaseModel.__subclasses__())
