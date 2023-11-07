from keyboa.keyboards import keyboa_maker
from peewee import IntegrityError
from telebot.types import CallbackQuery
from loguru import logger

from database.models import Conditions
from handlers.default_handlers import search_condition

from handlers.dictionary import emoji, dictionary
from keyboards.inline.brand_inline import (
    web_inline_btn,
    search_brand_inline_btn,
)
from keyboards.inline.types_inline import type_search_inline_btn
from loader import bot
from site_ip.response_main import main_handler, brand_handler, product_types_handler


@bot.callback_query_handler(func=lambda call: call.data in ["cancel_request"])
def commands_callback_main(call: CallbackQuery) -> None:
    """
        :param call: CallbackQuery
        :return: None
    """
    if call.data == "cancel_request":
        last_row = Conditions.select().order_by(Conditions.id.desc()).get()
        last_row.delete_instance()
        logger.info(f'Удален последний запрос')
        bot.delete_message(call.message.chat.id, call.message.id)


@bot.callback_query_handler(func=lambda call: call.data in ["brand_search", "list_brand"])
def brand_callback_main(call: CallbackQuery) -> None:
    """
    :param call: CallbackQuery
    :return: None
    """

    if call.data == "brand_search":
        msg_brand = bot.send_message(call.message.chat.id, "Введите бренд: ")  # ввести или выбрать
        bot.register_next_step_handler(msg_brand, search_condition.set_brand)
    elif call.data == "list_brand":
        kb_brands = keyboa_maker(items=brand_handler(), copy_text_to_callback=True, items_in_row=3)
        bot.send_message(
            chat_id=call.message.chat.id, reply_markup=kb_brands,
            text="Выберете бренд")


@bot.callback_query_handler(func=lambda call: call.data in brand_handler())
def brand_condition_search(call: CallbackQuery) -> None:
    """
      :param call:
      :return: None
    """

    try:
        user_id = call.from_user.id
        cond = Conditions(brand_cond=call.data,
                          user_id=user_id)
        cond.save()

        bot.send_message(call.message.chat.id,
                         "Выберете опцию: ",
                         reply_markup=search_brand_inline_btn())

        logger.info(f'Выбран бренд. User_id: {user_id}, Brand: {call.data}')

    except IntegrityError:
        user_id = call.from_user.id
        cond = Conditions(brand_cond=None,
                          user_id=user_id)
        cond.save()
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


@bot.callback_query_handler(func=lambda call: call.data in ["branding", "web"])
def brand_condition(call: CallbackQuery) -> None:
    """

    :param call: CallbackQuery
    :return: None
    """
    try:
        cond = Conditions(brand_cond=call.data,
                          user_id=call.from_user.id)
        cond.save()
        if call.data == "branding":
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
        elif call.data == "web" and search_condition.check_brand(call.message.text.lower()):
            fl = list(filter(lambda x: x['brand'] == call.data, main_handler()))
            bot.send_message(call.message.chat.id,
                             "Для перехода на сайт нажмите на кнопку".format(call.message.from_user),
                             reply_markup=web_inline_btn(fl))

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


@bot.callback_query_handler(func=lambda call: call.data in ["type_search", "list_type"])
def type_callback(call: CallbackQuery) -> None:
    """
    :param call: CallbackQuery
    :return: None
    """
    if call.data == "type_search":
        msg_brand = bot.send_message(call.message.chat.id, "Введите тип: ")  # ввести или выбрать
        bot.register_next_step_handler(msg_brand, search_condition.set_type)
    elif call.data == "list_type":
        kb_types = keyboa_maker(items=product_types_handler(), copy_text_to_callback=True, items_in_row=3)
        bot.send_message(
            chat_id=call.message.chat.id, reply_markup=kb_types,
            text="Please select one of the type:")


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
