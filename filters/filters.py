import telebot
from telebot.types import Message

from loader import bot


class MainFilter(telebot.custom_filters.AdvancedCustomFilter):
    key = 'text'

    @staticmethod
    def check(message, text, **kwargs):
        return message.text in text


class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key = 'is_admin'

    @staticmethod
    def check(message: Message, **kwargs):
        return bot.get_chat_member(message.chat.id, message.from_user.id).status in ['administrator', 'creator']


@bot.message_handler(is_admin=True, commands=['admin'])  # Check if user is admin
def admin_rep(message):
    bot.send_message(message.chat.id, "Hi admin")


@bot.message_handler(is_admin=False, commands=['admin'])  # If user is not admin
def not_admin(message: Message):
    """
    :type message: object
    """
    bot.send_message(message.chat.id, "You are not admin")


@bot.message_handler(text=['hi'])  # Response to hi message
def welcome_hi(message: Message):
    bot.send_message(message.chat.id, 'You said hi')


@bot.message_handler(text=['bye'])  # Response to bye message
def bye_user(message: Message):
    bot.send_message(message.chat.id, 'You said bye')


# Do not forget to register filters
bot.add_custom_filter(MainFilter())
bot.add_custom_filter(IsAdmin())

bot.infinity_polling(skip_pending=True)  # Skip old updates
