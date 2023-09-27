from telebot import types

from loader import bot


@bot.message_handler(commands=['low'])
def low(message: types.Message):
    """
        Команда, выводящая значения по заданному минимальному условию, стоимости или рейтингу
        :param message:
        :return:
        """
    markup = types.InlineKeyboardMarkup(row_width=1)
    min_price = types.InlineKeyboardButton(text='Фильтр по цене',
                                           callback_data="min_price")
    min_rating = types.InlineKeyboardButton(text='Фильтр по рейтингу',
                                            callback_data='min_rating')
    markup.add(min_price, min_rating)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'min_price')
def callback_min_price(call: types.CallbackQuery):
    min_value = bot.send_message(call.message.chat.id, "Выберите минимальное значение: ")
    bot.register_next_step_handler(min_value, find_price)


@bot.callback_query_handler(func=lambda call: call.data == 'min_price')
def callback_min_rating(call: types.CallbackQuery):
    min_value = bot.send_message(call.message.chat.id, "Выберите минимальное значение: ")
    bot.register_next_step_handler(min_value, find_rat)


def find_price(message: types.Message):
    bot.send_message(message.chat.id, "Идёт поиск: ")


def find_rat(message: types.Message):
    bot.send_message(message.chat.id, "Идёт поиск: ")
