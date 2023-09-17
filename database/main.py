import sqlite3 as sq

DB_FILE_NAME = 'user_inf.db'


def create_connect():
    return sq.connect(DB_FILE_NAME)


def init_db():
    with create_connect() as connect:
        connect.execute('''
            CREATE TABLE IF NOT EXISTS Message (
                id      INTEGER  PRIMARY KEY,
                user_id INTEGER  NOT NULL,
                text    TEXT  NOT NULL
            );
        ''')
        connect.commit()


def add_message(user_id, message):
    with create_connect() as connect:
        connect.execute(
            'INSERT INTO Message (user_id, text) VALUES (?, ?)', (user_id, message)
        )
        connect.commit()


init_db()

