from telebot.types import Message

from config_data.config import CUSTOM_COMMANDS
from loader import bot

text_messages = {
    'info':
        u'Список доступных команд: \n'
        u'{commands} \n'
}


@bot.message_handler(commands=['info'])
def bot_info(message):
    print('1')
    text = [f"/{command} - {desk}" for command, desk in CUSTOM_COMMANDS]
    bot.reply_to(message, text_messages['info'].format(commands="\n".join(text)))




