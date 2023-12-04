from loguru import logger

from telebot.types import Message

from database.models import User
from handlers.default_handlers.exception_handler import exc_handler
from user_interface import text
from loader import bot
import states.custom_states


@bot.message_handler(commands=['start'], state="*")
@exc_handler
def start_command_handler(message: Message) -> None:
    """Стартовый обработчик, срабатываемый на команду /start"""

    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    chat_id = message.chat.id

    bot.set_state(user_id=user_id, state=states.custom_states.UserState.search_state, chat_id=chat_id)

    User(user_id=user_id, username=username, first_name=first_name, last_name=last_name).save()
    logger.info(f'Добавлен новый пользователь. User_id: {user_id}')

    bot.send_message(chat_id=message.chat.id, text=text.START_MSG)


@bot.message_handler(commands=['start_again'], state="*")
@exc_handler
def start_command_handler(message: Message) -> None:
    """Обработчик, срабатываемый на команду /start_again"""

    user_id = message.from_user.id
    chat_id = message.chat.id

    bot.send_message(chat_id=chat_id, text="Ранее выбранные условия были сброшены")
    bot.delete_state(user_id, chat_id)

    bot.set_state(user_id=user_id, state=states.custom_states.UserState.search_state, chat_id=chat_id)
    bot.send_message(chat_id=chat_id, text=text.HELP_MSG)



