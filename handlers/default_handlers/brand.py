from loader import bot

from telebot import types
from telebot.types import Message

import requests

base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
response = requests.get(base_url)
data = response.json()
brands = [item['brand'] for item in data if item['brand'] is not None]
with open('brand.txt', 'w+') as f:
    for items in list(set(brands)):
        f.write('%s\n' % items)


@bot.message_handler(commands=['brand'])
def bot_info(message: Message, ) -> None:
    markup = types.InlineKeyboardMarkup(row_width=1)
    listBtn = types.InlineKeyboardButton(text='Вывести список всех брендов',
                                         callback_data="list")
    findBtn = types.InlineKeyboardButton(text='Поиск по бренду',
                                         callback_data='find')
    markup.add(listBtn, findBtn)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(call: types.CallbackQuery):
    if call.data == "list":
        with open('brand.txt', 'r') as f:
            a = [line.strip() for line in f]
            bot.send_message(call.message.chat.id,
                             '\n'.join(map(str, sorted(a))))
    elif call.data == "find":
        cid = call.message.chat.id
        msgBrand = bot.send_message(cid, "Введите бренд: ")
        bot.register_next_step_handler(msgBrand, set_brand)


def set_brand(message: types.Message):
    user_brand = message.text.lower()
    user_id = message.from_user.id
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
