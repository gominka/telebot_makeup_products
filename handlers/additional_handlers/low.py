from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['low'])
def low(message: Message) -> None:
    pass
