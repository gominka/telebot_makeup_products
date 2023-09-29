from loader import bot

from telebot import types

import requests

base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
response = requests.get(base_url)
data = response.json()
product_types = []
for item in data:
    if item['product_type'] is not None:
        if item['product_type'] not in product_types:
            product_types.append(item['product_type'])
with open('product_type.txt', 'w+') as f:
    for items in product_types:
        f.write('%s\n' % items)


@bot.message_handler(commands=['product_type'])
def bot_info(message: types.Message) -> None:
    markup = types.InlineKeyboardMarkup(row_width=1)
    list_type = types.InlineKeyboardButton(text='Вывести список типов продуктов',
                                           callback_data="list_type")
    type_search = types.InlineKeyboardButton(text='Поиск по типу',
                                             callback_data='type_search')
    markup.add(list_type, type_search)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "list_type")
def answer(call: types.CallbackQuery):
    with open('product_type.txt', 'r') as f:
        a = [line.strip() for line in f]
        bot.send_message(call.message.chat.id,
                         '\n'.join(map(str, sorted(a))))


@bot.callback_query_handler(func=lambda call: call.data == "type_search")
def answer(call: types.CallbackQuery):
    cid = call.message.chat.id
    msg_type = bot.send_message(cid, "Введите тип: ")
    bot.register_next_step_handler(msg_type, set_type)


def set_type(message: types.Message):
    user_type = message.text.lower()
    with open('product_type.txt') as f:
        if user_type in f.read():
            bot.reply_to(message, "true")
        else:
            bot.reply_to(message, "false")
