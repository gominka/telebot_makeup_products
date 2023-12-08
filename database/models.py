from peewee import (
    CharField,
    IntegerField,
    Model,
    SqliteDatabase
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


class Favorite(BaseModel):
    """Model of selected products or conditions"""

    user_id = IntegerField(null=False)
    brand = CharField(null=True)
    product_tag = CharField(null=True)
    product_type = CharField(null=True)


def create_models():
    db.create_tables(BaseModel.__subclasses__())
