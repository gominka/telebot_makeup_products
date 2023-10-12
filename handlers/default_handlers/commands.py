from telebot import types

from loader import bot

from config_data.config import CUSTOM_COMMANDS
from keyboards.reply.start_btn import btn_start
from handlers.additional_handlers import brand, tag, product_type


text_messages = {
    'start':
        u'Приветствуем Вас, '
        u'{name}, '
        u'в нашем телеграм боте \n\n'
        u'Выберите условие для поиска',
    'help':
        u'Список доступных команд: \n'
        u'{commands} \n'
}


@bot.message_handler(commands=['start'])
def bot_start(message: types.Message):
    bot.send_message(message.chat.id, text_messages['start'].format(
        name=message.from_user.first_name),
                     reply_markup=btn_start(message))


@bot.message_handler(commands=['help'])
def bot_info(message: types.Message):
    text = [f"/{command} - {desk}" for command, desk in CUSTOM_COMMANDS]
    bot.reply_to(message, text_messages['help'].format(commands="\n".join(text)))


@bot.message_handler(content_types=['text'])
def txt(message: types.Message):
    if message.text == "Бренд":
        brand.brand(message)
    elif message.text == "Тэг":
        tag.tag(message)
    elif message.text == "Тип продукта":
        product_type.product_type(message)
