from loader import bot
from telebot import types

import requests

base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
response = requests.get(base_url)
data = response.json()
tags = [item['tag_list'] for item in data if item['tag_list'] is not None]
with open('tag.txt', 'w+') as f:
    for items in tags:
        f.write('%s\n' % items)


@bot.message_handler(commands=['tag'])
def bot_info(message: types.Message) -> None:
    markup = types.InlineKeyboardMarkup(row_width=1)
    list_tags = types.InlineKeyboardButton(text='Вывести список всех тэгов',
                                           callback_data="list_tags")
    tag_search = types.InlineKeyboardButton(text='Поиск по бренду',
                                            callback_data='tag_search')
    markup.add(list_tags, tag_search)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)




