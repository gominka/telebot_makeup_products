import json
import os
from typing import Union, List, Dict

from telebot import types


from loader import bot

from config_data.config import CUSTOM_COMMANDS
from handlers.additional_handlers import brand, tag, product_type



# @bot.message_handler(commands=['high', 'low', 'custom'])
# def low_high_handler(message: types.Message) -> None:
#     """
#     Обработчик каманд: /high, /low, /custom
#     Установка сортирующей функции, определение следующего шага обработчика
#     :param message: types.Message
#     :return None
#     """
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     price = types.InlineKeyboardButton(text='Поиск по цене',
#                                        callback_data="price")
#     rating = types.InlineKeyboardButton(text='Поиск по рейтингу',
#                                         callback_data='rating')
#     markup.add(price, rating)
#     bot.send_message(message.chat.id, 'Выберите условие поиска:',
#                      reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def txt(message: types.Message):
#     if message.text == "Бренд":
#         brand.brand(message)
#     elif message.text == "Тэг":
#         tag.tag(message)
#     elif message.text == "Тип продукта":
#         product_type.product_type(message)
