from loader import bot
from telebot import types

from numpy import loadtxt
from telebot.types import Message
import requests

base_url = "http://makeup-api.herokuapp.com/api/v1/products.json"
querystring = {"brand"}
response = requests.get(base_url)
data = response.json()


brands = [item['brand'] for item in data]


with open('brand.txt', 'w+') as f:
    for items in list(set(brands)):
        f.write('%s\n' % items)


@bot.message_handler(commands=['brand'])
def bot_info(message: Message, ) -> None:
    markup = types.InlineKeyboardMarkup(row_width=1)
    listBtn = types.InlineKeyboardButton(text='Вывести список всех брендов', callback_data="list")
    findBtn = types.InlineKeyboardButton(text='Поиск по бренду', callback_data='find')
    markup.add(listBtn, findBtn)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == "list":
        with open('brand.txt', 'r') as f:
            a = [line.strip() for line in f]
            print(a)
            bot.send_message(call.message.chat.id, a)
    elif call.data == "find":
        bot.send_message(call.message.chat.id, "Текст")
