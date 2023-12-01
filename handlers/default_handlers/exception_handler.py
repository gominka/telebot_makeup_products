import traceback
from time import time, ctime, sleep
from typing import Callable, Union
import functools

from peewee import IntegrityError
from telebot import types

from database.models import Favourity
from keyboards.reply.reply_keyboards import get_reply_keyboard
from loader import bot
from user_interface import text


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
                    bot.send_message(chat_id=message.chat.id, text="Некорректнный ввод")
                else:
                    bot.send_message(chat_id=message.chat.id, text="Ошибка ввода")
                bot.register_next_step_handler(message=message, callback=exc_handler(method))

        except IntegrityError:
            bot.send_message(chat_id=message.chat.id, text=text.HELP_MSG)

        except Exception as exception:
            bot.reply_to(message, "Для начала поиска нажмите. Напишите /start")

            with open('errors_log.txt', 'a') as file:
                file.write('\n'.join([ctime(time()), exception.__class__.__name__, traceback.format_exc(), '\n\n']))
            sleep(1)

    return wrapped


def reset_data(user_id: int) -> None:
    """Сброс данных пользователя"""

    user = Favourity.get(Favourity.user_id == user_id)
    user.delete_instance()
