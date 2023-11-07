from peewee import IntegrityError
from loguru import logger

from telebot.types import Message

from config_data.config import CUSTOM_COMMANDS
from database.models import User
from handlers.dictionary import dictionary, emoji
from loader import bot


@bot.message_handler(commands=['start', 'help'])
def handle_start(message: Message) -> None:
    """
    Стартовый обработчик
    """
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        bot.send_message(chat_id=message.chat.id,
                         text=dictionary['started_message']['start'].format(
                             emoji['brand'],
                             emoji['highprice'],
                             emoji['lowprice'],
                             emoji['highrating'],
                             emoji['lowrating'],
                             emoji['custom'],
                             emoji['history'],
                             emoji['favourite']))
        logger.info(f'Добавлен новый пользователь. User_id: {user_id}')

    except IntegrityError:
        bot.reply_to(message=message,
                     text=dictionary['started_message']['help'].format(
                         emoji['brand'],
                         emoji['highprice'],
                         emoji['lowprice'],
                         emoji['highrating'],
                         emoji['lowrating'],
                         emoji['custom'],
                         emoji['history'],
                         emoji['favourite']))
