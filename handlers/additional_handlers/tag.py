import os

import requests

from loader import bot

from telebot import types

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



def set_sec_brand(message: types.Message) -> None:
    user_brand = message.text.lower()
    with open('brand.txt') as f:
        if user_brand in f.read():
            response = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json?brand={}".format(user_brand))
            data = response.json()
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn_tag = types.InlineKeyboardButton(text='Поиск по тэгу',
                                                 callback_data="sec_tag")
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
            bot.reply_to(message, "Не можем найти такой бренд. ",
                         reply_markup=false_brand_markup())


def sec_brand(message: types.Message) -> None:
    user_brand = message.text.lower()
    with open('brand.txt') as f:
        if user_brand in f.read():
            fl = list(filter(lambda x: x['brand'] == user_brand, main_handler()))
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Перейти на сайт",
                                                 url=fl[0]['website_link'])
            markup.add(button1)
            bot.send_message(message.chat.id,
                             "Для перехода на сайт нажмите на кнопку".format(message.from_user),
                             reply_markup=markup)
        else:
            bot.reply_to(message, "Не можем найти такой бренд. ",
                         reply_markup=false_brand_markup())


@bot.callback_query_handler(func=lambda call: call.data == [call.data == "tag_search", "taging_search",
                                                        "list_tag", "sec_tag", "name"])
def answer(call: types.CallbackQuery) -> None:
    if call.data == "tag_search":
        msg_tag = bot.send_message(call.message.chat.id, "Введите тэг: ")
        bot.register_next_step_handler(msg_tag, tag.set_tag)
    elif call.data == "list_tag":
        with open('tag.txt', 'r') as f:
            a = [line.strip() for line in f]
            bot.send_message(call.message.chat.id,
                             '\n'.join(map(str, sorted(a))))
    elif call.data == "taging_search":
        msg_type = bot.send_message(call.message.chat.id, "Введите тэг: ")
        bot.register_next_step_handler(msg_type, tag.set_sec_tag)

    elif call.data == "sec_tag":
        pass
    elif call.data == "name":
        pass


@bot.callback_query_handler(func=lambda call: call.data == ["list_tag", "tag_search"])
def answer(call: types.CallbackQuery) -> None:
    if call.data == "tag_search":
        msg_tag = bot.send_message(call.message.chat.id, "Введите тэг: ")
        bot.register_next_step_handler(msg_tag, tag.set_tag)
    elif call.data == "list_tag":
        with open('tag.txt', 'r') as f:
            a = [line.strip() for line in f]
            bot.send_message(call.message.chat.id,
                             '\n'.join(map(str, sorted(a))))

