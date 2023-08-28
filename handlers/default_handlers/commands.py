from telebot.types import Message

from config_data.config import CUSTOM_COMMANDS
from loader import bot

text_messages = {
    'start':
        u'Добро пожаловать {name}!\n\n',
    'info':
        u'Список доступных команд: \n'
}


@bot.message_handler(commands=['info'])
def bot_info(message):
    bot.reply_to(message, text_messages['info'])
    text = [f"/{command} - {desk}" for command, desk in CUSTOM_COMMANDS]
    bot.send_message(message.from_user.id, "\n".join(text))


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.reply_to(message, text_messages['start'].format(name=message.from_user.first_name))

