from telebot.types import CallbackQuery

import states

from loader import bot
from user_interface import text


@bot.callback_query_handler(func=lambda call: call.data in ["user_search_brand", "user_search_tag",
                                                            "user_search_product_type", "user_search_name"])
def user_product_selection(call: CallbackQuery) -> None:
    """
    Обработчик callback-запросов, связанных с самостоятельным вводом данных пользователем

    :param call: callback-запросы
    :return: None
    """
    user_id = call.from_user.id
    chat_id = call.message.chat.id

    bot.send_message(chat_id=chat_id, text=text.USER_HANDLER)
    bot.set_state(user_id=user_id, state=states.custom_states.UserState.search_in_file, chat_id=chat_id)
