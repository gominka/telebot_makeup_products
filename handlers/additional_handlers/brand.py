from telebot.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from loader import bot
from site_ip.response_brand import brand_handler, main_handler


@bot.message_handler(commands=['brand'])
def brand(message: Message) -> None:
    """
    Обработчик команды, срабатываемый на /brand
    :param message: Message
    :return: None
    """
    markup = InlineKeyboardMarkup(row_width=1)
    list_brand = InlineKeyboardButton(text='Вывести список всех брендов',
                                      callback_data="list_brand")
    brand_search = InlineKeyboardButton(text='Переход на сайт бренда',
                                        callback_data='brand_search')
    markup.add(list_brand, brand_search)
    bot.send_message(message.chat.id,
                     "Выберете опцию: ",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: [call.data == "brand_search",
                                               "list_brand"])
def brand_callback(call: CallbackQuery) -> None:
    """
    """
    if call.data == "brand_search":
        msg_brand = bot.send_message(call.message.chat.id, "Введите бренд: ")
        bot.register_next_step_handler(msg_brand, set_brand)
    elif call.data == "list_brand":
        try:
            file = open('brand.txt')
            a = [line.strip() for line in file]
            bot.send_message(call.message.chat.id,
                             '\n'.join(map(str, sorted(a))))
            file.close()
        except IOError:
            brand_handler()
            brand_callback(callback_data='list_brand')


def set_brand(message: Message) -> None:
    user_brand = message.text.lower()
    with open('brand.txt') as f:
        if user_brand in f.read():
            fl = list(filter(lambda x: x['brand'] == user_brand, main_handler()))
            markup = InlineKeyboardMarkup()
            button1 = InlineKeyboardButton("Перейти на сайт",
                                           url=fl[0]['website_link'])
            markup.add(button1)
            bot.send_message(message.chat.id,
                             "Для перехода на сайт нажмите на кнопку".format(message.from_user),
                             reply_markup=markup)
        else:
            markup = InlineKeyboardMarkup(row_width=1)
            list_brand = InlineKeyboardButton(text='Вывести список брендов',
                                              callback_data="list_brand")
            brand_search = InlineKeyboardButton(text='Попробовать еще раз',
                                                callback_data='brand_search')
            markup.add(list_brand, brand_search)
            bot.reply_to(message, "Не можем найти такой бренд. ",
                         reply_markup=markup)
