from keyboa.keyboards import keyboa_maker
from loguru import logger
from peewee import IntegrityError
from telebot.types import CallbackQuery

from database.models import History
from keyboards.inline.main_comm_inline_markup import search_inline_markup
from loader import bot
from site_ip.testt import cond_handler


@bot.callback_query_handler(func=lambda call: call.data in cond_handler("brand"))
def call_btn_file(call: CallbackQuery) -> None:
    """

      :param call:
      :return: None
    """

    user_id = call.from_user.id
    chat_id = call.message.chat.id
    msg_user = call.data

    try:

        History(brand=call.data, user_id=user_id).save()
        bot.send_message(
            chat_id=chat_id,
            text="Выберете опцию: ",
            reply_markup=search_inline_markup("brand")
        )
        with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
            data["brand"] = msg_user

        logger.info(f'Выбран бренд. User_id: {user_id}, Brand: {call.data}')

    except IntegrityError:
        # user_id = call.from_user.id
        # Conditions(brand_cond=None, user_id=user_id)
        # cond.save()
        bot.reply_to(message=call.message,
                     text="dddd")

@bot.callback_query_handler(func=lambda call: call.data in cond_handler("tag"))
def call_btn_file(call: CallbackQuery) -> None:
    """

      :param call:
      :return: None
    """

    user_id = call.from_user.id
    chat_id = call.message.chat.id
    msg_user = call.data

    try:

        History(tag=call.data, user_id=user_id).save()
        bot.send_message(
            chat_id=chat_id,
            text="Выберете опцию: ",
            reply_markup=search_inline_markup("tag")
        )
        with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
            data["tag"] = msg_user

        logger.info(f'Выбран тэг. User_id: {user_id}, Tag: {call.data}')

    except IntegrityError:
        # user_id = call.from_user.id
        # Conditions(brand_cond=None, user_id=user_id)
        # cond.save()
        bot.reply_to(message=call.message,
                     text="dddd")

@bot.callback_query_handler(func=lambda call: call.data in cond_handler("product_type"))
def call_btn_file(call: CallbackQuery) -> None:
    """

      :param call:
      :return: None
    """

    user_id = call.from_user.id
    chat_id = call.message.chat.id
    msg_user = call.data

    try:

        History(product_type=call.data, user_id=user_id).save()
        bot.send_message(
            chat_id=chat_id,
            text="Выберете опцию: ",
            reply_markup=search_inline_markup("product_type")
        )
        with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
            data["product_type"] = msg_user

        logger.info(f'Выбран product_type. User_id: {user_id}, Product_type: {call.data}')

    except IntegrityError:
        # user_id = call.from_user.id
        # Conditions(brand_cond=None, user_id=user_id)
        # cond.save()
        bot.reply_to(message=call.message,
                     text="dddd")