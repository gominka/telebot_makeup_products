from telebot.types import Message

from database.models import User
import handlers.callback_handlers
from keyboards.inline.brand_inline import (
    false_brand_inline_btn,
    web_inline_btn,
    main_commands_inline_btn
)
from loader import bot
from site_ip.response_main import main_handler


@bot.message_handler(state="*", commands=['brand', 'tag', 'product_type'])
def brand(message: Message) -> None:
    """
    Обработчик команды, срабатываемый на /brand
    :param message: Message
    :return: None
    """

    if User.get_or_none(User.user_id == message.from_user.id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    if message.text == "/brand":
        bot.send_message(message.chat.id, "Выберете условие для продолжения поиска: ",
                         reply_markup=main_commands_inline_btn("brand"))

    elif message.text == "/product_type":
        bot.send_message(message.chat.id, "Выберете опцию: ",
                         reply_markup=main_commands_inline_btn("product_type"))

    elif message.text == "/tag":
        bot.send_message(message.chat.id, "Выберете опцию: ",
                         reply_markup=main_commands_inline_btn("tag"))


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


def set_type(message: Message) -> None:
    pass


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

