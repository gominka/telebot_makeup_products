from keyboa.keyboards import keyboa_maker
from peewee import IntegrityError
from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from loguru import logger

from database.models import User, Conditions
from handlers import dictionary
from handlers.dictionary import emoji
from keyboards.inline.brand_inline import  false_brand_inline_btn, web_inline_btn
from loader import bot
from site_ip.response_main import main_handler, brand_handler


@bot.message_handler(state="*", commands=['history'])
def brand(message: Message) -> None:
    """
    Обработчик команды, срабатываемый на /brand
    :param message: Message
    :return: None
    """

    if User.get_or_none(User.user_id == message.from_user.id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    markup = InlineKeyboardMarkup(row_width=1)
    brands = InlineKeyboardButton(text='Вывести историю поиска брендов',
                                  callback_data="brands_history")
    types = InlineKeyboardButton(text='Вывести историю поиска типов',
                                 callback_data="types_history")
    tags = InlineKeyboardButton(text='Вывести историю поиска типов',
                                callback_data="tags_history")
    products = InlineKeyboardButton(text='Вывести историю поиска продуктов',
                                    callback_data="products_history")
    all_history = InlineKeyboardButton(text='Вывести историю поиска',
                                       callback_data="all_history")

    markup.add(brands, types, tags, products, all_history)

    bot.send_message(message.chat.id, "Выберите условие: ", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ["brands_history", "types_history", "tags_history",
                                                            "products_history", "all_history"])
def history_command_callback(call: CallbackQuery) -> None:
    """

    :param call: CallbackQuery
    :return: None
    """

    user_id = call.from_user.id
    if call.data == "brands_history":
        try:
            sql_select_query = Conditions.select(Conditions.brand_cond).where(Conditions.user_id == user_id)
            result = []
            for row in sql_select_query:
                result.append(str(row))
            bot.reply_to(call.message, "{}".format(set(result)))
        except TypeError:
            bot.reply_to(call.message, "История отсутствует")

    elif call.data == "types_history":
        try:
            sql_select_query = Conditions.select(Conditions.product_type_cond).where(Conditions.user_id == user_id)
            result = []
            for row in sql_select_query:
                result.append(str(row))
            bot.reply_to(call.message, "{}".format(set(result)))

        except TypeError:
            bot.reply_to(call.message, "История отсутствует")

    elif call.data == "tags_history":
        try:
            sql_select_query = Conditions.select(Conditions.tag_cond).where(Conditions.user_id == user_id)
            result = []
            for row in sql_select_query:
                result.append(str(row))
            bot.reply_to(call.message, "{}".format(set(result)))
        except TypeError:
            bot.reply_to(call.message, "История отсутствует")

