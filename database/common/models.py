from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('my_make_up')


class ModelBase(pw.Model):
    """Базовая модель для работы с Peewee"""
    created_at = pw.DateField(default=datetime.now())

    class Meta:
        database = db


class History(ModelBase):
    number = pw.TextField()
    message = pw.TextField()
