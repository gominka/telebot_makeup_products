from telebot import types

from loader import bot
from handlers.additional_handlers import brand, tag


@bot.message_handler(content_types=['text'])
def txt(message: types.Message):
    if message.text == "Бренд":
        brand.brand(message)
    elif message.text == "Тэг":
        tag.tag(message)