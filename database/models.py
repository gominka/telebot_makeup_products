from peewee import (
    CharField,
    IntegerField,
    Model,
    SqliteDatabase,
    DateTimeField
)

from config_data.config import DB_NAME

db = SqliteDatabase(DB_NAME)


class BaseModel(Model):
    """Base Model"""

    class Meta:
        database = db


class User(BaseModel):
    """Model of users"""

    user_id = IntegerField(unique=True)
    username = CharField()
    first_name = CharField()

    def __str__(self):
        return self.user_id


class Selections(BaseModel):
    """Model of users selections"""

    user_id = IntegerField()
    product_name = CharField()
    selection_date = DateTimeField()


def create_models():
    db.create_tables(BaseModel.__subclasses__())
