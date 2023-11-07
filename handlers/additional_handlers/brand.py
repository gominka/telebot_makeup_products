from keyboa.keyboards import keyboa_maker
from peewee import IntegrityError
from telebot.types import Message, CallbackQuery
from loguru import logger

from database.models import User, Conditions
from handlers import dictionary
from handlers.dictionary import emoji
from keyboards.inline.brand_inline import (
    brand_inline_btn,
    false_brand_inline_btn,
    web_inline_btn,
    search_brand_inline_btn
)
from loader import bot
from site_ip.response_main import main_handler, brand_handler


@bot.message_handler(state="*", commands=['brand'])
def brand(message: Message) -> None:
    """
    Обработчик команды, срабатываемый на /brand
    :param message: Message
    :return: None
    """

    if User.get_or_none(User.user_id == message.from_user.id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    bot.send_message(message.chat.id, "Выберете опцию: ",
                     reply_markup=brand_inline_btn())


@bot.callback_query_handler(func=lambda call: call.data in ["brand_search", "list_brand", "cancel_brand"])
def brand_callback_main(call: CallbackQuery) -> None:
    """

    :param call: CallbackQuery
    :return: None
    """

    if call.data == "brand_search":
        msg_brand = bot.send_message(call.message.chat.id, "Введите бренд: ")  # ввести или выбрать
        bot.register_next_step_handler(msg_brand, set_brand)
    elif call.data == "list_brand":
        kb_brands = keyboa_maker(items=brand_handler(), copy_text_to_callback=True, items_in_row=3)
        bot.send_message(
            chat_id=call.message.chat.id, reply_markup=kb_brands,
            text="Выберете бренд")
    elif call.data == "cancel_brand":
        last_row = Conditions.select().order_by(Conditions.id.desc()).get()
        last_row.delete_instance()
        logger.info(f'Удален последний запрос')
        bot.delete_message(call.message.chat.id, call.message.id)


def set_brand(message: Message) -> None:
    user_brand = message.text.lower()
    if check_brand(user_brand):
        fl = list(filter(lambda x: x['brand'] == user_brand, main_handler()))

        bot.send_message(message.chat.id,
                         "Для перехода на сайт нажмите на кнопку".format(message.from_user),
                         reply_markup=web_inline_btn(fl))

    else:
        bot.reply_to(message, "Не можем найти такой бренд. ",
                     reply_markup=false_brand_inline_btn)


def check_brand(user_brand) -> bool:
    """
    Происходит проверка наличия заданного бренда в cписке имеющихся брендов
    :param user_brand:
    :return: bool
    """

    with open('brand.txt') as f:
        if user_brand in f.read():
            return True
        else:
            return False


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
        elif call.data == "web" and check_brand(call.message.text.lower()):
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
