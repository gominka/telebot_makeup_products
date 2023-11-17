from telebot.types import CallbackQuery
from loguru import logger

from database.models import History

from loader import bot


@bot.callback_query_handler(func=lambda call: call.data in ["cancel"])
def delete_message(call: CallbackQuery) -> None:
    """
    Обработчик callback-запросов, связанных с самостоятельным вводом данных пользователем

    :param call: callback-запросы
    :return: None
    """
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.delete_message(call.message.chat.id, call.message.id - 1)


@bot.callback_query_handler(func=lambda call: call.data in ["deleting_adding"])
def commands_callback_main(call: CallbackQuery) -> None:
    """
    Обработчик callback запроса, который удаляет последнюю занесенную информацию от пользователя

    :param call: callback-запрос удаления
    :return: None
    """
    History.select().order_by(History.id.desc()).get().delete_instance()
    logger.info(f'Удален последний запрос')
    bot.delete_message(call.message.chat.id, call.message.id)


@bot.callback_query_handler(func=lambda call: call.data in ["system_list_brand"])
def user_select_brand(call) -> None:
    user_brand = call.message.text.lower()
    History(brand=user_brand, user_id=call.from_user.id).save()
    logger.info('Выбранное условие: ' + user_brand + f' User_id - {call.from_user.id}')

    bot.send_message(call.message.chat.id, "ooooo")


