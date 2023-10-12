from loader import bot

from telebot import types

from keyboards.inline.main_handler import command_type_markup
from site_ip.response_brand import types_handler


@bot.message_handler(commands=['product_type'])
def product_type(message: types.Message) -> None:
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=command_type_markup())


@bot.callback_query_handler(func=lambda call: call.data == "list_type")
def answer(call: types.CallbackQuery):
    types_handler()
    with open('product_type.txt', 'r') as f:
        bot.send_message(call.message.chat.id,
                         '\n'.join(map(str, sorted([line.strip() for line in f]))))


@bot.callback_query_handler(func=lambda call: call.data == "type_search")
def answer(call: types.CallbackQuery):
    msg_type = bot.send_message(call.message.chat.id, "Введите тип: ")
    bot.register_next_step_handler(msg_type, set_type)


def set_type(message: types.Message):
    user_type = message.text.lower()
    types_handler()
    with open('product_type.txt') as f:
        if user_type in f.read():
            bot.reply_to(message, "true")
        else:
            bot.reply_to(message, "false")
