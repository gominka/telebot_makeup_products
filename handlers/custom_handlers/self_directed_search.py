from peewee import logger
from telebot import types
from telebot.types import CallbackQuery

from handlers.default_handlers.exception_handler import exc_handler

from loader import bot
from site_ip.main_handler import conditions_list


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

    msg_user = bot.send_message(chat_id=chat_id, text="Введите условие")
    bot.register_next_step_handler(msg_user, find_user)


def find_user(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_message = message.text

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        cond = data["cond"]

        markup = types.InlineKeyboardMarkup(row_width=1)
        custom_search = types.InlineKeyboardButton(text='Поиск товаров', callback_data="check_len_responce")
        website = types.InlineKeyboardButton(text='Переход на сайт бренда', callback_data="website_link")
        cancel = types.InlineKeyboardButton(text='Отмена', callback_data='cancel_request')
        markup.add(custom_search)

        if cond == "brand":
            markup.add(website)

            data["params"]["brand"] = user_message
            logger.info(f'Выбран бренд. User_id: {user_id}, Brand: {user_message}')

        elif cond == "product_tag":
            data["params"]["product_tag"] = user_message
            logger.info(f'Выбран тэг. User_id: {user_id}, Product_tag: {user_message}')

        elif cond == "product_type":
            data["params"]["product_type"] = user_message
            logger.info(f'Выбран тип продукта. User_id: {user_id}, Product_type: {user_message}')

        markup.add(cancel)

        bot.send_message(chat_id=chat_id, text="Выберете опцию: ", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data in ["list_name_product"])
@exc_handler
def call_btn_file(call: CallbackQuery) -> None:

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]

    bot.send_message(chat_id=chat_id, text=str(conditions_list(params=params, selected_condition=call.data)))


