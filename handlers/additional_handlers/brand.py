from loader import bot

from telebot import types

import requests

base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
response = requests.get(base_url)
data = response.json()
brands = [item['brand'] for item in data if item['brand'] is not None]
with open('brand.txt', 'w+') as f:
    for items in list(set(brands)):
        f.write('%s\n' % items)


@bot.message_handler(commands=['brand'])
def bot_info(message: types.Message) -> None:
    markup = types.InlineKeyboardMarkup(row_width=1)
    list_brand = types.InlineKeyboardButton(text='Вывести список всех брендов',
                                            callback_data="list_brand")
    brand_search = types.InlineKeyboardButton(text='Поиск по бренду',
                                              callback_data='brand_search')
    markup.add(list_brand, brand_search)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "list_brand")
def answer(call: types.CallbackQuery):
    with open('brand.txt', 'r') as f:
        a = [line.strip() for line in f]
        bot.send_message(call.message.chat.id,
                         '\n'.join(map(str, sorted(a))))


@bot.callback_query_handler(func=lambda call: call.data == "brand_search")
def answer(call: types.CallbackQuery):
    cid = call.message.chat.id
    msg_brand = bot.send_message(cid, "Введите бренд: ")
    bot.register_next_step_handler(msg_brand, set_brand)


def set_brand(message: types.Message):
    user_brand = message.text.lower()
    with open('brand.txt') as f:
        if user_brand in f.read():
            fl = list(filter(lambda x: x['brand'] == user_brand, data))
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Перейти на сайт",
                                                 url=fl[0]['website_link'])
            markup.add(button1)
            bot.send_message(message.chat.id,
                             "Для перехода на сайт нажмите на кнопку)".format(message.from_user),
                             reply_markup=markup)
        else:
            bot.reply_to(message, "false")
