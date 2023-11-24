import traceback
from time import time, ctime, sleep
from typing import Callable, Union
import functools

from peewee import IntegrityError
from telebot import types

from database.models import History
from handlers.default_handlers import start_command
from loader import bot
from user_interface import text
from user_interface.emoji import emoji


def exc_handler(method: Callable) -> Callable:
    """ Декоратор. Логирует исключение вызванной функции, уведомляет пользователя об ошибке """
    @functools.wraps(method)
    def wrapped(message: Union[types.Message, types.CallbackQuery]) -> None:
        try:
            method(message)
        except ValueError as exception:
            if isinstance(message, types.CallbackQuery):
                message = message.message
            if exception.__class__.__name__ == 'JSONDecodeError':
                reset_data(message.chat.id)
                exc_handler(method(message))
            else:
                if str(exception) == 'Range Error':
                    bot.send_message(chat_id=message.chat.id,
                                     text="Ошибка")
                else:
                    bot.send_message(chat_id=message.chat.id, text="Ошибка")
                bot.register_next_step_handler(message=message, callback=exc_handler(method))

        except IntegrityError:
            bot.send_message(chat_id=message.chat.id, text=text.HELP.format(
                    emoji['condition']['brand'],
                    emoji['condition']['tag'],
                    emoji['condition']['product_type'],
                    emoji['condition']['name']))

        except Exception as exception:
            bot.send_message(chat_id=message.chat.id, text="Ошибка")
            with open('errors_log.txt', 'a') as file:
                file.write('\n'.join([ctime(time()), exception.__class__.__name__, traceback.format_exc(), '\n\n']))
            sleep(1)
            start_command.start_command_handler(message)

    return wrapped


def reset_data(user_id: int) -> None:
    """
    Сброс данных пользователя (json файла).
    :param user_id: user_id
    """
    user = History.get(History.user_id == user_id)
    user.delete_instance()
