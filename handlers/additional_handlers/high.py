from telebot import types

from loader import bot


@bot.message_handler(commands=['high'])
def high(message: types.Message):
    """
    Команда, выводящая значения по заданному максимальному условию, стоимости или рейтингу
    :param message:
    :return:
    """
    markup = types.InlineKeyboardMarkup(row_width=1)
    max_price = types.InlineKeyboardButton(text='Поиск по цене',
                                           callback_data="max_price")
    max_rating = types.InlineKeyboardButton(text='Поиск по рейтингу',
                                            callback_data='max_rating')
    markup.add(max_price, max_rating)
    bot.send_message(message.chat.id, 'Выберите условие поиска:', reply_markup=markup)


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
