from loader import bot
from telebot import types

from telebot.types import Message




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
        print('list')
    elif call.data == "find":
        print('find')
