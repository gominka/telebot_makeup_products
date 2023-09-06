from telebot import types

from loader import bot
from telebot.types import Message, InlineKeyboardButton

import requests

base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
querystring = {"brand"}
response = requests.get(base_url)
data = response.json()


brands = [item['brand'] for item in data]


with open('brand.txt', 'w+') as f:
    for items in list(set(brands)):
        f.write('%s\n' % items)

keyboard = types.InlineKeyboardMarkup(row_width=1)
listBtn = types.InlineKeyboardButton(text='Вывести список всех брендов', callback_data="list")
findBtn = types.InlineKeyboardButton(text='Поиск по бренду', callback_data='find')
keyboard.add(listBtn, findBtn)


@bot.message_handler(commands=['brand'])
def bot_info(message: Message) -> None:
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=keyboard)
