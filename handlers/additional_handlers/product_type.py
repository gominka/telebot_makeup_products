from keyboa.keyboards import keyboa_maker
from loguru import logger
from peewee import IntegrityError
from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from database.models import User, Conditions
from handlers.dictionary import dictionary, emoji
from keyboards.inline.types_inline import type_inline_btn, type_search_inline_btn
from loader import bot
from site_ip.response_main import product_types_handler


@bot.message_handler(state="*", commands=['product_type'])
def types(message: Message) -> None:
    """
    Обработчик команды, срабатываемый на /product_type
    :param message: Message
    :return: None
    """

    if User.get_or_none(User.user_id == message.from_user.id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    bot.send_message(message.chat.id, "Выберете опцию: ",
                     reply_markup=type_inline_btn())


@bot.callback_query_handler(func=lambda call: call.data in ["type_search", "list_type"])
def type_callback(call: CallbackQuery) -> None:
    """
    :param call: CallbackQuery
    :return: None
    """
    if call.data == "type_search":
        msg_brand = bot.send_message(call.message.chat.id, "Введите тип: ")  # ввести или выбрать
        bot.register_next_step_handler(msg_brand, set_type)
    elif call.data == "list_type":
        kb_types = keyboa_maker(items=product_types_handler(), copy_text_to_callback=True, items_in_row=3)
        bot.send_message(
            chat_id=call.message.chat.id, reply_markup=kb_types,
            text="Please select one of the type:")


def set_type(message: Message) -> None:
    pass


@bot.callback_query_handler(func=lambda call: call.data in product_types_handler())
def type_condition_search(call: CallbackQuery) -> None:
    """

      :param call:
      :return: None
    """
    try:
        user_id = call.from_user.id
        cond = Conditions(product_type_cond=call.data,
                          user_id=user_id)
        cond.save()

        bot.send_message(call.message.chat.id,
                         "Выберете опцию: ", reply_markup=type_search_inline_btn())

        logger.info(f'Выбран тип продукта. User_id: {user_id}, Type: {call.data}')
    except IntegrityError:
        # user_id = call.from_user.id
        # cond = Conditions(product_type_cond=None, user_id=user_id)
        # cond.save()
        bot.reply_to(message=call.message,
                     text=dictionary['started_message']['help'].format(
                         emoji['brand'],
                         emoji['highprice'],
                         emoji['lowprice'],
                         emoji['highrating'],
                         emoji['lowrating'],
                         emoji['custom'],
                         emoji['history'],
                         emoji['favourite']))


@bot.callback_query_handler(func=lambda call: call.data in ["typing", "web"])
def type_condition(call: CallbackQuery) -> None:
    """
    """
    try:
        cond = Conditions(product_type_cond=call.data,
                          user_id=call.from_user.id)
        cond.save()

        if call.data == "typing":
            bot.reply_to(message=call.message,
                         text=dictionary['message']['brand'].format(
                             emoji['highprice'],
                             emoji['lowprice'],
                             emoji['highrating'],
                             emoji['lowrating'],
                             emoji['custom'],
                             emoji['tag'],
                             emoji['product_type'],
                             emoji['name'],
                             emoji['add'],
                             emoji['favourite']))

    except IntegrityError:
        bot.reply_to(message=call.message,
                     text=dictionary['started_message']['help'].format(
                         emoji['brand'],
                         emoji['highprice'],
                         emoji['lowprice'],
                         emoji['highrating'],
                         emoji['lowrating'],
                         emoji['custom'],
                         emoji['history'],
                         emoji['favourite']))
