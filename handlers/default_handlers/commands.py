from telebot import types

from loader import bot

from config_data.config import CUSTOM_COMMANDS
from keyboards.reply.start_btn import btn_start

text_messages = {
    'start':
        u'Приветствуем Вас, '
        u'{message.from_user.first_name}, '
        u'в нашем телеграм боте \n\n'
        u'Выберите условие для поиска',
    'help':
        u'Список доступных команд: \n'
        u'{commands} \n'
}


@bot.message_handler(commands=['help'])
def bot_info(message: types.Message):
    print('1')
    text = [f"/{command} - {desk}" for command, desk in CUSTOM_COMMANDS]
    bot.reply_to(message, text_messages['help'].format(commands="\n".join(text)))


@bot.message_handler(commands=['start'])
def bot_start(message: types.Message):
    bot.send_message(message.chat.id, f'Приветствуем Вас, '
                                      f'{message.from_user.first_name}, '
                                      f'в нашем телеграм боте \n\n'
                                      f'Выберите условие для поиска', reply_markup=btn_start)
