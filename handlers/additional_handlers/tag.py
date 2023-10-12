import os

import requests

from loader import bot

from telebot import types

from keyboards.inline.main_handler import command_tag_markup
from site_ip.response_brand import tag_handler


@bot.message_handler(commands=['tag'])
def tag(message: types.Message) -> None:
    bot.send_message(message.chat.id,
                     'Выберите опцию:',
                     reply_markup=command_tag_markup())
    try:
        file = open('tag.txt')
        file.close()
    except IOError:
        tag_handler()


@bot.callback_query_handler(func=lambda call: call.data == ["list_tag", "tag_search"])
def answer(call: types.CallbackQuery) -> None:
    if call.data == "tag_search":
        msg_tag = bot.send_message(call.message.chat.id, "Введите тэг: ")
        bot.register_next_step_handler(msg_tag, set_tag)
    elif call.data == "list_tag":
        with open('tag.txt', 'r') as f:
            a = [line.strip() for line in f]
            bot.send_message(call.message.chat.id,
                             '\n'.join(map(str, sorted(a))))


def set_tag(message: types.Message) -> None:
    user_tag = message.text
    with open('tag.txt') as f:
        if user_tag in f.read():
            response = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json?tag={}".format(user_tag))
            data = response.json()
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn_tag = types.InlineKeyboardButton(text='Поиск по бренду',
                                                 callback_data="sec_brand")
            btn_type = types.InlineKeyboardButton(text='Поиск по типу',
                                                  callback_data="sec_type")
            btn_name = types.InlineKeyboardButton(text='Поиск по названию',
                                                  callback_data='name')
            markup.add(btn_tag, btn_type, btn_name)
            bot.send_message(message.chat.id,
                             "В опцию: ",
                             reply_markup=markup)
            id_user = [item['id'] for item in data]

            try:
                if os.stat("id.txt").st_size == 0:
                    with open('id.txt', 'w+') as f:
                        for items in id_user:
                            f.write('%s\n' % items)
                else:
                    with open('id.txt', 'r') as f:
                        alist = [line.rstrip() for line in f]
                        new_list = list(set(id_user) & set(alist))
                        print(new_list)
            except IOError:
                with open('id.txt', 'w+') as f:
                    for items in id_user:
                        f.write('%s\n' % items)
        else:
            bot.reply_to(message, "Не можем найти такой бренд. ")
