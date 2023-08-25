from telebot.types import Message

from loader import bot


@bot.message_handler(content_types=['text'])
def text_mess(message: Message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет', parse_mode='html')
