from keyboa.keyboards import keyboa_maker
from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from handlers.dictionary import dictionary, emoji
from loader import bot
from site_ip.response_brand import brand_handler, main_handler

cond_brand = ""


def brands():
    try:
        file = open('brand.txt')
        brands_list = sorted([line.strip() for line in file])
        file.close()
        return brands_list
    except IOError:
        brand_handler()
        brands()


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


@bot.callback_query_handler(func=lambda call: call.data in ["brand_search", "list_brand"])
def brand_callback(call: CallbackQuery) -> None:
    """
    """
    if call.data == "brand_search":
        msg_brand = bot.send_message(call.message.chat.id, "Введите бренд: ")  # ввести или выбрать
        bot.register_next_step_handler(msg_brand, set_brand)
    elif call.data == "list_brand":
        kb_brands = keyboa_maker(items=brands(), copy_text_to_callback=True, items_in_row=3)
        bot.send_message(
            chat_id=call.message.chat.id, reply_markup=kb_brands,
            text="Please select one of the brand:")


@bot.callback_query_handler(func=lambda call: call.data in brands())
def brand_condition(call: CallbackQuery) -> None:
    """
    """
    global cond_brand
    cond_brand = call.data
    markup = InlineKeyboardMarkup(row_width=1)
    list_brand = InlineKeyboardButton(text='Поиск товаров по бренду',
                                      callback_data="branding")
    brand_search = InlineKeyboardButton(text='Переход на сайт бренда',
                                        callback_data="web")
    markup.add(list_brand, brand_search)
    bot.send_message(call.message.chat.id,
                     "Выберете опцию: ",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ["branding", "web"])
def brand_condition(call: CallbackQuery) -> None:
    """
    """
    global cond_brand
    user_brand = cond_brand
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
    elif call.data == "web":
        with open('brand.txt') as f:
            if user_brand in f.read():
                fl = list(filter(lambda x: x['brand'] == user_brand, main_handler()))
                markup = InlineKeyboardMarkup()
                button1 = InlineKeyboardButton("Перейти на сайт",
                                               url=fl[0]['website_link'])
                markup.add(button1)
                bot.send_message(call.message.chat.id,
                                 "Для перехода на сайт нажмите на кнопку".format(call.message.from_user),
                                 reply_markup=markup)


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
