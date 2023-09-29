import time

from loader import bot

from telebot import types

import requests

base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
response = requests.get(base_url)
data = response.json()
start = time.time()
tags = []
for item in data:
    if item['tag_list']:
        for tag in item['tag_list']:
            if tag not in tags:
                tags.append(tag)
with open('tags.txt', 'w+') as f:
    for items in tags:
        f.write('%s\n' % items)


@bot.message_handler(commands=['tag'])
def bot_info(message: types.Message) -> None:
    markup = types.InlineKeyboardMarkup(row_width=1)
    list_brand = types.InlineKeyboardButton(text='Вывести список всех тэгов',
                                            callback_data="list_tag")
    brand_search = types.InlineKeyboardButton(text='Поиск по бренду',
                                              callback_data='tag_search')
    markup.add(list_brand, brand_search)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "list_tag")
def answer(call: types.CallbackQuery):
    with open('tags.txt', 'r') as f:
        a = [line.strip() for line in f]
        bot.send_message(call.message.chat.id,
                         '\n'.join(map(str, sorted(a))))


@bot.callback_query_handler(func=lambda call: call.data == "tag_search")
def answer(call: types.CallbackQuery):
    cid = call.message.chat.id
    msg_brand = bot.send_message(cid, "Введите тэг: ")

