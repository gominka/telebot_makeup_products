from peewee import IntegrityError
from loguru import logger

from telebot.types import Message

from database.models import User
from keyboards.reply.reply_keyboards import get_reply_keyboard
from user_interface import text
from loader import bot
import states.custom_states
from user_interface.emoji import emoji


@bot.message_handler(state="*", commands=['start', 'help'])
def handle_start(message: Message) -> None:
    """
    Стартовый обработчик, срабатываемый на команды /start и /help

    :param message: сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    chat_id = message.chat.id

    try:
        User(user_id=user_id, username=username, first_name=first_name, last_name=last_name).save()
        logger.info(f'Добавлен новый пользователь. User_id: {user_id}')

        bot.set_state(user_id=user_id, state=states.custom_states.UserState.search_state, chat_id=chat_id)
        bot.send_message(
            chat_id=message.chat.id,
            text=text.START,
            reply_markup=get_reply_keyboard(["/brand", "/tag", "/product_type"])
        )

    except IntegrityError:
        # TODO: уже есть в базе
        bot.set_state(user_id=user_id, state=states.custom_states.UserState.search_state, chat_id=chat_id)
        bot.send_message(
            chat_id=message.chat.id,
            text=text.HELP.format(
                emoji['condition']['brand'],
                emoji['condition']['tag'],
                emoji['condition']['product_type'],
                emoji['condition']['name']
            )
        )
