from telebot import types

from loader import bot

from keyboards.inline.conditions import comparison


@bot.message_handler(commands=['high'])
def high(message: types.Message):
    c = 'max'
    bot.send_message(message.chat.id, 'Выберите условие поиска:', reply_markup=comparison(c))


@bot.message_handler(commands=['low'])
def low(message: types.Message):
    c = 'min'
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=comparison(c))


@bot.message_handler(commands=['custom'])
def custom(message: types.Message) -> None:
    c = 'custom'
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=comparison(c))


@bot.callback_query_handler(func=lambda call: call.data == 'min_price')
def callback_min_price(call: types.CallbackQuery):
    min_value = bot.send_message(call.message.chat.id, "Выберите минимальное значение: ")
    bot.register_next_step_handler(min_value, find_price)


@bot.callback_query_handler(func=lambda call: call.data == 'min_price')
def callback_min_rating(call: types.CallbackQuery):
    min_value = bot.send_message(call.message.chat.id, "Выберите минимальное значение: ")
    bot.register_next_step_handler(min_value, find_rat)


@bot.callback_query_handler(func=lambda call: call.data == 'max_price')
def callback_max(call: types.CallbackQuery):
    max_value = bot.send_message(call.message.chat.id, "Выберите максимальное значение: ")
    bot.register_next_step_handler(max_value, find_price)


@bot.callback_query_handler(func=lambda call: call.data == 'max_rating')
def callback_max(call: types.CallbackQuery):
    max_value = bot.send_message(call.message.chat.id, "Выберите максимальное значение: ")
    bot.register_next_step_handler(max_value, find_rat)


def find_price(message: types.Message):
    bot.send_message(message.chat.id, "Идёт поиск: ")


def find_rat(message: types.Message):
    bot.send_message(message.chat.id, "Идёт поиск: ")
